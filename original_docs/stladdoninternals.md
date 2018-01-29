# NVDA Add-on internals: SysTray List

Author: Joseph Lee

## Introduction

When transitioning between screen readers, one of the first things people might ask is inclusion of familiar features from old screen reader in the new product. As a user who have worked with multiple screen readers, I often ask this question when moving from one screen reader to another.

As more and more people are transitioning from JAWS for Windows to NVDA, a frequently asked question is whether NVDA has a dialog to show system tray (notification area) icons. By default, NVDA does not ship with such a feature, but it can be brought back with an add-on appropriately called "SysTray List". This add-on, developed by Rui Fontes and Rui Batista, allows you to view a list of system tray or taskbar icons, and this is the add-on we'll find out how it works in this add-on internals article.

To download the add-on, go to https://addons.nvda-project.org/addons/systrayList.en.html, and for the source code, go to http://bitbucket.org/nvdaaddonteam/systraylist. Just like the previous series on StationPlaylist Studio, you don't have to use the add-on to learn about its internals, but having the source code and/or using the add-on could help you as you understand how this add-on works behind the scenes.

Important disclaimer: This add-on was not developed by the author of this article, and views expressed in this article are strictly the author's. SysTrayList add-on is copyright Rui Fontes and Rui Batista, Windows API is copyright Microsoft Corporation, NVDA is copyright NV Access, Python is copyright Python Software Foundation.

## SysTray List add-on features

After installing this add-on, you can press NVDA+F11 to view a list of system tray icons. This dialog lists the icons in the notification area, as well as buttons to cilck, double-click and do right mouse clicks.

A hidden gem of this add-on is that there is no command to view taskbar icons (that command is taken by NVDA's review cursor selection copy command (NvDA+F10)). Instead, to view taskbar icons, press NVDA+F11 twice quickly (more on how this is possible in a second). The list view changes to show taskbar icons (including pinned items). Pressing ENTER will cause NVDA to perform a left mouse click.

## Source code layout

This global plugin lives in its own directory named sysTrayList (globalPlugins/sysTrayList/__init__.py). Some add-ons, especially those that use helper modules uses package-style directory structure.

The global plugin file is composed of the following sections:

* Like any Python module, various modules are imported.
* An event executor (more on this below) that sends mouse events specified in the parameter.
* The global plugin (class GlobalPlugin(globalPluginHandler.GlobalPlugin)) which contains the systray script and helper functions.
* The dialog class (globalPlugins.systraylist.SystrayListDialog) for displaying the dialog itself.

## NVDA+F11: A behind the scenes tour

So what exactly happens when you press NVDA+F11? When you press this command after installing the add-on, NVDA will do the following:

1. Determines if you pressed this command once or twice by calling scriptHandler.getLastScriptRepeatCount. If you press NvDA+F11 and then you press NVDA+F11 within the next half a second, NvDA will treat this as multiple press of this command.
2. If NVDA sees that you have pressed NVDA+F11 once, NvDA will locate system tray icons, otherwise it'll fetch taskbar icons.
3. The icon locators (both are private functions) will do the following to obtain a list of icons needed:
	1. Each locator has a list of window paths (window class names) to be searched to locate the needed icons and their locations, and this list is used by another private function to obtain a list of icon names.
	2. The private function will use user32.dll's FindWindowEx to locate the handle to the icons list where the icons live (more on this in the next section).
	3. Once the handle is found, NVDA will locate the first icon via NVDAObjects.IAccessible.getNVDAObjectFromEvent function. Then NvDA will use object navigation emulation (object, does something, object = object.next) to locate the icons and store their names and location in a list, which will then be returned to the locator routines.
4. Once the locators obtain the list of icons and their locations, it'll call another private function to open a dialog and show the requested icons. Depending on script count, it'll change the title and the label for the icons list view.
5. After you select an icon and what to do (left click (default), right click, double-click), NVDA will perform the following:
	1. NVDA will look up the location of the selected icon.
	2. NVDA will perform a series of mouse clicks (mouseEvents function, more on this routine below).

## FindWindow versus FindWindowEx and its relation to icon locators

Windows API has changed a lot in more recent versions of Windows. This came as a response to security concerns, to extend API functionality and so on. Because of this, you may see many Windows API functions that ends with "Ex" (short for "extended").

In the original version, FindWindow would return a handle to a window given the class name and child window class name. For example, if we need to obtain a handle to a menu bar in an app, we would use:

hwnd = FindWindow("WindowClassName", "MenuBar")

Specifying NULL (None) for the second parameter would search for the top-level window.

As opposed to FindWindow, FindWindowEx takes two additional parameters, namely the handle to a window where the search should begin and which child window to search (or a group of windows to search). This results in the following signature:

hwnd = FindWindowEx(handle, childGroup, className, childClassName)

For example, the above call to FindWindow could become:

parentHwnd = FindWindow("Desktop", None)
hwnd = FindWindowEx(parentHwnd, None, "WindowClassName", "MenuBar")

## The "magic" behind icon name locator function

When asked by NVDA, the icon name locator function (noted above) will try its best to locate the first system tray or taskbar icon. This is how it is done:

1. For element in the path to be searched, it calls FindWindowEx to locate the needed handle. At first, this handle is 0, and search begins from the shell (desktop) object (the root of all windows).
2. Depending on the icons you are looking for, NvDA will search the following windows:
	* For system tray list: "shell_TrayWnd" (desktop object), "TrayNotifyWnd" (notification area), "SysPager" (system tray), "ToolbarWindow32" (first system tray icon).
	*Taskbar icons in Windows XP/Server 2003: "Shell_TrayWnd" (Desktop), "RebarWindow32" (Taskbar), "MSTaskSwWClass" (Taskbar), "ToolbarWindow32"), (first taskbar icon).
	* Taskbar icons in Windows Vista/Server 2008 and later: Shell_TrayWnd" (Desktop), "RebarWindow32" (Taskbar), "MSTaskSwWClass" (Taskbar), "MSTaskListWClass") , (taskbar icon).
3. For each path (window handle if found), this function will ask Windows to search for the next window in the path and store the resulting handle.

## Conclusion

Although the idea of listing system tray icons seems easy, there is a lot going on under the hood, involving locating the correct window via Windows API and carefully designing the user interface. This shows that designing a simple add-on like this involves careful thinking, especially if it'll be used by many users around the world. I hope this article was helpful in letting you understand how simple add-on suggestions are developed and designed.

A big hint: you don't have to use this add-on to access list of system tray icons. To access system tray, press Windows+B.

Lastly, I would like to stress the fact that JAWS for Windows and NonVisual Desktop Access are two completely different screen readers. Although they have borrowed features from each other, the underlying philosophy, license type (proprietary and commercial for JAWS versus open-source and GPL for NvDA), design and programming language in use are different. Thus, please do not expect all JAWS functionality suggestions to be investigated by NV Access, or Freedom Scientific to borrow every feature from NVDA.

## References:

1. FindWindow (user32.dll) reference (Windows API): https://msdn.microsoft.com/en-us/library/windows/desktop/ms633499(v=vs.85).aspx
2. FindWindowEx (user32.dll) reference (Windows API): https://msdn.microsoft.com/en-us/library/windows/desktop/ms633500(v=vs.85).aspx
