# -*- coding: utf-8 -*-
documentation = [
_(u"""Originally by Brian Vogel."""),
"",_(u"""The ribbons in Windows, whether in File Explorer or specific programs like MS-Word or others, are really just another variant on a menu system that has as its intention making the most commonly used items “front and center” for fast access."""),
"",_(u"""Many of the things you already know for using a menu-driven system still apply for accessing the ribbons.  In the old-style menus you hit ALT plus the appropriate letter to drop down that menu.  In the ribbon system you hit ALT plus the appropriate letter to open a specific tab that shows the ribbon you need to access."""),
"",_(u"""Every blessed option on a ribbon has a direct keyboard shortcut to activate it, so it is worth learning what your own “greatest hits” generally are and what their keyboard shortcuts are to save yourself a lot of time.  That being said, we all occasionally have to use a feature that we seldom use, so on occasion a brute force “tab by tab” search, either through a whole ribbon or within select groups on a given ribbon might be needed."""),
"",_(u"""One big difference between using the old-style menu system and ribbons is that the up, down, left, and right arrow keys were your primary navigation keys for menus.  They are not for ribbon navigation.  Your primary navigation key is the TAB key, along with CTRL+Right Arrow (or Left Arrow) if you wish to jump from ribbon group to ribbon group."""),
"",_(u"""What follows will use File Explorer as the program and its various buttons and ribbons.  This is from a system running Windows 10, Version 1607 (the Anniversary Update), Build 14393.187.  I do not recall having customized File Explorer in any way, so this should apply to File Explorer in its “out of the box” state.  The principles of navigation of the ribbon apply in any program that uses one, but the buttons and ribbons in other programs obviously differ."""),
"",_(u"""Just like it always has been with menus so it remains with tabs/ribbons that pressing ALT throws focus to the controls.  Of course, controls are context sensitive and so which are available versus which are not directly depends on the item or items you have selected in the File Explorer window.  The primary choices after hitting ALT are:"""),
"",_(u"""* F for the File Tab, which does not have a ribbon but does have a number of controls"""),
_(u"""* H for the Home Tab, which is by far and away the one that gets the most use"""),
_(u"""* S for the Share Tab"""),
_(u"""* V for the View Tab"""),
_(u"""* 1 for the properties dialog if you have a file or folder selected.  Can also be invoked using ALT+Enter instead"""),
_(u"""* 2 for the New Folder button.  Can also be invoked using CTRL+Shift+N instead"""),
_(u"""* E to invoke the Windows Help function for File Explorer.  Opens a web browser window in whatever browser you’ve set up as your default."""),
"",_(u"""## The Structure of Tabs & Ribbons"""),
"",_(u"""Most Tabs have a single ribbon, though some have none and are more “menu-like” structure with a collection of controls that are not split into groups/toolbars.  The File Tab is like this.  Since the Home Tab and its ribbon get the heavy-duty workload the vast majority of the time I will focus on it as my primary in-depth example.  The following will presume that you’ve already hit ALT followed by H and have the Home Tab open."""),
"",_(u"""To move directly in to the ribbon hit the down arrow key once, or hit the TAB key four times, as it traverses some controls on the window prior to entering the ribbon.  You will now be sitting in the Clipboard group/toolbar of the ribbon on the Pin to Quick Access control (which will be inactive unless you have a file or folder selected in the main pane of the window).  The Home Ribbon is broken in to 5 toolbars/control groups, left to right these are:"""),
"",_(u"""1.	Clipboard"""),
_(u"""2.	Organize"""),
_(u"""3.	New"""),
_(u"""4.	Open"""),
_(u"""5.	Select"""),
"",_(u"""Almost every control has a keyboard shortcut to invoke it.  The exceptions are those that involve selection from a table/list for a setting, and these have a keyboard shortcut to take you straight into the selection for that control and you can use TAB to traverse those selections."""),
"",_(u"""You can use the TAB key to do a control-by-control traversal of the entire ribbon.  The screen reader will announce when you have traversed from one toolbar/control group into the next.  You can also do a quick jump from wherever you might be within a given toolbar to the first control of the next (or previous) toolbar using CTRL+Right Arrow (Left Arrow).  When you are moving from control to control via the TAB key you will have the control announced along with the keyboard sequence (coupled with the ALT followed by letter that you’ve already entered) that would be used to invoke it directly."""),
"",_(u"""## Clipboard Toolbar/Control Group"""),
"",_(u"""Contains the following controls, I will note the direct keyboard sequence that would follow the ALT followed by H if you wish to invoke it directly within square brackets.  Some are single characters while others are two characters that must be typed rapidly :"""),
"",_(u"""* Pin to Quick Access – if a file or folder is selected will be active and will do precisely what its name states.  [PI]"""),
_(u"""* Copy [CO]   You can also use the CTRL+C keyboard shortcut to copy (which I always do)."""),
_(u"""* Paste [V]  You can also use the CTRL+V keyboard shortcut to paste (which I always do)."""),
_(u"""* Cut [T]  You can also use the CTRL+X keyboard shortcut to cut (again, which I always do)."""),
_(u"""* Copy Path [CP] Copies the full path to the file(s) or folder(s) selected to the clipboard"""),
_(u"""* Paste Shortcut [PS]  If you did a previous copy on a file, using Paste Shortcut will do what it says, paste a shortcut (symbolic link) to the original file in the folder you’re sitting in rather than an actual duplicate copy of the file."""),
"",_(u"""## Short List of Commonly Used Key Sequences for Ribbon Navigation."""),
"",_(u"""* ALT plus appropriate letter:  Throw focus on a specific tab that contains the ribbon you need to use.  For example, in MS-Word, ALT+F for File Tab or ALT+H for Home Tab."""),
_(u"""* Down Arrow, struck once.  In File Explorer this puts you into the ribbon without having to go through a couple of controls that are part of the File Explorer window itself.  You can also use this in any other program as well, but often TAB will work. I want people to be aware of this exception primarily for File Explorer since it requires four TAB presses to achieve what a single down arrow press does. """),
_(u"""* TAB – this is your primary control to control navigation key.  It’s great if you don’t know where something happens to be and need to listen for the control and its shortcut character or characters."""),
_(u"""* CTRL+Right Arrow (or Left Arrow)  move to the next (or previous) group of controls.  In the old menu system many menu items had submenus and in the ribbon system most controls are grouped together based on their functions, but all are visible.  If you know that the group you’re in definitely isn’t what you’re looking for you can quickly jump to the next or previous group rather than having to tab your way through each and every control."""),
"",_(u"""Learning the actual keyboard shortcuts for functions that you use all the time will save you a lot of time and effort.  For instance, if you use bullet lists in your Microsoft Word documents on a routine basis it’s a lot easier to hit, ALT+H,U, then down arrow through the bullet styles to choose the one you want than to hit ALT+H, CTRL+Right Arrow three times to get to the Paragraph control grouping, Enter to open the bullet list dialog (which happens to be the first control in the Paragraph group), then down arrowing through the bullet styles.  Also using keyboard shortcuts like CTRL+B to toggle bold type on/off, CTRL+I for italic, and CTRL+U for underline, is much faster than hunting for these in the Font Group via ribbon navigation."""),
]