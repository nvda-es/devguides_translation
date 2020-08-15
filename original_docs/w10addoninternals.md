# NVDA Add-on internals: Windows 10 App Essentials

Author: Joseph Lee

Revision: July 2020

## Introduction

Supporting new technologies can be fun and challenging, especially a new operating system version that changes how people perform certain tasks and introduces new ways of keeping up with changes. This is more so when it comes to letting screen readers support new operating systems such as Windows 10, which brings new ways of interacting with a computer, new set of apps and technologies, and accessibility improvements and challenges. NVDA includes solid support for Windows 10, including Microsoft Edge, the new Start menu, navigation in universal apps and so on, all made possible thanks to collaboration between users, Microsoft, NV Access and others, part of which involves the add-on we will meet in this article.

In NVDA Add-on Internals: Windows 10 App Essentials, we'll look at how this add-on came about, how it works, and go over recommendations from the add-on author (me) regarding accessibility practices. You'll also glimpse how UI Automation works at a high level, how features start out as an add-on component and end up as an NVDA feature and so on.

To download the add-on, visit https://addons.nvda-project.org/addons/wintenApps.en.html. The source code for this add-on can be found at https://github.com/josephsl/wintenApps. As Windows 10 and universal apps are UI Automation universes, it is essential that you know some things about UIA, which are covered later.

Disclaimer: Despite the article text and knowledge that's contained within, I (Joseph Lee, the add-on author) do not work for NV Access nor Microsoft.

Note: some of the features described may change as Windows 10 and NvDA development progresses. As of August 2020 revision, features from upcoming NVDA 2020.3 release and recent Windows Insider Preview builds are documented for reference purposes. Also, when refering to Windows 10 updates, release ID (YYMM) is used instead of using marketing label unless specified (for example, Version 1709 instead of Fall Creators Update, or 20H2 instead of 2009).

Copyright: Microsoft Windows, Windows 10, Windows API, UI Automation, Microsoft Edge, Universal Windows Platform (UWP) and related technologies are copyright Microsoft Corporation. NVDA is copyright NV Access. Windows 10 App Essentials add-on is copyright 2015-2020 Joseph Lee and contributors, released under GPL 2.

## Introducing Windows 10

Windows 10 is the "last major" version of Windows for the foreseeable future. It introduces a completely new way of keeping track of changes through Windows Insider Program and Windows as a Service (WaaS, a fancy term for continuous delivery), new application development framework, unification strategy in terms of user experience across devices and a new web browser. In addition, it features the return of an older style of Start menu, virtual desktops, Action Center to centralize notifications, a way to run command-line Linux utilities, and revamped Narrator that continues to receive refinements.

Windows 10 made its maiden flight in October 2014. Back then, it was called Windows Technical Preview, and after several weeks, it was renamed to Windows Insider Preview. Between October 2014 and July 2015 when Windows 10 Version 1507 (build 10240) shipped, more than five million users became Insiders, testing new builds and apps, submitting feedback and so on.

I call the October 2014 preview (build 9841) a maiden flight for several reasons. First, this is the first time where Microsoft did show interest in user-level feedback. Although betas existed for earlier versions such as Windows 7 and 8.1, Windows 10 is the first attempt from Microsoft at connecting with users and taking comments seriously. Second, build 9841 (the first Insider Preview build) hailed the start of Windows as a Service, a completely different approach to upgrading Windows where Microsoft wanted to provide two things: continuous delivery and feedback loop, and a unified configuration that works well with most devices. There were setbacks, such as privacy concerns due to telemetry, but for the most part, Windows 10 was received positively.

There is another, more personal reason for calling October 2014 release a maiden flight: I became one of the first Windows Insiders, and due to my work on NVDA, I have decided to make sure screen reader users were treated with respect. This included sending accessibility-related feedback, getting other screen reader users onboard as Insiders, and releasing NVDA try builds that resolved important issues for Windows Insiders. This culminated in the release of Windows 10 App Essentials add-on in November 2015 (in time for Windows 10 Version 1511/build 10586 release) that provided basic support for Insider Hub (now Feedback Hub) and other workarounds, which translated to superb user experience for NVDA users when it comes to using Windows 10 and various universal apps. My work on championing accessibility continues today, especially when it comes to making sure third-party universal apps are usable by many, supporting features such as Sets and so on.

## Purposes of Windows 10 App Essentials

Windows 10 App Essentials add-on is built on top of four pillars:

* New features support: part of making sure screen reader users were treated with respect was showcasing new Windows 10 features early through this NVDA add-on. These include support for really old versions of Feedback Hub app, emoji panel in Fall Creators Update and so on.
* Essential features and announcements: Until early 2017, NVDA did not announce important information such as status of Windows Update installations in Settings app. This has changed significantly in 2017 (see notes on live region change event for details).
* UI Automation and accessibility workarounds: every day, new features and bug fixes are added to various universal apps or Windows 10 itself. At the same time, there is at least one app where accessibility, particularly UI Automation, gets broken. Some of the add-on code is devoted to providing workarounds for odd UIA implementations.
* Demonstrating commitment to accessibility advocacy: some accessibility champions, including I, have recently stressed that accessibility is important in app designs, and that developers should take accessibility feedback seriously. Through workarounds and features, the add-on provides a way to demonstrate this commitment and advocacy.

There is a fifth pillar that has emerged in recent years: providing a testing ground for potential NVDA features dealing with Windows 10 and apps. Recently, parts of this add-on have made their way to NVDA screen reader, including emoji panel support, suggestion sounds, dialog detection and others.

## Add-on contents

The Windows 10 App Essentials add-on consists of a global plugin and app modules for various universal apps included with Windows 10. The Windows 10 Objects (shortened to WinTenObjs), the global plugin portion of this add-on, provides foundations such as overlay classes for frequently encountered controls in Windows 10 an universal apps, along with UIA event tracking and logger facility. Until 2018, the global plugin was also responsible for add-on update feature, documented here for sake of completeness.

In regards to app modules, these were included to either provide workarounds or enhance the user experience. For example, the app module for Settings app (systemsettings) allows NVDA to announce Windows Update download and installation progress, and app module for UWP frame host (shellexperiencehost) includes a workaround for menu expanded status problem in Start menu. We'll meet some of these app modules in subsequent sections.

### A note on feature parity with NVDA screen reader

As noted above, some features discussed in this article (such as suggestion sound playback and UIA notification event handler) were integrated into recent NVDA releases. I will point out some of these, as well as provide how these were integrated, including planning involved and some tips on modifying add-on features to fit into NVDA's code base.

### Information on add-on update feature

This article will sometimes reference add-on update feature, which is gone in 2019. Information about it is kept here for reference purposes. An add-on appropriately named "Add-on Updater" is used to update windows 10 App Essentials and other add-ons.

## Fun with UI Automation

Before we dive into how the add-on works, it is helpful to understand what UIA is and wy it is important. Only then the rest of the article makes sense, as Windows 10 and universal apps are UIA universes (exceptions exist, including desktop apps converted for distribution in Microsoft Store).

UI Automation (UIA), released in 2007, is an accessibility API based on Component Object Model (COM) that allows assistive technologies and other programs to communicate with each other regarding accessibility information about a control. In some respects, this API is a replacement for Microsoft Active Accessibility (MSAA), sometimes called IAccessible that was released in the 1990's. Being a COM-based API set, it allows programs and objects to expose essential information regardless of programming language in use as long as an object exposes documented routines that other programs can use.

In UIA world, an object on screen is termed an "element". Just like any accessibility API's, UIA exposes various elements to assistive technologies, which are termed "clients", with programs with the set elements termed "servers". These elements are organized into a UI tree, with the Windows Shell (desktop) object being the root, with tree being pruned and new leafs springing constantly whenever apps are started and closed, elements are created and destroyed, controls are shown and hidden on screen and so on.

Although UIA is meant to replace MSAA due to modernized accessibility information that can be gathered, screen reader vendors such as NV Access publishes workarounds for poor or odd UIA implementations. One such case is UIA issues in older versions of Microsoft Office, such as label problem in various combo boxes. Certain areas in Windows 10 and universal apps still have UIA issues, such as odd or badly applied control labels, generic XAML (eXtensible Application Markup Language)/UI labels, expected events not being fired and so on. This is one of the reasons for creating Windows 10 App Essentials add-on: to provide workarounds for issues like these.

### Automation ID and other interfaces and properties

A key piece of information UIA exposes (or attempts to gather) is automation ID, a string that uniquely identifies an element. For example, some search fields expose "SearchEditBox" as automation ID, which allows screen readers such as NVDA to detect these controls. Although most controls do expose unique automation ID's, some uses generic or auto-generated automation ID's (such as update history in Settings app).

Other useful information exposed by UIA elements are:

* Class name: the class name for this control, a string that denotes the class of this element (not to be confused with automation ID that uniquely identifies an element).
* Framework: the underlying framework used to create a given control such as XAML, Direct UI and others.
* Localized control type: a role type text that should be spoken by screen readers in different languages.
* Controller for: a list (array) of controls that this element manipulates when performing actions such as search suggestions (explained below).
* ARIA properties: a map of ARIA properties such as role description, mostly encountered in Microsoft Edge elements.

### UIA events

In addition to standard events expected from accessibility API's such as focus manipulation and object property (such as name and state) changes, UIA comes with some interesting events, including controller for, live region changed, notification and many others. Due to performance reasons, NVDA ignores certain events such as structure change and others. How NVDA and Windows 10 App Essentials deals with certain UIA events is covered later in this article.

### UIA-related additions, fixes and workarounds

The Windows 10 App Essentials add-on includes the following additions, fixes and workarounds for UIA issues and control problems:

* Search suggestions: NVDA now plays a sound to indicate appearance of search suggestions. More on this below.
* Live region change announcements in various apps. In the global plugin portion, a way to define and track this event is included.
* Floating suggestions such as Emoji panel in Version 1709 (Fall Creators Update) and hardware keyboard suggestions in Version 1803 (April 2018 Update). This has been incorporated into NVDA 2018.3 release, but more recent changes do require support from this add-on.
* Support for UIA notification event introduced in Version 1709. This became part of NVDA in 2018.2, and refined in 2019.2 to interupt users when important notifications are pending.
* Providing more meaningful labels for certain controls such as update history in Settings/Update and Security/Windows Update, sensitive to changes in Insider Preview builds.
* Announcing tooltips from universal apps, now part of NVDA 2019.3.
* Recognizing dialogs powered by XAML and various frameworks. Since NVDA 2018.3, NVDA itself takes care of this in most situations.

We'll meet various UIA controls and workarounds throughout this article.

## Windows 10 Objects

Windows 10 App Essentials add-on comes with Windows 10 Objects, a global plugin that contains definitions of common controls encountered in Windows 10 and various universal apps. These include search suggestion handling, tool tips for universal apps and so on. It also includes additional UIA handling routines and configuration and update facility for the add-on (the latter was removed in 2019).

### Source code layout

The global plugin consists of the following: 

* winTenObjs/__init__.py: the base global plugin.
* winTenObjs/_UIAHandlerEx.py: additional UIA routines for ones NVDA does not support natively (mostly for old NVDA releases). This module can come and go without notice.
* winTenObjs/w10config.py: configuration and updates. As of June 2017, the only thing configurable from Windows 10 App Essentials settings dialog is update facility, which includes whether update check should be performed automatically, update check interval and channel. This module is gone in 2019.

The main global plugin file is laid out thus:

1. Usual add-on header such as copyright information.
2. UIA constants not included in NVDA, including property ID's such as controller for event. Most are now part of NVDA itself.
3. Classes defining various Windows 10 and universal app controls, including search suggestions, looping selectors and so on.
4. The actual global plugin class, consisting of overlay class finder and tracking routines for various UIA events (only available if NVDA is restarted with debug logging enabled).

### Startup and shutdown

When the add-on loads, it performs up to four tasks:

1. Enables tracking of missing UIA events. For example, until May 2017, controller for event (an event fired by a control that depends on another control such as an edit field with search suggestions) wasn't available in NVDA screen reader, but search suggestion announcement was made possible as this add-on added this event.
2. Extends or replaces NVDA's UIA support subsystem if NVDA does not come with support for newer UIA interfaces. This is the case for notification event which NVDA did not support prior to 2018.2.
3. Adds user interface elements for this add-on, specifically add-on settings if appropriate.
4. Checks for add-on updates if told to do so.

The only thing done at shutdown is terminating the update check facility and removing user interface elements. This method, along with last two steps from the list above, no longer exists as of 2019.

### Notable Windows 10 objects and features

#### Sounds to indicate appearance of search suggestions

In some edit fields such as search box in Start menu, a list of suggestions will appear while entering text. for newer implementations, UIA controller for event is raised if this happens, with different screen readers reacting differently. For example, when typing something into Start search box while using Narrator, Narrator will play a sound to indicate appearance of suggestions, while old NVDA releases will announce top suggestion.

Because I felt it would be best to let users be notified when suggestions appear and disappear (and in some respects, follow Narrator's footsteps), I have implemented code to handle search suggestions. This is divided into four components:

* One or more classes used to identify edit fields that does raise UIA controller for event and ways to identify them. The reason for using several classes for the same object is due to compatibility reasons, as older NVDA releases does not come with a search field class. These classes include two events related to controller for event:
	* `event_suggestionsOpened`: called when suggestions appear. Some controls, notably embedded Cortana search box when opening a new Sets tab, does not fire this event properly.
	* `event_suggestionsClosed`: called when suggestions disappear. There are controls that does not raise this, including Edge's address omnibar.
* A class representing the suggestion items themselves.
* A set of sounds to indicate appearance/disappearance of suggestions.
* A compatibility layer for old and upcoming NVDA releases as noted above.

In addition, in some cases, it is helpful to announce how many suggestions have appeared, thus a routine has been added to announce this. With this added, the complete picture is as follows:

1. User types text into a search field.
2. NVDA will notice controller for event and will look for suggestions list. If such a list is found, NVDA will play the suggestion sound by raising suggestions opened event.
3. If suggestions are found, it'll announce the top suggestion or suggestion count. The former is for Start menu, while the latter is for other edit fields.
4. One can then use up or down arrow keys to move through suggestions, then press Enter to select or Escape to close suggestions list. When closing suggestions list, NVDA will play suggestions close sound.

Since NVDA 2017.3, suggestion announcement (not the count) is part of the screen reader.

Note that the routines described above was done at a time when it was desirable to detect all possible search fields. However, it was found that some workarounds were app specific, thus in June 2019, it was decided to transfer some search field handling to app modules. This is especially the case with address omnibar in legacy Microsoft Edge (EdgeHTML version) where the global plugin’s suggestions closed event handler did not apply if Edge is in use. Along the way, handling rarely used search fields that appeared in one or two apps (such as People app search field in old app releases) were dropped.

#### Announcing notifications

Windows 10 Version 1709 (Fall Creators Update) introduces a new event to let apps send text to be announced by UIA clients such as NVDA. One of the jobs of Windows 10 Objects is to catch this and announce notifications for NVDA releases which does not support this natively.

Because old NVDA releases do not support the new notification event natively, a trick is included with the add-on to allow NVDA to detect and handle notifications. This is done by extending UIA support subsystem through an internal module that takes over the NVDA's own routines. Among other things, this extended subsystem includes definitions for UIA notification event handler, and this subsystem takes over if NVDA 2018.1.x is running on Windows 10 Version 1709 and later.

The notification event handler takes five keyword arguments:

* Sender: the UIA element that raised the event.
* Notification kind: the kind of notification.
* Notification processing: how NVDA should process incoming notification.
* Display string: notification text.
* Activity ID: the unique identifier for the notification.

As of October 2018, NVDA itself announces notifications for all apps (especially for the currently active app) except one or two apps where this would cause issues, thus the add-on is no longer involved in announcing many notifications except those that could cause issues.

#### Tracking UIA events for controls

The Windows 10 Objects global plugin also has ability to track UIA events for controls and log info  about them, executed via `uiaDebugLogging` function that takes an object and the event name. This function records the following if NVDA is started with debug logging enabled or told to monitor specific events and/or events from specific apps:

* What the object actually is.
* Object name.
* Name of the event being logged.
* App where the control can be found (specifically, the app module).
* Automation ID.
* UIA class name.
* For controller for event, the list of objects the given control depends on.
* For tooltip open event, the GUI framework that powers the element.
* For item status event, new item status text.

For notification events, NVDA records event parameters from the event handler method itself.

#### Looping selectors

A looping selector is a combo box-like control where the selection loops around. This is employed in places such as Alarms and Clock, Settings/Update and Security/Windows Update/active hours and so on.

In older Windows 10 and universal app releases, when changing selector values, item selected UIA event wasn't fired. To get around this, the add-on will examine states for each item and announce if an item has selected state. This isn't the case for newer implementations, but for backward compatibility, the old routines are kept. This has been enhanced in NVDA 2019.1, and since June 2019, the add-on is no longer involved in keeping an eye on this control as NVDA supports it natively.

#### Live region change events

Some controls are live regions - that is, a control whose content denotes live text, such as progress of something, alerts and so on. Because of odd live region change event implementations, older NVDA releases does not support this event natively, but NVDA 2017.3 and later includes a trivial implementation where NVDA will announce the live region text i.e. object name.

The Windows 10 Objects goes one step further by recording instances of this event and providing workarounds for specific cases. These include announcing correct text for Edge alerts (see below), preventing repeat announcements in some apps and so on.

#### Recognizing various dialogs

Despite not being identified as such, some windows are actually dialogs. These include pop-up dialog for uninstaling apps, various dialogs found in Settings app and so on.

In old add-on releases, NVDA would consult a list of known dialog class names in hopes of catching a dialog. In newer releases, especially if run on Windows 10 Version 1809 and later, UIA IsDialog property is used to catch dialog elements. Once dialogs are recognized, NVDA will read contents of these dialogs automatically when they appear. This has been simplified in NVDA 2018.3 as NVDA itself will try its best to recognize more dialogs, including those marked as a dialog via UIA in Version 1809. However, there are windows that are actually dialogs, so the add-on still ships with a list of known dialog classes to be consulted by NVDA.

## App modules for universal apps

In addition to Windows 10 Objects global plugin, the add-on comes with app modules designed to provide extra support for various universal apps that comes with Windows 10. These modules include enhancers and/or fixers, broadly divided into five categories:

1. Adding extra features.
2. Supporting new technologies.
3. Announcing (or, more recently, suppressing extraneous announcement of) information in various situations.
4. Workarounds for UIA issues.
5. Respond to changes in apps, and in at least three occasions, adding aliases due to renamed executable names.

The modules and enhancers/fixers applied are:

* Calculator: selectively announce calculator display.
* Calendar: suppress read-only state announcement in various controls.
* Cortana/Start menu/Windows Search (classic Cortana): suppress double announcement of suggestion result item in some cases, staying silent when user is dictating to Cortana, handling bad UIA implementations.
* Cortana/conversations (new Cortana): announcing Cortana's responses.
* Mail: table navigation commands in message list, suppress read-only announcement in email content, app alias for hxmail.exe and hxoutlook.exe (the latter for updates released in May 2017).
* Maps: play location coordinates for map items, suppress repeated live region announcements, aliases to support old and new Maps releases (the old alias, maps_windows, is gone).
* Microsoft Edge (classic EdgeHTML version): announce correct alert text and enhancements for address omnibar, supports both the overall Microsoft Edge process and the content process (microsoftedgecp.exe).
* Microsoft Store: announce needed information when live region changed event is fired by some controls, aliases to support old and new Store versions (the old alias, winstore_mobile, is no more).
* Modern keyboard/text input host: support for emoji panel, dictation, hardware input suggestions, and pasting clipboard items (Version 1809), part of NVDA since 2018.3.
* MSN Weather: use up or down arrow keys to read forecast information.
* Open With: announce open with dialog content in recent Windows 10 releases.
* People: announcing first suggestion when looking for a contact.
* Settings: selectively announce various status information, provide correct labels for certain controls.
* Shell Experience Host: work around some UIA state information mismatch and announce item status in Action Center. Action Center support, including reclassifying brightness button as a proper button is now part of NVDA 2019.1.

### Adding useful features in apps

The following app modules add functionality unique to NVDA and/or commands that are used to improve user experience when using apps:

* Maps (maps.py): when using object navigation to examine a map, a tone will be played to indicate where things are located on the map. This is achieved by defining a custom handler for `event_becomeNavigatorObject` that'll take the coordinates of the object (in pixels) and play a tone, essentially emulating mouse coordinate beeps in NVDA. The app module also allows users to hear new locations when using street view to navigate the map, and this is done through handlers for live region changed event.
* Mail (hxoutlook.py): when focused on messages list, one can use table navigation commands (Control+Alt+arrow keys) to review message headers. This is possible thanks to two things: headers are child objects of the message item, and because of this, `NVDAObjects.behaviors.RowWithFakeNavigation` class can be employed to add this functionality.
* MSN Weather (microsoft_msn_weather.py): this app module, contributed by Derek Riemer, allows users to use up and down arrow keys to read forecast information, achieved by calling corresponding review cursor movement commands to move by line.

#### A note about modern keyboard

Modern keyboard, sometimes called Composable Shell (windowsinternal_composableshell_experiences_textinput_inputapp.py) and nowadays called Text Input Host, is the name of the app that provides various features, including emoji panel, dictation, hardware input suggestions, listing items to be pasted from cloud clipboard and many other input related features. This is not exactly an app, but more towards a floating overlay, much akin to touch keyboard on touchscreen devices. Powering these is a redesigned touch keyboard where XAML-based touch panel (with its own process) is used.

In Windows 10 Insider Preview build 16215 and later, it is possible for users to browse and select emojis to insert in an edit field. This is done by pressing Windows+period (.) or Windows+semicolon (;). A floating panel of emoji categories and emojis will appear. One can then use arrow keys to move through emojis or Tab and Shift+Tab to cycle through categories. In build 16226, one can type emoji descriptions to narrow the emoji field.

In build 17666 and later, this panel has been redesigned. Instead of using Tab key to move between categories, one would press Tab to move between emoji grid and categories. In case of People category, pressing Tab will let you move to skin tones list where you can use arrow keys to select a skin tone, then press Tab to move to emoji grid.

Build 18305 and later brought another design change to this panel. In addition to selecting emojis, it also hosts two new grand categories named kaomoji ("face characters" in Japanese) and symbols. When one presses Tab, one will eventually reach category list with three items: emoji, kaomoji, and symbols. Just like selecting emoji categories, pressing Enter will switch the panel among these modes.

Build 18963 renamed Modern Keyboard to Text Input Host, along with bringing refined version of Input Method Editor (IME) for certain languages. For languages such as Japanese, the modern IME hosted by Text Input Host is used.

When this panel opens, a menu open event is fired by the emoji panel (File Explorer in build 18305 and later), an event NVDA does not detect for performance reasons. As items are selected, an item selected event is fired, to which NVDA responds by walking the panel in a tree-like fashion in order to locate the item selected. The actual announcement of emoji characters depends on synthesizers; currently, recent SAPI5 and OneCore (aka SAPI Mobile) voices and Espeak nG ships with definitions of emoji characters, expanded to cover other synthesizers in NVDA 2018.4

Similar to emoji panel (or expanded input panel in build 18305 and later), in build 17025 and later, modern keyboard can also provide input suggestions. This is done by checking a new option in Settings/Devices/Typing, and activated when one presses up arrow while typing (only United States English keyboard layout is supported). Just like emoji panel, a floating window appears, and in this case, one can press left or right arrow to navigate between suggestions and press Enter to accept the offered item.

The above mechanism for selecting input suggestions is also employed when pasting items from cloud clipboard. In build 17666 and later, one can copy text and small images to the clipboard to be pasted later, and Windows will keep a history of items copied to the clipboard. When Windows+V is pressed, a list of clipboard items will be displayed, and one can use left or right arrows to select the desired item.

In NVDA 2018.3, support for all of these (modern keyboard features) plus dictation window (also part of modern keyboard) have become part of NVDA. The add-on is still required in order to support more recent panel redesigns (see above).

### What to announce, what not to announce

It is sometimes helpful to let users know what's going on by announcing various status information, while at other times it is equally important to not announce extraneous messages. The former was the case for majority of app modules below in the past, but since mid-2017, reverse is happening more frequently.

The app modules (and for one in particular, more than an app module) in question are:

* Calculator (calculator.py): while entering calculations, entered expression will be announced via name change handler. Because this may interfere with typed character announcement in NVDA, the calculator display will be announced only when actual results appear or when the display is cleared.
* People (peopleapp.py): NVDA will announce first suggestion when looking for a contact. Unlike other search fields, there is no controller for event. However, the suggestion raises item selected event.
* Cortana (searchui.py)/new Start menu and Windows Search experience (searchapp.py): classic Cortana uses name change events and specific automation ID's to convey text messages. Name change event is also employed when Cortana tries to understand the text a user is dictating, which in old releases of the add-on meant NVDA would announce gibberish, subsequently resolved in later add-on releases. In recent Windows 10 releases, due to Windows Search redesign (which also involve changing executable for Windows Search to searchapp), search box content instead of result details is announced, or if results are announced, they are announced twice.
* Cortana conversations (cortana.py): similar to classic Cortana, Cortana's responses are announced.
* Open With (openwith.py): announces open with dialog content, used to select an app when opening unknown file types.
* Settings (systemsettings.py): NVDA will announce messages such as Windows Update notifications, and this is done through live region changed event (name change event in older add-on releases).
* Shell Experience Host (shellexperiencehost.py): in Action Center, toggling some quick actions causes item status change event to be logged. NVDA will announce the new status if appropriate.
* Microsoft Store (winstore_app.py): just like Settings app, status messages are announced, this time dealing with product downloads such as apps and multimedia content.

### Hunting for UIA implementation issues

As noted above, some controls ship with odd or bad UIA implementations, and universal apps are no exception (at least for app modules that ships with the add-on). Because of this, the following app modules (and in case of two, taken care of by Windows 10 Objects global plugin itself) include workarounds for various UIA problems:

* Calendar (hxcalendarappimm.py) and Mail (hxoutlook.py): some edit fields, such as appointment title and others are shown as read-only when they are not, and removing this state from states set for these controls resolved this problem.
* Cortana: some search suggestions expose same text for name and description, which results in repeats for suggestion result text. This was corrected by comparing name and description and nullifying the description (obj.description = None). This workaround is no longer applicable due to Windows Search redesign in Version 1903. Also, when opening Sets version of Cortana search box (builds 17666 and 17692), wrong controller for event is fired, which prevents NvDA from announcing suggestions, and this has been corrected.
* Maps: despite no changes to the app, live region changed event is fired by map title control, so NvDA includes a way to suppress repetitions.
* Microsoft Edge (microsoftedge.py and microsoftedgecp.py, legacy version): for some alerts, the name of the control that fires live region changed and system alert events have the name of "alert", with the actual text as the last child or text is scattered across child elements, thus NVDA will look for actual alert text when announcing alerts.
* Settings and Store: for some controls (such as when downloading content from Store), a specific status control fires live region changed event. Unfortunately, the text for them are generic (for example, "downloading some percent" as opposed to announcing the product one is downloading), thus NVDA will locate information such as product names when this happens to make this easier to follow. Also, in Settings app, some controls in older versions of this app have no label, thus NVDA is told to look for labels to traversing sibling (next/previous) objects, and in case of certain Windows 10 Version 1809 installations, the correct label is the name of the first child.
* Shell Experience Host: for some submenus, NVDA does not know that it is a submenu, thus worked around by teaching NVDA to recognize the proper role and state for these. This procedure was limited to this app in 2018, but was expanded to cover submenus in Edge app menu in August 2018.

### A tale on app module and executable names

One of the side-effects of continuous delivery is appearance of unanticipated changes. This is more so when a workaround for an app broke simply because the name of the executable or the app has changed. In addition, some apps shipped with an executable whose name broke Python's module name and import routines.

The specific issues encountered were:

* Mail, Maps, Modern Keyboard, Start menu and Store: executable names have changed throughout Windows 10 development. For example, in May 2017, workarounds in place for Mail app broke when Microsoft renamed hxmail to hxoutlook, and in July 2019, Modern Keyboard was renamed to textinputhost. Microsoft Edge is a special case of this because it requires use of two app modules: microsoftedge.exe for web browser management, and microsoftedgecp.exe (content process) for displaying content in a more secure way. Due to this, aliasing (a new app module importing everything from an old version) is common.
* MSN Weather, Store, modern keyboard and others: some executable names have a dot (.) in the middle, which breaks app module import routines. This is countered by replacing dots with underscores (_). For example, for Skype, the actual executable name is skype.app.exe, while the app module for this app is named skype_app.py. This fix is now part of recent NVDA releases.

## Few remarks

### UIA performance

Numerous issues were filed on NVDA's GitHub page regarding UIA performnace issues. These include issues in early days of Edge support where navigating the document was slow (resolved in NVDA 2017.2), list view issues in File Explorer while using a program with high CPU usage (GoldWave, for example, resolved in NVDA 2018.4) and so on. While some are specific to NVDA, others are reproducible while using Narrator, hence NV Access and Microsoft are actively collaborating on identifying and writing fixes for performance and control implementation problems (such as some of the ones listed above).

### Narrator is the new reference in screen reading in Windows 10 and universal apps

Until a few years ago, any screen reader wishing to support an app or add features would look up to JAWS for Windows for guidance. This is no longer the case with Windows 10 and universal apps, as Narrator provides a useful yardstick (at least a base implementation other screen reader vendors should respond to) when it comes to reading text on screen, feature set for supporting universal apps, and investigate UIA issues. Some of the features discussed above, such as search suggestion notification, were inspired by Narrator's handling of various UIA events, and because Narrator reads what is told to read, NVDA ships with workarounds for odd UIA implementations to get around some poblems.

### Integrating features from this add-on to NVDA screen reader

As noted above, some add-on features are being (or have been) integrated into NVDA. These include search suggestion notification, modern keyboard support, live region changed event tracking and announcement and so on.

Typically, when a feature from an add-on is integrated into NVDA, it goes through a typical issue-review-test-documentation cycle. To illustrate this, let us go through steps involved in getting search suggestions into NVDA:

1. Issue: an issue regarding search suggestions was filed in 2016.
2. Review: I and NV Access went through a review phase where implementation detail were discussed and test cases written.
3. Test: in 2017, search suggestion feature made its debut in an NVDA next snapshod. This resulted in feedback from users regarding braille support, sounds and others. After several weeks, this feature was made available to master snapshot users, thus ready for NVDA 2017.3.
4. Documentation: the search suggestion feature was documented in the user guide. Discussion of this feature in this article is a special case of documentation step.

Due to changes to release process in 2018, testing occurs via pull requests.

In addition, when a feature from an add-on is under consideration for inclusion in NVDA, I modify the add-on source code to make it compliant with NVDA source code guidelines, such as commenting style, copyright header and so on.

### Giving feedback to app developers

Feedback drives Windows 10 and universal apps. one of the reasons for instituting Windows Insider Program, as noted by Microsoft and others, is to gather feedback from millions of users in hopes of making Windows 10 better in the long run. As such, sending feedback regarding Windows 10 and preinstalled universal apps, as well as third-party apps is crucial at the age of feedback-driven development.

Here are some tips regarding sending feedback to app writers:

1. Embrace: have willingness to embrace (use and test) the app in question.
2. Document: if something happens, document what happened, steps to reproduce, and possible workarounds.
3. Send: send feedback to developers (Feedback Hub, contacting developers of third-party universal apps, screen reader vendors and so on).
4. Follow-up: follow-up with developers if they have questions for you or you want to know what's going on with your feedback.

### Accessibility best practices for universal apps

As a Windows Insider, a screen reader contributor and the author of a screen reader add-on for Windows 10 and universal apps, I came across numerous examples where apps were inaccessible at first, or usability was overshadowed by issues when working with controls, navigation and so on.

Here are some tips in hopes of making universal apps truly universally accessible and usable:

* Listen to feedback, especially feedback coming from users with disabilities such as screen reader users.
* Do not put accessibility as an afterthought, nor something you want to work in the future (say, version 3). Proactive accessibility and investigations into issues is something app developers should learn as they develop apps.
* Test with screen readers and other assistive technologies: one way to validate accessibility issues raised by users with disabilities is using assistive technologies in real life. Use facilities offered by screen readers such as Python console in NVDA, developer mode in Narator and so on in hopes of locating where the root of the issue lies.
* Try using keyboards and other input methods offered by various assistive technologies: touchscreen isn't the only input method used in universal apps. Many screen reader users use a keyboard to interact with apps, and some use touchscreen gestures offered by screen readers to navigate an app and respond to changes. Try using them to make sure app features are working as advertised when using keyboards and other input methods.
* Use useful labels: in case the control has no label as reported by screen readers, be sure to provide labels. A good historical case is Windows Defender Security Center where there was no label for various buttons in 2016, which was fixed in 2017 with Creators Update. Also, avoid generic XAML labels such as someclass.someotherclass.such (especialy lists and list items), as it does not provide an accurate picture as to where one is located. A classic case is Feedback Hub app where generic labels for lists were presnet in older versions, subsequently fixed in recent updates.
* Raise appropriate UIA events: screen readers listen to UIA events to detect what's happening with apps. For example, if there's a need to anounce suggestions, controller for event should be fired. An example is Store where old releases did not raise controller for event when content suggestions appeared, with recent versions raising this event.

## Conclusion

With the introduction of Windows 10 and Universal Windows Platform, a new way of connecting users and developers has emerged: feedback-driven development. This allows users to send feedback regarding features and bugs, including that of accessibility feedback. Although accessibility of Windows 10 and universal apps were spotty at first, this situation is improving, driven by Microsoft's commitment to accessibility, continued feedback, and collaboration between Microsoft and assistive technology vendors.

In terms of NVDA, what made Windows 10 usability possible was not only changes made from within Windows and universal apps, but also proactive investigations into making sure NVDA users have a great time with Windows 10. Windows 10 App Essentials add-on is part of that work, as discussed throughout this article when talking about UIA workarounds, improving support for apps and controls and others. But there are limits as to what the add-on can do, as the other puzzle pieces are willingness from developers (especially third-party UWP developers) to embrace accessibility as a pillar in their apps, and willingness from users to send accessibility feedback. Although some add-on features are being integrated into NVDA, there are some areas where the add-on is needed (especially when supporting features introduced in Windows Insider Preview builds), and until the day accessibility is everywhere in Windows 10 ecosystem and universal apps, the add-on will still be here.

## References

* Windows 10 (Wikipedia): https://en.wikipedia.org/wiki/Windows_10
* Windows Insider Program (Microsoft): https://insider.windows.com/
* Windows as a Service Overview (Microsoft Docs): https://docs.microsoft.com/en-us/windows/deployment/update/waas-overview
* What's a Universal Windows Platform (UWP) App (Microsoft UWP App Developer): https://docs.microsoft.com/en-us/windows/uwp/get-started/whats-a-uwp
* UI Automation Overview (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee684076(v=vs.85).aspx
* MSAA overview (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/dd373592(v=vs.85).aspx
* UI Automation and Active Accessibility (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee671585(v=vs.85).aspx
* Component Object Model Overview (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ms680573(v=vs.85).aspx
* IUIAutomationElement interface (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee671425(v=vs.85).aspx
* cachedAutomationId (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee671434(v=vs.85).aspx
* UI Automation Properties Overview (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee671594(v=vs.85).aspx
* UI Automation Events Overview (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee671221(v=vs.85).aspx
* UI Automation Event Identifiers (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee671223(v=vs.85).aspx
* Auto-suggest accessibility, part of Accessible Text Requirements (Microsoft Docs): https://docs.microsoft.com/en-us/windows/uwp/accessibility/accessible-text-requirements
* IUIAutomationNotificationEventHandler::HandleNotificationEvent (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/mt814955(v=vs.85).aspx
