# -*- coding: utf-8 -*-
documentation = [
_(u"""# NVDA 2018.1 Developer Guide"""),
"",_(u"""## Table of Contents"""),
"",_(u"""  * 1\\. Introduction"""),
_(u"""    * 1.1. A Note About Python"""),
_(u"""  * 2\\. Translation"""),
_(u"""    * 2.1. Character Descriptions"""),
_(u"""    * 2.2. Symbol Pronunciation"""),
_(u"""      * 2.2.1. Defining Complex Symbols"""),
_(u"""      * 2.2.2. Defining Symbol Information"""),
_(u"""  * 3\\. Plugins"""),
_(u"""    * 3.1. Overview"""),
_(u"""    * 3.2. Types of Plugins"""),
_(u"""    * 3.3. Basics of an App Module"""),
_(u"""    * 3.4. Example 1: An App Module that Beeps on Focus Change Events"""),
_(u"""    * 3.5. Basics of a Global Plugin"""),
_(u"""    * 3.6. Example 2: a Global Plugin Providing a Script to Announce the NVDA Version"""),
_(u"""    * 3.7. NVDA Objects"""),
_(u"""    * 3.8. Scripts and Gesture Bindings"""),
_(u"""    * 3.9. Example 3: A Global Plugin to Find out Window Class and Control ID"""),
_(u"""    * 3.10. Events"""),
_(u"""    * 3.11. the App Module SleepMode variable"""),
_(u"""    * 3.12. Example 4: A Sleep Mode App Module"""),
_(u"""    * 3.13. Providing Custom NVDA Object Classes"""),
_(u"""    * 3.14. Example 5: Command to Retrieve the Length of Text in an Edit Field Using a Custom NVDA Object"""),
_(u"""    * 3.15. Making Small Changes to an NVDA Object in App Modules"""),
_(u"""    * 3.16. Example 6: Labelling the Notepad Edit Field Using event\\_NVDAObject\\_init"""),
_(u"""  * 4\\. Packaging Code as NVDA Add-ons"""),
_(u"""    * 4.1. Non-ASCII File Names in Zip Archives"""),
_(u"""    * 4.2. Manifest Files"""),
_(u"""      * 4.2.1. Available Fields"""),
_(u"""      * 4.2.2. An Example Manifest File"""),
_(u"""    * 4.3. Plugins and Drivers"""),
_(u"""    * 4.4. Optional install / Uninstall code"""),
_(u"""      * 4.4.1. the onInstall function"""),
_(u"""      * 4.4.2. The onUninstall Function"""),
_(u"""    * 4.5. Localizing Add-ons"""),
_(u"""      * 4.5.1. Locale-specific Manifest Files"""),
_(u"""      * 4.5.2. Locale-specific Messages"""),
_(u"""    * 4.6. Add-on Documentation"""),
_(u"""  * 5\\. NVDA Python Console"""),
_(u"""    * 5.1. Usage"""),
_(u"""    * 5.2. Namespace"""),
_(u"""      * 5.2.1. Automatic Imports"""),
_(u"""      * 5.2.2. Snapshot Variables"""),
_(u"""  * 6\\. Remote Python Console"""),
_(u"""    * 6.1. Usage """),
"","",_(u"""## 1\\. Introduction"""),
"",_(u"""This guide provides information concerning NVDA development, including translation and the development of components for NVDA. """),
"",_(u"""### 1.1. A Note About Python"""),
"",_(u"""NVDA and its components are primarily written in the Python programming language. It is not the goal of this guide to teach you Python, though examples are provided through out this guide which will help to familiarise you with the Python syntax. Documentation and other resources related to the Python language can be found at [www.python.org/](http://www.python.org/)"""),
"",_(u"""## 2\\. Translation"""),
"",_(u"""In order to support multiple languages/locales, NVDA must be translated and data specific to the locale must be provided. This section only includes information on custom NVDA file formats required for translation. Other items need to be translated, such as the NVDA user interface and documentation, but these use standard file formats. For complete documentation about translating NVDA, please see <https://github.com/nvaccess/nvda/wiki/Translating>"""),
"",_(u"""### 2.1. Character Descriptions"""),
"",_(u"""Sometimes, it can be very difficult or even impossible to distinguish one character from another. For example, two characters might be pronounced the same way, even though they are actually different characters. To help users when this occurs, character descriptions can be provided which describe the character in a unique way. """),
"",_(u"""Character descriptions can be provided for a locale in a file named characterDescriptions.dic in the directory for the locale. This is a UTF-8 encoded text file. Blank lines and lines beginning with a \"\\#\" character are ignored. All other lines should contain a character, followed by a tab, then one or more descriptions separated by tabs. """),
"",_(u"""For example: """),
_(u"""    """),
_(u"""    """),
_(u"""    # This is a comment."""),
_(u"""    a	alpha"""),
_(u"""    b	bravo"""),
_(u"""    """),
"",_(u"""See the file locale\\en\\characterDescriptions.dic for a full example. """),
"",_(u"""In most cases, the characters in this file should be a single lower case character. It is assumed that characters will have the same description regardless of their case, so upper case characters are converted to lower case before looking up their character descriptions. """),
"",_(u"""### 2.2. Symbol Pronunciation"""),
"",_(u"""It is often useful to hear punctuation and other symbols pronounced as words when reading text, particularly when moving by character. Unfortunately, the pronunciation of symbols is inconsistent between speech synthesisers and many synthesisers do not speak many symbols and/or do not allow control over what symbols are spoken. Therefore, NVDA allows information about symbol pronunciation to be provided. """),
"",_(u"""This is done for a locale by providing a file named symbols.dic in the directory for the locale. This is a UTF-8 encoded text file. Blank lines and lines beginning with a \"\\#\" character are ignored. All locales implicitly inherit the symbol information for English, though any of this information can be overridden. """),
"",_(u"""The file contains two sections. """),
"",_(u"""#### 2.2.1. Defining Complex Symbols"""),
"",_(u"""The first section is optional and defines regular expression patterns for complex symbols. Complex symbols are symbols which aren't simply a character or sequence of characters, but instead require a more complicated match. An example is the full stop \\(.\\) sentence ending in English. The \".\" is used for multiple purposes, so a more complicated check is required to determine whether this refers to the end of a sentence. """),
"",_(u"""The complex symbols section begins with the line: """),
_(u"""    """),
_(u"""    """),
_(u"""    complexSymbols:"""),
_(u"""    """),
"",_(u"""Subsequent lines contain a textual identifier used to identify the symbol, a tab and the regular expression pattern for that symbol. For example: """),
_(u"""    """),
_(u"""    """),
_(u"""    . sentence ending	(?<=[^\\s.])\\.(?=[\\\"')\\s]|$)"""),
_(u"""    """),
"",_(u"""Again, the English symbols are inherited by all other locales, so you need not include any complex symbols already defined for English. """),
"",_(u"""#### 2.2.2. Defining Symbol Information"""),
"",_(u"""The second section provides information about when and how to pronounce all symbols. It begins with the line: """),
_(u"""    """),
_(u"""    """),
_(u"""    symbols:"""),
_(u"""    """),
"",_(u"""Subsequent lines should contain several fields separated by tabs. The only mandatory fields are the identifier and replacement. The default will be used for omitted fields. The fields are as follows: """),
"",_(u"""  * identifier: The identifier of the symbol. In most cases, this is just the character or characters of the symbol. However, it can also be the identifier of a complex symbol. Certain characters cannot be typed into the file, so the following special sequences can be used: """),
_(u"""    * \\0: null """),
_(u"""    * \\t: tab """),
_(u"""    * \\n: line feed """),
_(u"""    * \\r: carriage return """),
_(u"""    * \\f: form feed """),
_(u"""    * \\\\\\#: \\# character \\(needed because \\# at the start of a line denotes a comment\\) """),
_(u"""  * replacement: The text which should be spoken for the symbol. """),
_(u"""  * level: The symbol level at which the symbol should be spoken. The symbol level is configured by the user and specifies the amount of symbols that should be spoken. This field should contain one of the levels \"none\", \"some\", \"most\", \"all\" or \"char\", or \"-\" to use the default. \"char\" means that the symbol should only be pronounced when moving by character. The default is to inherit the value or \"all\" if there is nothing to inherit. """),
_(u"""  * preserve: Whether the symbol itself should be preserved to facilitate correct pronunciation by the synthesiser. For example, symbols which cause pauses or inflection \\(such as the comma in English\\) should be preserved. This field should be one of the following: """),
_(u"""    * never: Never preserve the symbol. """),
_(u"""    * always: Always preserve the symbol. """),
_(u"""    * norep: Only preserve the symbol if it is not being replaced; i.e. the user has set symbol level lower than the level of this symbol. """),
_(u"""    * -: Use the default.  The default is to inherit the value or \"never\" if there is nothing to inherit. """),
"","",_(u"""Finally, a display name for the symbol can be provided in a comment after a tab at the end of the line. This will be shown to users when editing the symbol information and is especially useful for translators to define translated names for English complex symbols. """),
"",_(u"""Here are some examples: """),
_(u"""    """),
_(u"""    """),
_(u"""    (	left paren	most"""),
_(u"""    """),
"",_(u"""This means that the \"\\(\" character should be spoken as \"left paren\" only when the symbol level is set to most or higher; i.e. most or all. """),
_(u"""    """),
_(u"""    """),
_(u"""    ,	comma	all	always"""),
_(u"""    """),
"",_(u"""This means that the \",\" character should be spoken as \"comma\" when the symbol level is set to all and that the character itself should always be preserved so that the synthesiser will pause appropriately. """),
_(u"""    """),
_(u"""    """),
_(u"""    . sentence ending	point	# . fin de phrase"""),
_(u"""    """),
"",_(u"""This line appears in the French symbols.dic file. It means that the \". sentence ending\" complex symbol should be spoken as \"point\". Level and preserve are not specified, so they will be taken from English. A display name is provided so that French users will know what the symbol represents. """),
"",_(u"""Please see the file locale\\en\\symbols.dic for the English definitions which are inherited for all locales. This is also a good full example. """),
"",_(u"""## 3\\. Plugins"""),
"",_(u"""### 3.1. Overview"""),
"",_(u"""Plugins allow you to customize the way NVDA behaves overall or within a particular application. They are able to: """),
"",_(u"""  * Respond to particular events such as focus and object property changes; e.g. when a control changes its name. """),
_(u"""  * Implement commands which are bound to particular key presses or other input. """),
_(u"""  * Customise the behaviour of and implement additional functionality for particular controls. """),
_(u"""  * Customise or add new support for text content and complex documents. """),
"","",_(u"""This section provides an introduction to developing plugins. Developers should consult the code documentation for a complete reference. """),
"",_(u"""### 3.2. Types of Plugins"""),
"",_(u"""There are two types of plugins. These are: """),
"",_(u"""  * App Modules: code specific to a particular application. The App Module receives all events for a particular application, even if that application is not currently active. When the application is active, any commands that the App Module has bound to key presses or other input can be executed by the user. """),
_(u"""  * Global Plugins: code global to NVDA; i.e. it is used in all applications. Global Plugins Receive all events for all controls in the Operating System. Any commands bound by a Global Plugin can be executed by the user wherever they are in the operating system, regardless of application. """),
"","",_(u"""If you wish to improve NVDA's access to a particular application, it is most likely you will want to write an App Module. In contrast, if you wish to add some overall functionality to NVDA \\(e.g. a script that announces current Wireless network strength while in any application\\), then a Global Plugin is what you want. """),
"",_(u"""Both App Modules and Global Plugins share a common look and feel. They are both Python source files \\(with a .py extension\\), they both define a special class containing all events, scripts and bindings, and they both may define custom classes to access controls, text content and complex documents. However, they do differ in some ways. """),
"",_(u"""The following few sections will talk separately about App Modules and Global Plugins. After this point, discussion is again more general. """),
"",_(u"""### 3.3. Basics of an App Module"""),
"",_(u"""App Module files have a .py extension, and are named the same as the main executable of the application for which you wish them to be used. For example, an App Module for notepad would be called notepad.py, as notepad's main executable is called notepad.exe. """),
"",_(u"""App Module files must be placed in the appModules subdirectory of the user's NVDA user configuration directory. For more information on where to find the user configuration directory, please see the NVDA user guide. """),
"",_(u"""App Modules must define a class called AppModule, which inherits from appModuleHandler.AppModule. This class can then define event and script methods, gesture bindings and other code. This will all be covered in depth later. """),
"",_(u"""NVDA loads an App Module for an application as soon as it notices the application is running. The App Module is unloaded once the application is closed or when NVDA is exiting. """),
"",_(u"""### 3.4. Example 1: An App Module that Beeps on Focus Change Events"""),
"",_(u"""The following example App Module makes NVDA beep each time the focus changes within the notepad application. This example shows you the basic layout of an App Module. """),
"",_(u"""Copy and paste the code between \\(but not including\\) the start and end markers into a new text file called notepad.py, which should be saved in the AppModules subdirectory. Be very careful to keep all tabs and spaces intact. """),
"",_(u"""Once saved in the correct location, either restart NVDA or choose Reload Plugins found under Tools in the NVDA menu. """),
"",_(u"""Finally, open Notepad and move the focus around the application; e.g. move along the menu bar, open some dialog boxes, etc. You should hear beeps each time the focus changes. Note though that if you move outside of Notepad - for instance, to Windows Explorer - you do not hear beeps. """),
_(u"""    """),
_(u"""    """),
_(u"""    --- start ---"""),
_(u"""    # Notepad App Module for NVDA"""),
_(u"""    # Developer guide example 1"""),
_(u"""    """),
_(u"""    import appModuleHandler"""),
_(u"""    """),
_(u"""    class AppModule(appModuleHandler.AppModule):"""),
_(u"""    """),
_(u"""    	def event_gainFocus(self, obj, nextHandler):"""),
_(u"""    		import tones"""),
_(u"""    		tones.beep(550, 50)"""),
_(u"""    		nextHandler()"""),
_(u"""    """),
_(u"""    --- end ---"""),
_(u"""    """),
"",_(u"""This App Module file starts with two comment lines, which describe what the file is for. """),
"",_(u"""It then imports the appModuleHandler module, so that the App Module then has access to the base AppModule class. """),
"",_(u"""Next, it defines a class called AppModule, which is inherited from appModuleHandler.AppModule. """),
"",_(u"""Inside this class, it defines 1 or more events, scripts or gesture bindings. In this example, it defines one event method for gainFocus events \\(event\\_gainFocus\\), which plays a short beep each time it is executed. The implementation of this event is not important for the purposes of this example. The most important part is the class itself. Events will be covered in greater detail later. """),
"",_(u"""As with other examples in this guide, remember to delete the created app module when you are finished testing and then restart NVDA or reload plugins, so that original functionality is restored. """),
"",_(u"""### 3.5. Basics of a Global Plugin"""),
"",_(u"""Global Plugin files have a .py extension, and should have a short unique name which identifies what they do. """),
"",_(u"""Global Plugin files must be placed in the globalPlugins subdirectory of the user's NVDA user configuration directory. For more information on where to find the user configuration directory, please see the NVDA user guide. """),
"",_(u"""Global Plugins must define a class called GlobalPlugin, which inherits from globalPluginHandler.GlobalPlugin. This class can then define event and script methods, gesture bindings and other code. This will all be covered in depth later. """),
"",_(u"""NVDA loads all global plugins as soon as it starts, and unloads them on exit. """),
"",_(u"""### 3.6. Example 2: a Global Plugin Providing a Script to Announce the NVDA Version"""),
"",_(u"""The following example Global Plugin Allows you to press NVDA+shift+v while anywhere in the Operating System to find out NVDA's version. This example is only to show you the basic layout of a Global Plugin. """),
"",_(u"""Copy and paste the code between \\(but not including\\) the start and end markers into a new text file with a name of example2.py, which should be saved in the globalPlugins subdirectory. Be very careful to keep all tabs and spaces intact. """),
"",_(u"""Once saved in the right place, either restart NVDA or choose Reload Plugins found under Tools in the NVDA menu. """),
"",_(u"""From anywhere, you can now press NVDA+shift+v to have NVDA's version spoken and brailled. """),
_(u"""    """),
_(u"""    """),
_(u"""    --- start ---"""),
_(u"""    # Version announcement plugin for NVDA"""),
_(u"""    # Developer guide example 2"""),
_(u"""    """),
_(u"""    import globalPluginHandler"""),
_(u"""    import ui"""),
_(u"""    import versionInfo"""),
_(u"""    """),
_(u"""    class GlobalPlugin(globalPluginHandler.GlobalPlugin):"""),
_(u"""    """),
_(u"""    	def script_announceNVDAVersion(self, gesture):"""),
_(u"""    		ui.message(versionInfo.version)"""),
_(u"""    """),
_(u"""    	__gestures={"""),
_(u"""    		\"kb:NVDA+shift+v\": \"announceNVDAVersion\","""),
_(u"""    	}"""),
_(u"""    """),
_(u"""    --- end ---"""),
_(u"""    """),
"",_(u"""This Global Plugin file starts with two comment lines, which describe what the file is for. """),
"",_(u"""It then imports the globalPluginHandler module, so that the Global Plugin has access to the base GlobalPlugin class. """),
"",_(u"""It also imports a few other modules, namely ui and versionInfo, which this specific plugin needs in order for it to perform the necessary actions to announce the version. """),
"",_(u"""Next, it defines a class called GlobalPlugin, which is inherited from globalPluginHandler.GlobalPlugin. """),
"",_(u"""Inside this class, it defines 1 or more events, scripts or gesture bindings. In this example, it defines a script method that performs the version announcement, and provides a binding from NVDA+shift+v to this script. However, the details of the script and its binding are not important for the purposes of this example. The most important part is the class itself. """),
"",_(u"""As with other examples in this guide, remember to delete the created Global Plugin when finished testing and then restart NVDA or reload plugins, so that original functionality is restored. """),
"",_(u"""### 3.7. NVDA Objects"""),
"",_(u"""NVDA represents controls and other GUI elements as NVDA Objects. These NVDA Objects contain standardised properties, such as name, role, value, states and description, which allow other parts of NVDA to query or present information about a control in a generalised way. For example, the OK button in a dialog would be represented as an NVDA Object with a name of \"OK\" and a role of button. Similarly, a checkbox with a label of \"I agree\" would have a name of \"I agree\", a role of checkbox, and if currently checked, a state of checked. """),
"",_(u"""As there are many different GUI Toolkits and platform and accessibility APIs, NVDA Objects abstract these differences into a standard form that NVDA can use, regardless of the toolkit or API a particular control is made with. For example, the Ok button just discussed could be a widget in a Java application, an MSAA object, an IAccessible2 object or a UI Automation element. """),
"",_(u"""NVDA Objects have many properties. Some of the most useful are: """),
"",_(u"""  * name: the label of the control. """),
_(u"""  * role: one of the ROLE\\_\\* constants from NVDA's controlTypes module. Button, dialog, editableText, window and checkbox are examples of roles. """),
_(u"""  * states: a set of 0 or more of the STATE\\_\\* constants from NVDA's controlTypes module. Focusable, focused, selected, selectable, expanded, collapsed and checked are some examples of states. """),
_(u"""  * value: the value of the control; e.g. the percentage of a scroll bar or the current setting of a combo box. """),
_(u"""  * description: a sentence or two describing what the control does \\(usually the same as its tooltip\\). """),
_(u"""  * location: the object's left, top, width and height positions in screen coordinates. """),
_(u"""  * parent: this object's parent object. For example, a list item object's parent would be the list containing it. """),
_(u"""  * next: the object directly after this one on the same level in logical order. For example, a menu item NVDA Object's next object is most likely another menu item within the same menu. """),
_(u"""  * previous: like next but in reverse. """),
_(u"""  * firstChild: the first direct child object of this object. For example, a list's first child would be the first list item. """),
_(u"""  * lastChild: the last direct child of this object. """),
_(u"""  * children: a list of all the direct children of this object; e.g. all the menu items in a menu. """),
"","",_(u"""There are also a few simplified navigation properties such as simpleParent, simpleNext, simpleFirstChild and simpleLastChild. These are like their respective navigation properties described above, but NVDA filters out unuseful objects. These properties are used when NVDA's simple review mode is turned on, which is the default. These simple properties may be easier to use, but the real navigation properties more closely reflect the underlying Operating System structure. Also, these may change in future versions of NVDA as improvements are made to simple review, so they should generally be avoided when programmatically locating specific objects. """),
"",_(u"""When developing plugins, most of the time, it is not important what toolkit or API backs an NVDA Object, as the plugin will usually only access standard properties such as name, role and value. However, as plugins become more advanced, it is certainly possible to delve deeper into NVDA Objects to find out toolkit or API specific information if required. """),
"",_(u"""Plugins make use of NVDA Objects in three particular ways: """),
"",_(u"""  * Most events that plugins receive take an argument which is the NVDA Object on which the event occurred. For example, event\\_gainFocus takes the NVDA Object that represents the control gaining focus. """),
_(u"""  * Scripts, events or other code may fetch objects of interest such as the NVDA Object with focus, NVDA's current navigator object, or perhaps the Desktop NVDA Object. The code may then retreave information from that object or perhaps even retreave another object related to it \\(e.g. its parent, first child, etc.\\). """),
_(u"""  * the Plugin may define its own custom NVDA Object classes which will be used to wrap a specific control to give it extra functionality, mutate its properties, etc. """),
"","",_(u"""Just like App Modules and Global Plugins, NVDA Objects can also define events, scripts and gesture bindings. """),
"",_(u"""### 3.8. Scripts and Gesture Bindings"""),
"",_(u"""App Modules, Global Plugins and NVDA Objects can define special methods which can be bound to a particular piece of input such as a key press. NVDA refers to these methods as scripts. """),
"",_(u"""A script is a standard Python instance method with a name starting with \"script\\_\"; e.g. \"script\\_sayDateTime\". """),
"",_(u"""A script method takes two arguments: """),
"",_(u"""  * self: a reference to the App Module, Global Plugin or NVDA Object instance the script was called on. """),
_(u"""  * gesture: an Input Gesture object, which represents the input that caused the script to run. """),
"","",_(u"""As well as the actual script method, some form of gesture binding must be defined, so that NVDA knows what input should execute the script. """),
"",_(u"""To bind a gesture to a script, a special \"\\_\\_gestures\" Python dictionary can be defined as a class variable on the App Module, Global Plugin or NVDA Object. These dictionaries should contain gesture identifier strings pointing to the name of the requested script, without the \"script\\_\" prefix. """),
"",_(u"""There are more advanced ways of binding gestures in a more dynamic fashion, though the \\_\\_gestures dictionary is the simplest. """),
"",_(u"""A gesture identifier string is a simple string representation of a piece of input. It consists of a two leter character code denoting the source of the input, an optional device in brackets, a colon \\(:\\) and one or more names separated by a plus \\(+\\) denoting the actual keys or input values. """),
"",_(u"""Some examples of gesture string identifiers are: """),
"",_(u"""  * \"kb:NVDA+shift+v\" """),
_(u"""  * \"br\\(freedomScientific\\):leftWizWheelUp\" """),
_(u"""  * \"kb\\(laptop\\):NVDA+t\" """),
"","",_(u"""Currently, the input sources in NVDA are: """),
"",_(u"""  * kb: system keyboard input """),
_(u"""  * br: braille display controls """),
_(u"""  * ts: touch screen """),
_(u"""  * bk: braille keyboard input """),
"","",_(u"""When NVDA receives input, it looks for a matching gesture binding in a particular order. Once a gesture binding is found, the script is executed and no further bindings are used, nore is that particular gesture passed on automatically to the Operating System. """),
"",_(u"""The order for gesture binding lookup is: """),
"",_(u"""  * Loaded Global Plugins """),
_(u"""  * App Module of the active application """),
_(u"""  * Tree Interceptor of the NVDA Object with focus if any; e.g. a virtualBuffer """),
_(u"""  * NVDA Object with focus """),
_(u"""  * Global Commands \\(built in commands like quitting NVDA, object navigation commands, etc.\\) """),
"","",_(u"""You should specify a description of the script in the function's docstring which describes the command for users. For example, this is reported to users when in Input Help mode and shown in the Input Gestures dialog. You specify the docstring by setting a \" _doc_ \" attribute on the script function. The script will not appear in the Input Gestures dialog unless this is specified. """),
"",_(u"""You can also specify a category for a script so that it can be grouped with other similar scripts. For example, a script in a global plugin which adds browse mode quick navigation keys may be categorized under the \"Browse mode\" category. For individual scripts, this is done by setting a \"category\" attribute on the script function to a string containing the name of the category. You can also set the \"scriptCategory\" attribute on the plugin class, which will be used for scripts which do not specify a category. There are constants for common categories prefixed with SCRCAT\\_ in the inputCore and globalCommands modules. The script will be listed under the specified category in the Input Gestures dialog. If no category is specified, the script will be categorized under \"Miscellaneous\". """),
"",_(u"""### 3.9. Example 3: A Global Plugin to Find out Window Class and Control ID"""),
"",_(u"""The following Global Plugin allows you to press NVDA+leftArrow to have the window class of the current focus announced, and NVDA+rightArrow to have the window control ID of the current focus announced. This example shows you how to define one or more scripts and gesture bindings on a class such as an App Module, Global Plugin or NVDA Object. """),
"",_(u"""Copy and paste the code between \\(but not including\\) the start and end markers into a new text file with a name of example3.py, which should be saved in the globalPlugins subdirectory. Be very careful to keep all tabs and spaces intact. """),
"",_(u"""Once saved in the right place, either restart NVDA or choose Reload Plugins found under Tools in the NVDA menu. """),
_(u"""    """),
_(u"""    """),
_(u"""    --- start ---"""),
_(u"""    #Window utility scripts for NVDA"""),
_(u"""    #Developer guide example 3"""),
_(u"""    """),
_(u"""    import globalPluginHandler"""),
_(u"""    import ui"""),
_(u"""    import api"""),
_(u"""    """),
_(u"""    class GlobalPlugin(globalPluginHandler.GlobalPlugin):"""),
_(u"""    """),
_(u"""    	def script_announceWindowClassName(self, gesture):"""),
_(u"""    		focusObj = api.getFocusObject()"""),
_(u"""    		name = focusObj.name"""),
_(u"""    		windowClassName = focusObj.windowClassName"""),
_(u"""    		ui.message(\"class for %s window: %s\" % (name, windowClassName))"""),
_(u"""    """),
_(u"""    	def script_announceWindowControlID(self, gesture):"""),
_(u"""    		focusObj = api.getFocusObject()"""),
_(u"""    		name = focusObj.name"""),
_(u"""    		windowControlID = focusObj.windowControlID"""),
_(u"""    		ui.message(\"Control ID for %s window: %d\" % (name, windowControlID))"""),
_(u"""    """),
_(u"""    	__gestures = {"""),
_(u"""    		\"kb:NVDA+leftArrow\": \"announceWindowClassName\","""),
_(u"""    		\"kb:NVDA+rightArrow\": \"announceWindowControlID\","""),
_(u"""    	}"""),
_(u"""    """),
_(u"""    --- end ---"""),
_(u"""    """),
"",_(u"""### 3.10. Events"""),
"",_(u"""When NVDA detects particular toolkit, API or Operating System events, it abstracts these and fires its own internal events on plugins and NVDA Objects. """),
"",_(u"""Although most events are related to a specific NVDA Object \\(e.g. name change, gain focus, state change, etc.\\), these events can be handled at various levels. When an event is handled, it is stopped from going further down the chain. However, code inside the event can choose to propagate it further if needed. """),
"",_(u"""The order of levels through which the event passes until an event method is found is: """),
"",_(u"""  * Loaded Global Plugins """),
_(u"""  * The App Module associated with the NVDA Object on which the event was fired """),
_(u"""  * The Tree Interceptor \\(if any\\) associated with the NVDAObject on which the event was fired """),
_(u"""  * the NVDAObject itself. """),
"","",_(u"""Events are Python instance methods, with a name starting with \"event\\_\" followed by the actual name of the event \\(e.g. gainFocus\\). """),
"",_(u"""These event methods take slightly different arguments depending at what level they are defined. """),
"",_(u"""If an event for an NVDA Object is defined on an NVDA Object itself, the method only takes one mandatory argument which is the 'self' argument; i.e. the NVDA Object instance\\). Some events may take extra arguments, though this is quite rare. """),
"",_(u"""If an event for an NVDA Object is defined on a Global Plugin, App Module or Tree Interceptor, the event takes the following arguments: """),
"",_(u"""  * self: the instance of the Global Plugin, App Module or Tree Interceptor """),
_(u"""  * obj: the NVDA Object on which the event was fired """),
_(u"""  * nextHandler: a function that when called will propagate the event further down the chain. """),
"","",_(u"""Some common NVDA Object events are: """),
"",_(u"""  * foreground: this NVDA Object has become the new foreground object; i.e. active top-level object """),
_(u"""  * gainFocus """),
_(u"""  * focusEntered: Focus has moved inside this object; i.e. it is an ancestor of the focus object """),
_(u"""  * loseFocus """),
_(u"""  * nameChange """),
_(u"""  * valueChange """),
_(u"""  * stateChange """),
_(u"""  * caret: when the caret \\(insertion point\\) within this NVDA Object moves """),
_(u"""  * locationChange: physical screen location changes """),
"","",_(u"""There are many other events, though those listed above are usually the most useful. """),
"",_(u"""For an example of an event handled by an App Module, please refer to example 1 \\(focus beeps in notepad\\). """),
"",_(u"""### 3.11. the App Module SleepMode variable"""),
"",_(u"""App Modules have one very useful property called \"sleepMode\", which if set to true almost completely disables NVDA within that application. Sleep Mode is very useful for self voicing applications that have their own screen reading functionality, or perhaps even some games that need full use of the keyboard. """),
"",_(u"""Although sleep mode can be toggled on and off by the user with the key command NVDA+shift+s, a developer can choose to have sleep mode enabled by default for an application. This is done by providing an App Module for that application which simply sets sleepMode to True in the AppModule class. """),
"",_(u"""### 3.12. Example 4: A Sleep Mode App Module"""),
"",_(u"""The following code can be copied and pasted in to a text file, then saved in the appModules directory with the name of the application you wish to enable sleep mode for. As always, the file must have a .py extension. """),
_(u"""    """),
_(u"""    """),
_(u"""    --- start ---"""),
_(u"""    import appModuleHandler"""),
_(u"""    """),
_(u"""    class AppModule(appModuleHandler.AppModule):"""),
_(u"""    """),
_(u"""    	sleepMode = True"""),
_(u"""    """),
_(u"""    --- end ---"""),
_(u"""    """),
"",_(u"""### 3.13. Providing Custom NVDA Object Classes"""),
"",_(u"""Providing custom NVDA Object classes is probably the most powerful and useful way to improve the experience of an application in an NVDA plugin. This method allows you to place all the needed logic for a particular control altogether in one NVDA Object class for that control, rather than scattering code for many controls across a plugin's events. """),
"",_(u"""There are two steps to providing a custom NVDA Object class: """),
"",_(u"""  * Define the NVDA Object class and its events, scripts, gesture bindings and overridden properties. """),
_(u"""  * Tell NVDA to use this NVDA Object class in specific situations by handling it in the plugin's chooseNVDAObjectOverlayClasses method. """),
"","",_(u"""When defining a custom NVDAObject class, you have many NVDAObject base classes to choose from. These base classes contain the base support for the particular accessibility or OS API underlying the control, such as win32, MSAA or Java access Bridge. You should usually inherit your custom NVDAObject class from the highest base class you need in order to choose your class in the first place. For example, if you choose to use your custom NVDAObject class when the window class name is \"Edit\" and the window control ID is 15, you should probably inherit from NVDAObjects.window.Window, as clearly you are aware that this is a Window object. Similarly, if you match on MSAA's accRole property, you would probably need to inherit from NVDAObjects.IAccessible.IAccessible. You should also consider what properties you are going to override on the custom NVDA Object. For instance, if you are going to override an IAccessible specific property, such as shouldAllowIAccessibleFocusEvent, then you need to inherit from NVDAObjects.IAccessible.IAccessible. """),
"",_(u"""the chooseNVDAObjectOverlayClasses method can be implemented on app modules or global plugin classes. It takes 3 arguments: """),
"",_(u"""  1. self: the app module or global plugin instance. """),
_(u"""  2. obj: the NVDAObject for which classes are being chosen. """),
_(u"""  3. clsList: a Python list of NVDAObject classes that will be used for obj. """),
"","",_(u"""Inside this method, you should decide which custom NVDA Object class\\(es\\) \\(if any\\) this NVDA Object should use by checking its properties, etc. If a custom class should be used, it must be inserted into the class list, usually at the beginning. You can also remove classes chosen by NVDA from the class list, although this is rarely required. """),
"",_(u"""### 3.14. Example 5: Command to Retrieve the Length of Text in an Edit Field Using a Custom NVDA Object"""),
"",_(u"""This app module for notepad provides a command to report the number of characters in edit fields. You can activate it using NVDA+l. Notice that the command is specific to edit fields; i.e. it only works while you are focused in an edit field, rather than anywhere in the application. """),
"",_(u"""The following code can be copied and pasted in to a text file, then saved in the appModules directory with the name of notepad.py. """),
_(u"""    """),
_(u"""    """),
_(u"""    --- start ---"""),
_(u"""    import appModuleHandler"""),
_(u"""    from NVDAObjects.IAccessible import IAccessible"""),
_(u"""    import controlTypes"""),
_(u"""    import ui"""),
_(u"""    """),
_(u"""    class AppModule(appModuleHandler.AppModule):"""),
_(u"""    """),
_(u"""    	def chooseNVDAObjectOverlayClasses(self, obj, clsList):"""),
_(u"""    		if obj.windowClassName == \"Edit\" and obj.role == controlTypes.ROLE_EDITABLETEXT:"""),
_(u"""    			clsList.insert(0, EnhancedEditField)"""),
_(u"""    """),
_(u"""    class EnhancedEditField(IAccessible):"""),
_(u"""    """),
_(u"""    	def script_reportLength(self, gesture):"""),
_(u"""    		ui.message(\"%d\" % len(self.value))"""),
_(u"""    """),
_(u"""    	__gestures = {"""),
_(u"""    		\"kb:NVDA+l\": \"reportLength\","""),
_(u"""    	}"""),
_(u"""    """),
_(u"""    --- end ---"""),
_(u"""    """),
"",_(u"""### 3.15. Making Small Changes to an NVDA Object in App Modules"""),
"",_(u"""Sometimes, you may wish to make only small changes to an NVDA Object in an application, such as overriding its name or role. In these cases, you don't need the full power of a custom NVDA Object class. To do this, you can use the NVDAObject\\_init event available only on App Modules. """),
"",_(u"""The event\\_NVDAObject\\_init method takes two arguments: """),
"",_(u"""  1. self: the AppModule instance. """),
_(u"""  2. obj: the NVDAObject being initialized. """),
"","",_(u"""Inside this method, you can check whether this object is relevant and then override properties accordingly. """),
"",_(u"""### 3.16. Example 6: Labelling the Notepad Edit Field Using event\\_NVDAObject\\_init"""),
"",_(u"""This app module for notepad makes NVDA report Notepad's main edit field as having a name of \"content\". That is, when it receives focus, NVDA will say \"Content edit\". """),
"",_(u"""The following code can be copied and pasted in to a text file, then saved in the appModules directory with the name of notepad.py. """),
_(u"""    """),
_(u"""    """),
_(u"""    --- start ---"""),
_(u"""    import appModuleHandler"""),
_(u"""    from NVDAObjects.window import Window"""),
_(u"""    """),
_(u"""    class AppModule(appModuleHandler.AppModule):"""),
_(u"""    """),
_(u"""    	def event_NVDAObject_init(self, obj):"""),
_(u"""    		if isinstance(obj, Window) and obj.windowClassName == \"Edit\" and obj.windowControlID == 15:"""),
_(u"""    			obj.name = \"Content\""""),
_(u"""    --- end ---"""),
_(u"""    """),
"",_(u"""## 4\\. Packaging Code as NVDA Add-ons"""),
"",_(u"""To make it easy for users to share and install plugins and drivers, they can be packaged in to a single NVDA add-on package which the user can then install into a copy of NVDA via the Add-ons Manager found under Tools in the NVDA menu. Add-on packages are only supported in NVDA 2012.2 and later. An add-on package is simply a standard zip archive with the file extension of nvda-addon which contains a manifest file, optional install/uninstall code and one or more directories containing plugins and/or drivers. """),
"",_(u"""### 4.1. Non-ASCII File Names in Zip Archives"""),
"",_(u"""If your add-on includes files which contain non-ASCII \\(non-English\\) characters, you should create the zip archive such that it uses UTF-8 file names. This means that these files can be extracted properly on all systems, regardless of the system's configured language. Unfortunately, many zip archivers do not support this, including Windows Explorer. Generally, it has to be explicitly enabled even in archivers that do support it. [http://www.7-zip.org/](https://www.nvaccess.org/files/nvda/documentation/7-Zip) supports this, though it must be enabled by specifying the \"cu=on\" method parameter. """),
"",_(u"""### 4.2. Manifest Files"""),
"",_(u"""Each add-on package must contain a manifest file named manifest.ini. This must be a UTF-8 encoded text file. This manifest file contains key = value pares declaring info such as the add-on's name, version and description. """),
"",_(u"""#### 4.2.1. Available Fields"""),
"",_(u"""Although it is highly suggested that manifests contain all fields, the fields marked as mandatory must be included. Otherwise, the add-on will not install. """),
"",_(u"""  * name: A short unique name for the add-on. This is used to differentiate add-ons internally and is not shown to the user. \\(Mandatory\\) """),
_(u"""  * summary: The name of the add-on as shown to the user. \\(Mandatory\\) """),
_(u"""  * version: The version of this add-on; e.g. 2.0. \\(Mandatory\\) """),
_(u"""  * author: The author of this add-on, preferably in the form Full Name <email address>; e.g. Michael Curran <[mick@kulgan.net](mailto:mick@kulgan.net)>. \\(Mandatory\\) """),
_(u"""  * description: A sentence or two describing what the add-on does. """),
_(u"""  * url: A URL where this add-on, further info and upgrades can be found. """),
_(u"""  * docFileName: The name of the main documentation file for this add-on; e.g. readme.html. See the Add-on Documentation section for more details. """),
"","",_(u"""#### 4.2.2. An Example Manifest File"""),
_(u"""    """),
_(u"""    """),
_(u"""    --- start ---"""),
_(u"""    name = MyTestAddon"""),
_(u"""    summary = Cool Test Add-on"""),
_(u"""    version = 1.0"""),
_(u"""    description = An example add-on showing how to create add-ons!"""),
_(u"""    author = Michael Curran <mick@kulgan.net>"""),
_(u"""    url = http://www.nvda-project.org/wiki/Development"""),
_(u"""    --- end ---"""),
_(u"""    """),
"",_(u"""### 4.3. Plugins and Drivers"""),
"",_(u"""The following plugins and drivers can be included in an add-on: """),
"",_(u"""  * App modules: Place them in an appModules directory in the archive. """),
_(u"""  * Braille display drivers: Place them in a brailleDisplayDrivers directory in the archive. """),
_(u"""  * Global plugins: Place them in a globalPlugins directory in the archive. """),
_(u"""  * Synthesizer drivers: Place them in a synthDrivers directory in the archive. """),
"","",_(u"""### 4.4. Optional install / Uninstall code"""),
"",_(u"""If you need to execute code as your add-on is being installed or uninstalled from NVDA \\(e.g. to validate license information or to copy files to a custom location\\), you can provide a Python file called installTasks.py in the archive which contains special functions that NVDA will call while installing or uninstalling your add-on. This file should avoid loading any modules that are not absolutely necessary, especially Python C extensions or dlls from your own add-on, as this could cause later removal of the add-on to fail. However, if this does happen, the add-on directory will be renamed and then deleted after the next restart of NVDA. Finally, it should not depend on the existence or state of other add-ons, as they may not be installed, have already been removed or not yet be initialized. """),
"",_(u"""#### 4.4.1. the onInstall function"""),
"",_(u"""NVDA will look for and execute an onInstall function in installTasks.py after it has finished extracting the add-on into NVDA. Note that although the add-on will have been extracted at this time, its directory will have a .pendingInstall suffix until NVDA is restarted, the directory is renamed and the add-on is really loaded for the first time. If this function raises an exception, the installation of the add-on will fail and its directory will be cleaned up. """),
"",_(u"""#### 4.4.2. The onUninstall Function"""),
"",_(u"""NVDA will look for and execute an onUninstall function in installTasks.py when NVDA is restarted after the user has chosen to remove the add-on. After this function completes, the add-on's directory will automatically be removed. As this happens on NVDA startup before other components are initialized, this function cannot request input from the user. """),
"",_(u"""### 4.5. Localizing Add-ons"""),
"",_(u"""It is possible to provide locale-specific information and messages for your add-on. Locale information can be stored in a locale directory in the archive. This directory should contain directories for each language it supports, using the same language code format as the rest of NVDA; e.g. en for English, fr\\_CA for French Canadian. """),
"",_(u"""#### 4.5.1. Locale-specific Manifest Files"""),
"",_(u"""Each of these language directories can contain a locale-specific manifest file called manifest.ini, which can contain a small subset of the manifest fields for translation. These fields are summary and description. All other fields will be ignored. """),
"",_(u"""#### 4.5.2. Locale-specific Messages"""),
"",_(u"""Each language directory can also contain gettext information, which is the system used to translate the rest of NVDA's user interface and reported messages. As with the rest of NVDA, an nvda.mo compiled gettext database file should be placed in the LC\\_MESSAGES directory within this directory. to allow plugins in your add-on to access gettext message information via calls to \\_\\(\\), you must initialize translations at the top of each Python module by calling addonHandler.initTranslation\\(\\). For more information about gettext and NVDA translation in general, please read <http://www.nvda-project.org/wiki/TranslatingNVDA>"""),
"",_(u"""### 4.6. Add-on Documentation"""),
"",_(u"""Documentation for an add-on should be placed in a doc directory in the archive. Similar to the locale directory, this directory should contain directories for each language in which documentation is available. """),
"",_(u"""Users can access documentation for a particular add-on by opening the Add-ons Manager, selecting the add-on and pressing the Add-on help button. This will open the file named in the docFileName parameter of the manifest. NVDA will search for this file in the appropriate language directories. For example, if docFileName is set to readme.html and the user is using English, NVDA will open doc\\en\\readme.html. """),
"",_(u"""## 5\\. NVDA Python Console"""),
"",_(u"""The NVDA Python console emulates the interactive Python interpreter from within NVDA. It is a development tool which is useful for debugging, general inspection of NVDA internals or inspection of the accessibility hierarchy of an application. """),
"",_(u"""### 5.1. Usage"""),
"",_(u"""The console can be activated in two ways: """),
"",_(u"""  * By pressing NVDA+control+z. If activated in this fashion, a snapshot of the current state of NVDA at the time the key was pressed will be taken and saved in certain variables available in the console. See Snapshot Variables for more details. """),
_(u"""  * By selecting Tools -> Python console from the NVDA system tray menu. """),
"","",_(u"""The console is similar to the standard interactive Python interpreter. Input is accepted one line at a time. The current line is processed when enter is pressed. You can navigate through the history of previously entered lines using the up and down arrow keys. """),
"",_(u"""Output \\(responses from the interpreter\\) will be spoken when enter is pressed. The f6 key toggles between the input and output controls. """),
"",_(u"""Closing the console window simply hides it. This allows the user to return to the session as it was left when it was closed, including history and variables. """),
"",_(u"""### 5.2. Namespace"""),
"",_(u"""#### 5.2.1. Automatic Imports"""),
"",_(u"""For convenience, the following modules and variables are automatically imported in the console: sys, os, wx, log \\(from logHandler\\), api, queueHandler, speech, braille """),
"",_(u"""#### 5.2.2. Snapshot Variables"""),
"",_(u"""Whenever NVDA+control+z is pressed, certain variables available in the console will be assigned according to the current state of NVDA. These variables are: """),
"",_(u"""  * focus: The current focus object """),
_(u"""  * focusAnc: The ancestors of the current focus object """),
_(u"""  * fdl: Focus difference level; i.e. the level at which the ancestors for the current and previous focus differ """),
_(u"""  * fg: The current foreground object """),
_(u"""  * nav: The current navigator object """),
_(u"""  * mouse: The current mouse object """),
_(u"""  * brlRegions: The braille regions from the active braille buffer """),
"","",_(u"""## 6\\. Remote Python Console"""),
"",_(u"""A remote Python console is available for situations where remote debugging of NVDA is useful. It is similar to the local Python console discussed above, but is accessed via TCP. """),
"",_(u"""Please be aware that this is a huge security risk. You should only enable it if you are connected to trusted networks. """),
"",_(u"""### 6.1. Usage"""),
"",_(u"""To enable the remote Python console, use the local Python console to import remotePythonConsole and call remotePythonConsole.initialize\\(\\). You can then connect to it via TCP port 6832. """),
"",_(u"""History of previously entered lines is not supported. """),
"",_(u"""The namespace is the same as the namespace in the local Python console. """),
"",_(u"""There are some special functions: """),
"",_(u"""  * snap\\(\\): Takes a snapshot of the current state of NVDA and saves it in the snapshot variables. """),
_(u"""  * rmSnap\\(\\): Removes all snapshot variables. """),
"",]