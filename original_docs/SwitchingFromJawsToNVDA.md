<!--- Please fill out the edit message before submitting changes. Do not use this guide to promote illegal software.--->
# Switching From JAWS To NVDA

## Introduction

The purpose of this guide is to assist users of JAWS (Job Access With Speech), a commercial screen reader by Freedom Scientific to switch to the open-source screen reader NVDA (NonVisual Desktop Access) with ease. It assumes prior knowledge of JAWS and that you are proficient in its use.

It is not intended to be a replacement of the included user guide, rather as a means to make NVDA seem less daunting.

## Strengths And Weaknesses 

The intent of this guide is not to be a comparison of JAWS and NVDA, but it is necessary to mention some things that work differently.  In most daily situations, NVDA works just as well as JAWS, if not better in some cases.

## A Quick Note about NVDA's Laptop Keyboard Layout

Selecting the laptop keyboard layout does not automatically set the CapsLock key to act as the NVDA modifier key.  In NVDA's keyboard settings, a checkbox is provided next to the Keyboard Layout combo box to toggle this setting.  Press NVDA+control+k to open these settings.

## Note On The Insert Key.

As you may be aware, both JAWS and NVDA can use the insert key for its modifier key. Both screen readers treat it slightly differently, which could lead to some confusion if you are used to one or the other.

With JAWS loaded, the insert key is solely for its use. This means that, in order to use the original function assigned to it (such as switching between insert and overwrite modes in a text editor or word processor), you first have to activate JAWS's pass key through command.

NVDA, on the other hand, allows you to carry out the insert key's original function by pressing it twice quickly.
Keep this in mind the next time you're editing text while using NVDA and find yourself erasing what you've already written by typing over it.  This also works for caps lock when it is assigned as the NVDA modifier key (press it twice to toggle caps lock).

## Alternative Synthesizers

Windows OneCore voices, included in Windows 10, is used by NVDA as the default synthesizer in Windows 10.  Windows OneCore voices are responsive, natural-sounding and available in many languages.  To add extra voices install a new language in Windows 10 itself, including the language pack.  Variants of a language, such as "English (United Kingdom)" and "English (United States)" each include different voices.

The eSpeak NG synthesizer is also included with NVDA.  It is used as the default in Windows 8.1 and earlier. Like NVDA itself, eSpeak NG is also free and open-source, which is one of the reasons for its inclusion. Another being the sheer amount of languages it can speak.

Both Windows OneCore Voices, and eSpeak NG, have access to features such as "rate boost", enabling the speech rate to effectively be doubled.  You can also press SHIFT to pause, and continue, speaking, instead of CONTROL which simply stops speech.

To change synthesizer, press NVDA+control+s.  To set other voice options, press NVDA+control+v.

However, you may find that, for whatever reason, neither Windows OneCore, nor eSpeak NG is right for you. If this is the case you will be glad to know that there are alternatives, which will be discussed in the following sections.

### Eloquence

Code Factory has released a version of [eloquence as an NVDA add-on which can be purchased from this link.](http://codefactoryglobal.com/app-store/voices-for-nvda/).  A license to use Nuance's Vocalizer synthesizer is also included in the price.

See the section entitled "Scripts" for information about NVDA add-ons.

### Even more voices

If you still cannot find the perfect voice for you, the [Extra Voices page](http://community.nvda-project.org/wiki/ExtraVoices) lists several other speech synthesizers (both free and paid you can use instead.

## Terminology

Most of the time, both NVDA and JAWS share a lot of the same terminology to describe controls e.g. radio buttons, combo boxes, checkboxes etc.

One notable difference is that NVDA differentiates between single and multi-line edit fields, and will also tell you if a field is "protected" (anything you type will be replaced by asterisks).  It will also alert you if text is selected in a field when you tab over to it.  If so, typing will replace the highlighted text.

NVDA  refers to the different languages a speech synthesizer can speak as voices, and the different voices supported by your synthesizer as variants.

## Cursors

NVDA has various cursors to aid in navigating Windows and applications, similar to JAWS.  The terminology is slightly different as described below.

The PC cursor in NVDA's documentation is referred to as the system focus and system caret.

The equivalent to the JAWS cursor is a combination of object navigation, the review cursor and the various review modes; such as  Document review, object review and Screen Review. The Screen Review function is the one perhaps most similar to the JAWS cursor.  However, it is beneficial to become familiar with all of these. You will find thorough, easy to understand instructions in the user guide, or the [Basic Training for NVDA](https://www.nvaccess.org/product/basic-training-for-nvda-ebook/) ($30 AUD).

Unlike JAWS, you don't have to switch between the PC and JAWS cursor equivalents as the numpad is reserved exclusively for working with the JAWS cursor like functions.

It is worth noting that when you use object navigation or the review cursor, the mouse does not, by default, move in sync. You have to press a command to move the mouse to the location of the review cursor, which is similar to how JAWS' "invisible cursor" works. There are also commands to simulate clicking or locking both mouse buttons.

However, if you simply want to activate the current object you are focused on when using object navigation, there is a command to do this without having to move the mouse cursor to it first.

### Accessing the notification area (system tray)

NVDA does not provide a dialog to access the notification area, as this is accessible natively.  Press WINDOWS+B to access the notification area.  To move between notification area items, either use the arrow keys or press the first letter of an item.  Pressing the spacebar on an icon is the same as left-clicking the mouse.  Pressing enter is the same as double-clicking the left mouse button (there is no distinction between these in Windows 10).  Pressing the applications key or shift+f10 to open the context menu for an item.

If the first item in the notification area is "Notification chevron button", Windows is not set to show all icons.  Press ENTER or spacebar to open this and then arrow through the items.  To set Windows to always show all notification area icons, open "notification area" windows settings, or "select which icons appear on the taskbar", and ensure "Always show all icons in the notification area" is checked.

If you prefer to have a dialog you can access with NVDA+F11, there is a "SysTrayList" add-on available in the [Add-ons website](https://addons.nvda-project.org/index.en.html).

### Accessing the ribbon

Microsoft Office 2007 replaced the menu and toolbars with a "ribbon".  Like the notification area, these are accessible so NVDA does not provide a "virtual ribbon" replacement.  Microsoft has a page on [Using the keyboard to work with the ribbon](https://support.office.com/en-us/article/use-the-keyboard-to-work-with-the-ribbon-954cd3f7-2f77-4983-978d-c09b20e31f0e).  Essentially press ALT or ALT+letter to access individual ribbons.  Press CONTROL+LEFT and RIGHT ARROWS to move between groups within the current ribbon (eg Clipboard, font, paragraph, etc in Word's Home ribbon).  Press TAB to move between individual items in each ribbon and spacebar or enter to activate the current ribbon item.  The Ribbon also includes "tell me".  Press alt+q, type the command or feature you would like to access, use the arrow keys to select it from the list and enter to activate it.

### Checking the status of progress bars

Jaws provides a command control+insert+b to check the status of progress bars in the current window.  NVDA has options to have progress bars automatically reported as they update.  This can be done verbally ("5%", "6%", "23%", etc), as beeps, increasing in pitch, or both.  To adjust this, press NVDA+U.  Alternatively, it is available from the Object Presentation settings.  Press NVDA+control+o to open these settings.

### Accessing characters and emoji

Jaws has a command INSERT+4 to select symbols.  In NVDA INSERT+4 (assuming INSERT is your NVDA modifier key) toggle speak command keys, which reports when non-alphanumeric keys, such as spacebar or arrows are pressed.  To select special characters can be done in different ways in many programs.  For instance, press CONTROL+ALT+E to type a Euro symbol in Word.  The insert symbol functionality in Word (ALT+N, then U) is accessible, although some of the symbols listed in the "more symbols" dialog are not read correctly in all versions of Word.  Similarly, the "charmap" program in Windows itself allows any symbol from any font to be inserted.  Again, not all characters are completely described.

The Windows 10 Emoji window is accessible.  Press WINDOWS+. (WINDOWS+full stop).  Press TAB to move to the categories, select a category then press enter.  Press SHIFT+TAB to move to the list of emoji for that category, use the arrows to move between the available emoji and enter to insert the current emoji into text.  Press escape when done.

### Touch cursor

In JAWS 15 or later, you can use numpad keys to navigate apps using a tree-like structure, similar to how users of smartphone screen readers such as VoiceOver would navigate touchscreens. in NVDA, object navigation and object mode touch commands can be used for this purpose

## Virtual Cursor

The virtual cursor in NVDA is known as browse mode. It functions in much the same way as JAWS, giving you access to navigation quick keys, or in NVDA speak, single letter navigation.

Following are some common issues you may encounter when browsing the web with NVDA for the first time, and how to address them.

### Why Is Everything On One Line?

In case you are unaware, JAWS has two modes for displaying webpages or other documents using the virtual cursor; simple layout and screen layout.  Simple layout is the default, which displays content in a linear fashion - putting each link or control on its own line.  Screen layout formats the content similar to how it's displayed on screen.

The default in NVDA is screen layout, but you can easily switch to its version of simple layout by pressing NVDA+V while in browse mode. This will turn Screen layout off. Be sure to save your configuration after making this change with NVDA+CTRL+c.

### It Keeps Saying Clickable Clickable Clickable.

While reading webpages, you might notice sometimes that NVDA says "clickable", even multiple times on the same link or control.

As of version 2018.4 and later, NvDA will now only say clickable once, so if you experience this issue, please upgrade your copy. Because there is no cost associated with upgrading, NV Access recommends always using the latest stable release of NVDA.

You can also turn off the announcement of clickable elements entirely by going to document formatting in settings (NVDA+control+d) and unchecking "clickable" in the elements group.

### Find doesn't work on the web.

While JAWS is loaded, pressing ctrl+f in Internet Explorer or Firefox brings up the JAWS Find dialogue rather than activating the browser's built-in find command.  This is to allow you to search for text using the virtual cursor.  The regular find command will search for the next occurrence of the entered text, but will not move the virtual cursor to that location.  This is due to how screen readers interact with web pages.

NVDA has its own find command to search in browse mode, but it has not been tied to CTRL+F, so pressing that shortcut key calls up the browser's find command, hence find not working as expected.

To bring up NVDA's find dialogue, press ctrl+NVDA+F.  Type in what you wish to find then press enter.

### No commands to view forms and headings?

In JAWS, you can press JAWS+F5 to list forms, JAWS+F6 to list headings and JAWS+F7 to list links. In NVDA, the latter two have been combined into an elements list dialog, and you can access it by pressing NVDA+F7.  You can then press ALT+H to select Headings (the default), ALT+F for form field, ALT+B for buttons and ALT+D for landmarks.

## Forms Mode

The equivalent of forms mode in NVDA is focus mode, and it behaves very similar to JAWS, Even switching modes automatically when navigating through a webpage. It will play a sound alerting you to which mode you are in.  If desired, NVDA can speak the mode change rather than use a sound.

Details about Focus Mode can be found in the user guide.

## NVDA talks too much.

Sometimes you may find that NVDA can seem overly verbose, particularly in some list views. This is because as far as NVDA is concerned, list views are tables.   NVDA is configured by default to announce each column or row header.

To turn that option off, uncheck "Report table row/column headers" in the "Document Formatting" screen of NVDA's settings dialogue.  Press NVDA+control+d to open this setting screen.

## the Speech dictionary

NVDA has always included a function to edit "Speech Dictionaries", which are similar to JAWS' dictionary manager files.  There is a group of radio buttons in the Add/edit dictionary entry labelled type, which determines how the text in the pattern, (NVDA speak for actual word), box will be treated.

* anywhere, which is the default behavior.
* Whole word, which is how JAWS handles dictionary entries.
* Regular Expression, which is complicated.

You will also find a case sensitive checkbox.

Access the speech dictionaries with NVDA+n (to open the NVDA menu), then P for preferences, then D for dictionaries.  There are three options.  Default dictionary works across the board, Voice dictionary works only for the current voice, and temporary works only for the current session.  Unless you know you want one of the other two, most of the time "default dictionary" is the desired dictionary to edit.

## Scripts

Like JAWS, scripts can be added to NVDA to provide support for other applications or to add new features that can be accessed from anywhere.  These script packages are called NVDA Add-ons.  You can find add-ons on the [NVDA Community Add-ons page](http://addons.nvda-project.org/).

These include a few that emulate JAWS features not currently present in NVDA such as a system tray list, virtualise window function and ability to append text to clipboard. Scripts for popular applications such as GoldWave are also available. The user guide has details on installing add-ons, and you can read help documentation that comes with each add-on to learn more about how to use the add-on.

There is an [NVDA Developer Guide](https://www.nvaccess.org/files/nvda/documentation/developerGuide.html) with information on how to create add-ons.

## Screen Shade

From version 2019.3, NVDA includes an equivalent to JAWS' Screen Shade feature called Screen Curtain, which will blacken the screen. By default it is not assigned to a keystroke, but you can assign one from the input gestures dialogue. See the users guide for details on how to do this.

Activating the command once will enable or disable the screen curtain until you restart your computer, whereas doing so twice quickly will enable it permanently until you disable it. You can also toggle it in the vision category in Settings. 

## Remote access

In 2015, Christopher Toth and Tyler Spivey released a free add-on to allow NVDA users to provide remote support, similar to JAWS Tandem. To learn more about this add-on, go to the [NVDA Remote site](http://www.nvdaremote.com).

## Application-specific settings

NVDA can use configuration profiles, which make it possible to configure certain settings to be applied only when using a program. This is done by creating an app-specific configuration profile. To create an app-specific profile, open the Configuration Profiles dialogue while using the app in question. To open the dialogue, hit NVDA+N, to bring up the NVDA menu. arrow down until you hear configuration profiles and press enter, or press NVDA+control+P.  

When the dialogue opens, select New, and select "current application" when asked when to use this profile.  Any changes made to NVDA settings (eg synthesizer, speech rate or punctuation level) are applied to this profile.

### Alternate say all

In recent versions of JAWS, you can configure a different speech synthesizer to be used when say all is active. You can do this in NVDA by creating a say all profile in the configuration profiles menu.

Here are the steps.

1. Open the configurations profile from the main NVDA menu. Press NVDA, N, then arrow down to configuration profiles.
2. Create a new profile by tabbing to the *new* button or press alt, N.
3. After you name your profile, tab to the profile usage radio butttons. arrow down until you hear "say all". Hit *OK* 

while this profile is active, you need to complete the process by configuring the synthesizer while the say all profile is active.

## Missing Info

This guide is a community driven project and is ever expanding. If you have some experience of both JAWS and NVDA and think something's missing, feel free to add a section or revise out of date info. Spelling and grammar corrections are of course welcome. Please note that a Github account is required.

After Editing, please  preview your changes and  fill in the edit summary box before submitting.