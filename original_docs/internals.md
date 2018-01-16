# NVDA feature internals

This article is designed to give users and developers a tour of internals of various features of NVDA. Thus, it is important to have some knowledge of NVDA itself, Python, C++ and programming concepts to follow this article.

Note: This article is directly based on (and is an enhanced version of) the design overview document found in NVDA Community website. Parts of this article are based on NVDA User Guide.

----
[[PageOutline(2-4,,inline)]]
----

## Introduction

### About NVDA

NVDA (Nonvisual Desktop Access) is a free, open-source, community-driven screen reader for Microsoft Windows. This modular, highly extensible screen reader provides all the features expected from screen readers, such as accepting keyboard input to perform various tasks, displaying a rich set of configuration options, responding to events and so on.

### Audience

As this is an article on feature internals, we will assume that you meet the following prerequisites:

- You are a user of NVDA and curious about how things work.
- You have some experience with programming and are familiar with C++ and Python.
- You would like to contribute your expertise but don't know where to start and how NVDA performs its job.
- You are a new or a seasoned NVDA add-on writer and like to dive deeper into NVDA internals.

### Article structure

It might be pointless to talk about internals of a complex software system such as NVDA without having something we can follow. As such, we'll start by letting you see how to obtain NVDA source code and the software packages involved in doing this and building NVDA for the first time.

After you download the source code, you might be interested in seeing the contents of the source code folder and the modules which holds NVDA together. In addition to learning more about various NVDA components and a high-level overview of runtime life of NVDA, you'll get a chance to learn why NVDA uses two programming languages for various tasks.

Next, we'll visit routines that will let NVDA start on your computer (installer and launcher), including the trick NVDA employs to detect that it is installed on a computer or running from a USB flash drive. Following that, we'll visit core.main, the function responsible for starting and exiting NVDA and things it does in between.

A significant portion of the article will focus on the life of NVDA and things it does to let thousands of blind people use computers. We'll visit what scripts and events are, how accessibility API's are handled, how overlay classes and objects come to life, a tour of browse mode functionality and get a chance to interview various app modules, speech synthesizers and braille display driver modules. We'll then visit add-on subsystem and discuss how various add-ons use various NVDA functionality.

Following our discussion of important NVDA routines, we'll take a look at NVDA's user interface and how user settings are managed. We'll also tour what happens when NVDA is told to check for updates, how NVDA changes its behavior when running from secure screens, Ease of Access integration and other miscellaneous services.

Lastly, we'll talk about how you can make a feature idea come to life. We'll briefly talk about coding style, submitting patches for review and will conclude with development process.

## Where to obtain NVDA source code and compile NVDA

If you would like to learn NVDA's internals, it is important to have NVDA source code handy. Like many open-source projects, NVDA uses Git for source code management. For more information on obtaining source code, see AccessingAndRunningSourceCode article.

### Building NVDA

There are times when you would like to see NVDA in action. To help you with this and in case you'd like to test a new feature idea, you should build NVDA from source. Source code compilation steps are managed by SCons, and details on how to build NVDA from source can be found in readme.md found in the root directory of the NVDA source code.

## NVDA components and source code layout

When you open the folder containing the source code, you may have noticed that it is composed of various directories besides the "source" directory. Let's examine the folder structure, and after that, we'll tour various components that holds NVDA together.

### Source code folder structure

The source code package comprises following folders and files:

- build: Created when NVDA is built from source and is used as a staging area for compiled code.
- extras: Contains NVDA Controller Client package.
- include: Major dependencies needed by NVDA, such as IAccessible2 library, are stored here.
- launcher: Holds the MSI for NVDA's launcher.
- misc-deps: The miscellaneous dependencies folder houses other packages required to build NVDA such as various Python packages.
- nvdaHelper: Contains the C++ portion of NVDA used in various situations.
- output: The resulting packages from various build tasks are stored here.
- site_scons: Other packages built by SCons are stored here.
- source: This is where Python portion of NVDA lives. We'll talk about contents of this directory throughout this article.
- uninstaller: Routines used by NVDA's uninstaller is stored here.
- user_docs: Documentation files for NVDA are stored in this folder.

### NVDA components overview

NVDA relies on various components to perform its job, such as supporting various accessibility API's, understanidng keyboard commands, sending output to a braille display and more. Here is a complete list of components used by NVDA:

- Installer: This module is the first module encountered when using NVDA for the very first time.
- Launcher (nvda.pyw, nvda.exe if using binary builds): Used to start NVDA. This module is responsible for checking command-line arguments and performs initial startup tasks.
- NVDA service: This is used when NVDA runs as a service, such as when using NVDA in secure screens. A related module is used to register NVDA with Ease of Access (Windows Vista and later).
- Core: Performs bulk of NVDA's startup routine, coordinates how NVDA should exit and involved in NVDA's life from start to finish.
- Event processor: Routines in event handler and queue handler are used to process events, queue events and perform related actions.
- Accessibility API support: NVDA comes with handlers for MSAA (Microsoft Active Accessibility)/IAccessible, IAccessible2, Java Access Bridge (JAB) and UI Automation (UIA). Together with various overlay classes, API handlers allow NVDA to present uniform experience across different API's.
- Text navigation and access: Various methods for handling different types of text widgets are provided in text infos package.
- App modules: NVDA comes with several app modules to let you use NVDA in various apps. Coordinating app module support is app module handler, and its duties include managing app module initialization and termination and keeping track of which app modules are active.
- Global plugins: A global plugin adds interesting functionality to be used by NVDA users, and there is a manager that keeps an eye on global plugins: global plugin handler.
- Add-on subsystem: You can write or use add-ons to enhance NVDA's functionality. Coordinating various NVDA add-ons is add-on handler, which is invoked when installing and removing add-ons and throughout the life of an add-on.
- Browse mode management: Routines housed in virtual buffers package and browse mode module allow you to navigate complex documents such as PDF documents and websites.
- Input support: The input core and its subordinates handle various input scenarios. This include a key press from a keyboard, flick on a touchscreen, tracking mouse movement and recording actions associated with a button on a braille display.
- Output routines: NVDA can be told to announce something via speech, braille, tones, wave file playback or combination of these.
- Speech and synthesizers: These two subsystems allow NVDA to speak things on screen via a user-defined speech synthesizer.
- Braille display management: This complex subsystem allows NVDA to communicate with various braille displays to send braille text or receive and interpret input from them.
- Message announcer: NVDA can announce various information via speech and/or braille using a function in the "ui" module.
- Graphical user interface: NVDA can show various dialogs, windows and so on, all housed in the "gui" package.
- Configuration management: The config package not only houses the default configuration for NVDA, but also acts as a clerk responsible for managing user configuration such as switching between configuration profiles.
- Localization support: Various modules are involved when supporting NVDA localization, including language handler and translation files for NVDA interfaces in different languages.
- NVDA helper: this module performs two things: allows NVDA's Python routines to call C++ routines and used to let NVDA communicate with other programs via code injection and other advanced techniques.
- Windows API wrappers: NVDA comes with wrapper modules for some Windows API functions, housed in different modules named after Windows API libraries such as user32.dll wrapped in winUser.py.

We will examine these modules in detail throughout this article (the rest of this article is based on the Design Overview article). But first, let's learn more about NVDA's architecture, starting with some important definitions.

## Terminology

### Abbreviations
 * API: Application programming interface
 * GUI: Graphical user interface
 * OS: Operating system
 * DLL: Dynamic Link Library
 

### Definitions
 * Caret: The system cursor; i.e. the cursor generally moved when you use the normal cursor keys.
 * Focus: The highlighted region of screen where the system sets focus.
 * Script: A function which is executed in response to input from the user such  as key presses from the keyboard, manipulating braille display controls and taps on touchscreens. Also known as a command.
 * Gesture: A piece of input such as a keyboard command.
 * Event: A routine to be used when certain conditions occur.
 * Widget: An individual component in a GUI with which a user can interact; e.g. a button, an editable text field, a list box, etc. Also known as a control or object.

## General

### Programming Languages
NVDA is primarily written in the [Python programming language](http://www.python.org/), which allows for rapid development among other benefits. Code that needs to be [#In-processCode injected into other processes] is written in C++ for high performance.

Note: Because of dependencies, NVDA is written using Python 2.7.

### Accessibility APIs
In order to make graphical widgets accessible to assistive technologies, operating systems and applications can use special purpose accessibility APIs. These APIs provide information about the widget such as its name, type/role (button, check box, editable text field, etc.), description, value, states (checked, unavailable, invisible, etc.) and keyboard shortcut. Accessibility APIs also provide events to allow assistive technologies to monitor changes, such as when the focus changes, properties of an object (such as name, description, value, and state) change, etc. Rich accessibility APIs provide additional information, including the ability to access detailed information about and track the cursor in editable text controls, and table information such as row and column coordinates. NVDA relies heavily on accessibility APIs to gather information. Several accessibility APIs are used, including Microsoft Active Accessibility (MSAA) (also known as IAccessible), [IAccessible2](http://www.linuxfoundation.org/en/Accessibility/IAccessible2), Java Access Bridge and UI Automation.

### Native APIs
Some widgets do not expose sufficient information via accessibility APIs to make them fully accessible. For example, MSAA, which is the accessibility API used by most standard Windows controls, does not provide the ability to obtain the location of the cursor or retrieve individual units of text in editable text fields. However, some widgets provide their own native APIs (not specific to accessibility) which can be used to obtain this information. NVDA makes use of these APIs where possible; e.g. in standard edit controls.

### Operating System Functions
Aside from accessibility and native APIs, Windows provides many functions which can be used to obtain information and perform tasks. Information that can be obtained includes the class name of a window, the current foreground window and system battery status. Tasks that can be performed include moving/clicking the mouse and sending key presses.

## NVDA Components
NVDA is built with an extensible, modular, object oriented, abstract design. It is divided into several distinct components.

### Launcher
The launcher is the module which the user executes to start NVDA. It is contained in the file `nvda.pyw` (`nvda.exe` or variations for binary builds). It handles command line arguments, performs some basic initialisation and starts the [#Core core] (unless NVDA is already running or a command line option specifies otherwise).

### Core
The core (in the function `core.main`) loads the configuration, initialises all other components and then enters the main loop.

The initialization steps in `core.main` are thus:

1. Obtains the configuration file path and the name for the initial configuration file unless overridden from the command line.
2. Initializes configuration management subsystem (`config.initialize`).
3. Unless silenced by the user, NVDA's startup sound is played unless minimal initialization option is specified in the command line.
4. Obtains following information:

* Log level as defined by the user unless a predefined log level is specified in the command line.
* Language (either a specific language or the language used by the Windows operating system).
* Version information for NVDA, Python, Windows and COMTypes package.

5. Loads add-ons (by default, they live in addons folder in user configuration folder). One of the jobs of this routine is to see if the user told NVDA to disable add-ons.
6. Next, NVDA continues by initializing app module handler, NvDA Helper and speech components including speech dictionaries.
7. If it took NVDA five seconds or more to initialize components, this fact is recorded and the user will hear, "Loading NVDA, please wait".
8. Next, wxPython, braille support (including braille input module), display model and GUI subsystem are prepared.
9. Localization support preparation is next, preparing NVDA to display its interface in the configured language.
10. The NVDA API module is initialized, including setting initial focus, mouse and other objects.
11. NvDA then initializes various modules for accessibility API's. In case of Java Access Bridge (JAB) and UI Automation (UIA), relevant checks are performed at this time (for example, making sure the user is running Windows 7 or later when initializing UIA support).
12. Next, input support modules are initialized, including the input core itself and modules supporting input from keyboards, mice and touchscreens (if one is installed on a computer running Windows 8 and later).
13. Lastly, global plugin handler and global plugins are initialized. With this step complete, basic NVDA features such as GUI support are ready for action.
14. Depending on command line options, configuration values and circumstances such as installing silently, NVDA will perform appropriate action such as displaying the welcome dialog, performing automatic update check and so on.

The main loop keeps looping until NVDA is instructed to exit. IN each iteration/tick, the core pumps the [#APIHandlers API] and [#InputHandlers input] handlers, [#RegisteredGenerators registered generators] and the main queue. All events, scripts, etc. are indirectly queued to this main queue by API and input handlers, so pumping the main queue causes these to be executed. The main loop is what "drives" NVDA or makes it "tick".

Once NVDA is instructed to exit, the core terminates all other components, saves the configuration if appropriate and then exits. The details steps are as follows:

1. If update check is in progress, tells update check to quit.
2. NVDA then terminates watchdog (NVDA core monitor), global plugin support (along with global plugins if any), GUI subsystem and saves user settings if told to do so.
3. If focus is located on a control, NVDA is instructed to call lose focus event on this control.
4. NVDA continues by terminating various subsystems, starting with tree interceptor handler, accessibility API support, app module handler and various app modules, input handlers, speech and braille support and add-on handler.
5. Lastly, unless explicitly silenced, NVDA shutdown sound is played, and the message window is destroyed.

#### Event and Script Handling
Rather than queuing scripts and events directly to the main queue, this is abstracted using the `eventHandler` and `scriptHandler` modules. Input and API handlers use these modules to queue or directly execute scripts and events.

#### Registered Generators
Some tasks need to run in the background without causing NVDA to block (freeze) while waiting for them to complete. They need to execute code regularly, but at no specific time interval. NVDA allows Python generator functions to be registered for this purpose. Once registered, the generator will be pumped once for each iteration/tick of the main loop. Examples of this include the say all and speak spelling functionality. They are registered using `queueHandler.registerGeneratorObject`.

### Input Handlers
The input handlers handle input from various sources. Currently, there are three main input handler modules: `keyboardHandler`, `mouseHandler` and `touchHandler`. [#OutputDrivers Braille display drivers] can also handle input. These handlers listen for input and generate appropriate [#InputGestures input gestures] and events.

### Input Gestures
An input gesture is an abstract representation of a single piece of input from the user; e.g. a key press. All input gestures derive from the base `inputCore.InputGesture` class. This allows all input to be handled in a consistent, unified way. For example, any input gesture can be bound to any script, both in code and by the user.

### API Handlers
These handle initialisation, listening for events and termination for specific accessibility and native APIs. They also contain utility functions useful for working with their API. When an event is received for a widget, an appropriate [#NVDAObjects NVDA object] is fetched or constructed and an event is then queued for that NVDA object. Together with [#NVDAObjects NVDA objects], they abstract the handling of queries and events for specific APIs so that the bulk of NVDA need not be concerned with specific APIs. To introduce support for a new API, a developer just creates another API handler and appropriate NVDA objects without needing to change the majority of the code. API handler modules include `IAccessibleHandler` for MSAA/IAccessible and IAccessible2, `JABHandler` for Java Access Bridge and `UIAHandler` for UI Automation.

### Output Modules
Separate modules encapsulate the handling of output functionality. Currently, there are two main output modules: `speech` and `braille`. There is also the `tones` module, which is used to output tones/beeps, and `nvWave` module used to play wave files indicating specific events.

For most cases, speech and braille will output similar texts. To facilitate this, a dedicated user interface (ui) module is provided to speak and/or braille a message. This function (`ui.message`) calls `speech.speakMessage` and `braille.handler.message` functions.

### Output Drivers
Synth drivers are drivers to allow NVDA to utilise particular speech synthesisers. They are derived from the `synthDriverHandler.SynthDriver` base class.

Braille display drivers are drivers to allow NVDA to utilise particular braille displays. They are derived from the `braille.BrailleDisplayDriver` base class.

### NVDA Objects
An NVDA object (NVDAObject) is an abstract representation of a single widget in NVDA. All NVDA objects derive from the base `NVDAObjects.NVDAObject` class. Methods and properties are used to query information about, handle events from and execute actions on the widget represented by the NVDA object in an abstract way. This means that the bulk of NVDA need not be concerned with specific accessibility or native APIs, but can instead work with a single, abstract representation. This allows for the seemless support and integration of many vastly different APIs.

It is here that the full power of object oriented programming is used. Many methods are implemented on the base `NVDAObject` class and only need to be overridden if specific functionality is required. Similarly, if a particular widget is non-standard, problematic, provides additional information using other mechanisms, etc., it can simply subclass another NVDA object and override methods as appropriate.

NVDA objects that might be used in any application are contained in the NVDAObjects package. [#AppModules App modules] may also define NVDA objects specific to an application.

### Text Ranges
When working with editable text controls, NVDA needs to be able to obtain information about the text in the widget. Aside from just retrieving the entire text, proper navigation requires retrieval of specific units of text (e.g. paragraphs, lines, words and characters), as well as the ability to find and set the location of the caret and selection. Also, if the widget supports formatting, NVDA should be able to retrieve text attributes such as font name, size, bold, italic, underline and whether there is a spelling error. Each API provides a different way of querying and manipulating text. Just as NVDA objects provide an abstract representation of a widget, TextInfo objects provide an abstract representation of a range of text. These objects are derived from the `textInfos.TextInfo` base class.

### Global Commands
The global commands object (`globalCommands.GlobalCommands`) contains built-in global scripts; i.e. they can be executed everywhere. For example, the review, report current focus and date/time scripts are all located in global commands.

### Plugins
NvDA allows third-parties to extend NvDA's functionality through plugins and add-ons. These may define custom NVDA objects for specific applications, add global features and add support for new braille displays and speech synthesizers. There are three plugin types: appModules, globalPlugins and drivers, with drivers further divided between speech synthesizer and braille display support.

#### App Modules
Generally, most widgets may appear in any application and an [#NVDAObjects NVDA object] should therefore be included in the main `NVDAObjects` package. However, there are sometimes cases where a widget is implemented specifically for one application, as well as cases where a single event must be overridden or a script must be provided only in one application. An app module provides support specific to an application for these cases.

An app module is derived from the `appModuleHandler.AppModule` base class. App modules receive events for all [#NVDAObjects NVDA objects] in the application and can bind scripts which can be executed anywhere in that application. They can also implement their own NVDA objects for use within the application.

#### Global Plugins
Aside from application specific customisation using [#AppModules app modules], it is also possible to extend NVDA on a global level. For example, new global commands can be added, behaviour can be changed and new GUI toolkits can be supported. This can be done using global plugins.

A global plugin is derived from the `globalPluginHandler.GlobalPlugin` base class. Similar to [#GlobalCommands global commands], they can bind scripts which can be executed everywhere. They can also implement their own global [#NVDAObjects NVDA Objects].

### Tree Interceptors
Sometimes, it is necessary to intercept events and scripts for an entire hierarchy (or tree) of [#NVDAObjects NVDA objects]. For example, this is necessary to seemlessly handle complex documents which consist of many objects. This can be done using a tree interceptor.

A tree interceptor (TreeInterceptor) is derived from the `treeInterceptorHandler.TreeInterceptor` base class. It receives events and scripts for all [#NVDAObjects NVDA objects] beneath and including the root NVDA object. Tree interceptors are created when a TreeInterceptor class is returned from the `treeInterceptorClass` property of an NVDA object.

### Virtual Buffers
Complex documents such as web pages are very often not flat; i.e. information does not simply run from top to bottom. Because of this, complex document browsers often do not provide a way to navigate documents using the caret, and even when they do, it is often problematic. Therefore, screen readers need to create their own flat representation of a document from the object hierarchy provided by the browser and allow the user to navigate this flat representation. NVDA calls these virtual buffers. Due to the extreme slowness of performing large numbers of [#Out-of-processCode out-of-process] queries, NVDA creates these with the help of [#In-processCode in-process code].

A virtual buffer (VirtualBuffer) in NVDA is derived from the `virtualBuffers.VirtualBuffer` base class and is a type of [#TreeInterceptors tree interceptor].

### GUI
NVDA has its own graphical user interface to allow for easy configuration and other user interaction. This code is primarily contained in the `gui` package. [wxPython](http://www.wxpython.org/) is used as the GUI toolkit.

## Special Object Functions

### Events
NVDA object, app module and virtual buffer instances can all contain special methods which handle events for NVDA Objects. These methods are all named beginning with "event_"; e.g. `event_gainFocus` and `event_nameChange`. These events are generally executed by a call to `eventHandler.executeEvent`, which is in turn generally called resultant to events queued by [#APIHandlers API Handlers]. Most events do not take any additional arguments. App modules and virtual buffers are passed a handler function which should be called if the event should be handled by the next handler; e.g. the object itself.

### Scripts
NVDA object, app module and virtual buffer instances can all contain special methods called scripts which are executed in response to [#InputGestures input gestures] from the user. These methods are all named beginning with "script_"; e.g. `script_reportCurrentFocus` and `script_dateTime`. Script methods are passed the input gesture that triggered them.

Input gestures are bound to scripts in the class using a `__gestures` dict. They can also be bound at runtime using `bindGesture`. These are inherited from `baseObject.ScriptableObject`.

## Inter-process Communication
In general terms, every running application or service on a computer, including NVDA, is a separate process. No process can access data in another process except via special operating system mechanisms. This is called inter-process communication (IPC).

### Out-of-process Code
NVDA functions primarily out-of-process. That is, events and queries for information from other processes must be marshalled (communicated) between NVDA and the process in question using IPC. This is many times slower than queries and events managed in the same process. However, for the majority of screen reader functionality, this performance hit is insignificant.

### In-process Code
When large numbers of queries need to be made in one hit, working [#Out-of-processCode out-of-process] is far too slow. A noteworthy example is rendering a web page into a flat representation, as is done by [#VirtualBuffers virtual buffers]. In these cases, code can be "injected" into the remote process. Because this code is running in the same process, queries and events are much faster, as they do not have to be marshalled between processes, which means that large numbers of queries are quite fast. NVDA can then perform single out-of-process queries for relevant information.

In-process code must be small and light-weight, as it is being injected into other processes. It must also be as fast as possible to allow for maximum performance. Python is unsuitable for this task. All of NVDA's in-process code is written in C++, which allows for maximum performance and minimal overhead.