The following draft page provides an introduction into NVDA's braille framework. For more information about braille displays, read the page that describes the process of [Adding Support for a Braille Display](https://github.com/nvaccess/nvda/wiki/AddingSupportForABrailleDisplay).

## Basic introduction to Modules
NVDA"s braille framework depends on the following modules:

* [`braille.py`](https://github.com/nvaccess/nvda/blob/master/source/braille.py): contains the base of NVDA"s braille code, including the braille handler as well as a base braille display driver that all braille display drivers inherit from. Also, it contains classes for  regions, braille buffers and braille display gestures, described in greater detail below.
* [`brailleTables.py`](https://github.com/nvaccess/nvda/blob/master/source/brailleTables.py): contains definitions of liblouis braille tables used within NVDA.
* [`brailleInput.py`](https://github.com/nvaccess/nvda/blob/master/source/brailleInput.py): the code that is responsible for the processing of braille input and key presses from braille keyboards.
* [`bdDetect.py`](https://github.com/nvaccess/nvda/blob/master/source/bdDetect.py): contains definitions of detection data for braille displays and implements a Detector class that facilitates automatic detection of braille displays over USB or Bluetooth.
* [`hwIo.py`](https://github.com/nvaccess/nvda/tree/master/source/hwIo): contains classes that streamline thread safe communication with braille displays using HID, Serial or Bulk protocols.
* [`hwPortUtils.py`](https://github.com/nvaccess/nvda/blob/master/source/hwPortUtils.py): contains functions that ease detection of HID, USB or Serial based hardware.

## The `braille` module

### The `BrailleHandler` class
The `BrailleHandler` class is the playing point guard of the braille framework. It receives requests from NVDA's core to control what has to be shown on a braille display, thereby making use of underlying technology and classes, including BrailleBuffers and BrailleRegions. When braille is initialized using the initialize function, a single BrailleHandler is instantiated as braille.handler. Basically, the braille handler does the following:

* It keeps track of the current braille display in use and enables or disables automatic detection if appropriate.
* It keeps track of several braille settings, including tethering, focus context presentation, cursor blinking, message timeout, braille output tables, etc.
* it allows interaction with displays using gestures for scrolling and cursor routing
* it performs actions based on several NVDA events related to objects, including when an object gains focus or becomes the navigator object.

### The `Region` and `BrailleBuffer` classes
The `Region` and `BrailleBuffer` classes are strongly related to each other. A `Region` can be seen as the smallest entity within the braille framework, presenting information about an NVDA object. A BrailleBuffer can be seen as a box of regions that are relevant for the current focus object, navigator object or review position.

There are basically three types of regions:

1. `TextRegion`: A simple region that just contains some text and isn't related to an NVDA object.
 It can be used to show braille messages, such as those that are shown when retrieving the current time or date, the current battery status or when changing an NVDA setting using a gesture.
2. `NVDAObjectRegion`: A region that shows information about an NVDA object, such as its name (I agree), its role (checkbox or chk) and states (not checked or ⣏⣀⣹).
 Note that NVDAObjectRegions *do not** show the text within an edit control, such as a text editor.
3. `TextInfoRegion`: These regions contain the content of TextInfo objects. The position of the review cursor within screen review, the text shown at the caret in a text editor or the currently selected line within NVDA"s browse mode are all shown using a TextInfoRegion or one of its subclasses.

A `BrailleBuffer` is responsible for chaining several `Region` instances together. When viewing an object that has been selected using object navigation, the buffer usually contains one or two objects;; one NVDAObjetRegion for the object's properties and an optional TextInfoRegion to show the text within the object when it is a text control. When showing a focused object however, the buffer may also contain several objects that form the so called focus ancestry of an object.

The structure of a buffer is probably best described using an example.

1. Using the NVDA menu, go to `Preferences` > `Settings` and select the `Speech` category. Alternatively, you can press control+NVDA+v to open this category within the settings dialog.
2. Focus the synthesizer edit control that contains the name of the current synthesizer.
3. In this particular case, the braille buffer contains 4 regions:
 1. An NVDAObjectRegion for the dialog, represented by the text "'NVDA: Speech (normal configuration) dlg"
 2. An NVDAObjectRegion for the synthesizer grouping, represented by the text "'Synthesizer grp Alt+s"
3. An NVDAObjectRegion for the synthesizer text control, represented by the text "Synthesizer ro mln edt Alt+s"
4. A TextInfoRegion for the contents of the synthesizer text control, which contains the text "Windows OneCore voices"
 These regions or parts of the buffer form the raw text of the buffer: 'NVDA: Speech (normal configuration) dlg Synthesizer grp Alt+s Synthesizer ro mln edt Alt+s Windows OneCore voices

Note that this buffer is almost 200 characters in size and in braille characters, this might be even more, depending on your current braille table of use. However, a braille display may have only 40 braille cells. This is where NVDA makes a distiction between a braille buffer or a braille window. The braille window is the part of the buffer that is currently visible on your braille display. As you may expect, the braille window has a maximum size of the length of the current braille display. In the case that the braille window contains less characters, the braille display is padded up with spaces. You can change your position in a buffer with the scroll buttons on a braille display, in which case the position of the braille window is changed, effectively changing what is currently visible on your braille display.