# NVDA Add-on internals: Enhanced Touch Gestures

Author: Joseph Lee

## Introduction

Touch-based user interface is everywhere: from smartwatches to some mainframe computers, from home automation systems to aircraft monitoring equipments. The idea of using one's finger to manipulate screen elements was a dream many decades ago, but in the 21st century, new products equipped with touchscreens appear every day, more so in the world of smartphones and tablets.

For blind people, the most common way to interact with a computer has been, and still is, keyboard. But increasingly, thanks to technologies such as Apple's VoiceOver and Google Accessibility suite, it became possible for blind people to interact with computers and smartphones via touch. This is more so now that Windows screen readers such as Narrator and NVDA comes with built-in support for touchscreen access, with more work to be done in some areas.

In NVDA Add-on Internals: Enhanced Touch Gestures, we'll take a look at how NVDA's touchscreen support is implemented, as well as how this add-on helps enhance user experience on touchscreens.

## Timeline of NVDA's touch support

Touch support in NVDA can be traced to efforts by various mobile screen readers in the 2000's, most significantly, for Windows Mobile and VoiceOver on iOS. Screen readers for Windows Mobile such as Code Factory's Mobile Speak (discontinued) provided basic touch commands for navigation and performing basic tasks. Compared to today's touchscreen devices, devices from Windows Mobile era were resistive devices, often requiring use of a stylus. Although revolutionary at that time, touch-based mobile device interaction were a nitch market, and combined with lack of accessibility guidelines for early smartphones, early iOS and Android devices were not recommended for use by blind people.

This changed in 2009 when Apple announced VoiceOver as part of iOS 3.0. This mobile screen reader, partly derived from VoiceOver on OS X/macOS with optimizations for touch interaction, were met with immediate success. With VoiceOver preinstalled, devices running iOS 3 and later (including iPhone, iPad, iPod Touch and others) became accessible for blind people, made more significant because of intuitive touch commands for navigation and various tasks. Google followed suit, introducing a series of Android relesaes with TalkBack, a built-in screen reader for Android, along iwth accessibility services designed to allow third-party solutions to provide additoinal services.

Touchscreen devices became a mainstream on Windows computers in 2012 with the release of Windows 8. Although Windows 7 and earlier had basic support for touchscreens, it wasn't until Windows 8 that touch interaction took on a more prominent role. Learning from Apple and Google, Microsoft introduced a substantially revamped Narrator with built-in touch support, along with support services so third party screen readers such as NVDA can take advantage of touch interaction. This NVDA did, and NVDA 2012.3 (November 2012) became one of the first third-party screen readers to support touchscreens on Windows natively.

## How touch support in NVDA works

In order for NVDA to support touchscreens, it must be installed on a computer running Windows 8 and later (portable and temporary installers will not work). This is because as part of touch support, NVDA must communicate with Ease of Access regarding modifying touch interaction flags, wihch can be done as long as the running executable is registered with Ease of Access (only the installed copy is eligible to do this). In addition, a touchscreen monitor must support at least five touch points, although most touchscreens support 10 touch points.

At startup, once NVDA detects that touchscreen support can be used, it starts a touch handler thread that informs Ease of Access that an assistive technology supporting touch interaction is active, along with creating a touch event window that receives touch input events. The job of the touch events window is to detect touch input and ask a touch tracker manager to construct a more meaningful representation of a touch input, commonly known as a "touch gesture". Currently NVDA can recognize a tap (short press), flicks (short travel), tap and hold (tap followed by another tap and a holding gesture), hovers (moving around the screen with one finger without removing the finger from the screen), and a combination of these taking place with at least one finger (the maximum being how many touch points are supported by the monitor). When NVDA closes, NVDA closes the touch handler thread, which in turn kills the touch events window and informs Ease of Access that NVDA is exiting so touch interaction can return to normal.

Each piece of touch input is recorded via a touch tracker object. Single finger tracker is used to track one finger gestures, while multi-touch tracker is used to generalize this to multiple fingers. Each touch tracker records which finger was used, direction of travel, tap count, and if this gesture is part of a hover gesture. Collectively, these tracker objects are represented under a dedicated input gesture so NVDA commands can be assigned to them, including those found in Enhanced Touch Gestures add-on.

## Introducing Enhanced Touch Gestures add-on

As the name implies, Enhanced Touch Gestures enhances the touch interaction experience for users. The overall goal of this add-on is to provide touch commands for some common NVDA commands that come with no touch commands by default, as well as providing additional navigation possibilities such as web navigation.

This add-on began in 2013 shortly after acquiring a touch-capable computer. I studied touch support features provided by NVDA, and because I was familiar with iOS, I looked at differences between NVDA and Voiceover in terms of touch commands. Some features of this add-on are result of trying to reduce the gap between screen readers, while others were born out of suggestions from users such as passthrough mode (see below).

Recently, another goal has emerged: pull requests for NVDA. Because of popularity of Enhanced Touch Gestures, I decided to send some features of this add-on to NV Access as a series of pull requests. As of time of this writing (August 2019), at least one pull request based on this add-on has been submitted for code review for inclusion in future NVDA releases.

## Add-on structure

While powerful, all the action takes place inside a single global plugin module. The global plugin is divided into the following parts:

* Touch commands for common actions such as announcing status bar, title bar and others.
* Support enhancers such as additional touch modes and coordinate announcement beep.
* Additional navigation possibilities such as web navigation.
* Touch passthrough mode and other additional features that might be included in NVDA in the future.
* Dedicated features for touch keyboard.
* Additional touch interaction settings.

Some features are now part of NVDA, most notably touch typing toggle.

## Additional touch modes

By default, NVDA comes with object and text touch modes, which can be toggled by doing a three finger single tap. Enhance Touch Gestures adds up to two additional touch modes:

* Web mode: used to navigate web elements. In this mode, one finger flick up and down cycles between web elements, while one finger flickt left and right navigates via the chosen element.
* Synth settings mode: in this mode, two finger flick left and right cycles through synth settings ring options, while two finger flick up and down changes values.

### Web touch mode

Web touch mode is designed to allow users to navigate complex documents. In short, this is similar to various element rotor options in VoiceOver.

By default, normal mode is used. In this mode, one finger flick left and right moves through objects just as one can do in object touch mode. The other element types are link, heading, frame, table, landmark, and forms.

Internally, element navigation calls relevant single letter navigation scripts except for normal mode which calls next/previous object in flow commands. The available elements are housed inside a tuple, and changing the navigation element changes which tuple entry is looked up for web navigation gestures.

## Touch keyboard

Touch keyboard, as the name implies, allows users to type using a virtual keyboard that appears on screen. One can type characters, perform function commands, and access additional symbols not "printed" on the keyboard.

Three features (for one, a bug fix) are grouped under touch keyboard support provided by Enhanced Touch Gestures, with one of them now part of NVDA:

* Summoning and dismissing touch keyboard.
* Removing extraneous information while announcing keyboard keys such as read-only state which isn't accurate.
* Controlling whether keys are typed by double-tapping it or lifting one's finger.

### Summoning and dismissing touch keyboard

By default, there is a touch keyboard button on the bottom of the screen, and unless one is dealing with an edit area, this button must be tapped to bring up the touch keyboard. By doing a four finger flick right, one can summon or dismiss touch keyboard from anywhere. NVDA does this by looking for the touch keyboard button through object navigation emulation, and once found, activating it.

### Touch typing

Unlike most controls where one must double tap to activate them, NVDA can be told to enter keys from touch keyboard by lifting one's finger. This mode is called "touch typing" as opposed to classic typing by object activation. NVDA performs touch typing by defining a "hover up" gesture that will allow typing using the touch keyboard.

In the past, it wasn't possible to toggle between these two modes, but in recent releases of the add-on, these modes can be toggled via add-on settings interface. With touch typing mode off, one must double-tap the desired key, but with this on, one can just lift a finger. This, along with some parts of add-on settings interface, is now part of NVDA.

## Touch passthrough

## Coordinate announcement beep

## Conclusion

