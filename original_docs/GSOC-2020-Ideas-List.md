## Introduction
As a part of the Google Summer of Code application process, NV Access is required to provide a project ideas list, which will help students as they plan and write their project proposals.
The [NVDA project](https://github.com/nvaccess/nvda/) currently has more than 2000 [open issues](https://github.com/nvaccess/nvda/issues/) on Github and will consider project proposals on any of them assuming the size and complexity is suitable for GSOC, please get in touch to discuss.
However, the following list are just some of the higher priority issues students may wish to consider.

Please direct any questions about these ideas to the NV Access GSOC mentors:
* Michael Curran <mick@nvaccess.org> (@michaeldcurran on Github)
* Reef Turner <reef@nvaccess.org> (@feerrenrut on Github)

## Ideas

### Improve stability of NVDA's audio output
[Related issues](https://github.com/nvaccess/nvda/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+label%3Aaudio)

#### The problem
NVDA outputs audio (including sounds and speech from most speech synthesizers) via the [Windows  Multimedia](https://docs.microsoft.com/en-gb/windows/desktop/Multimedia/waveform-functions) (winMM) API.
Some users (especially those using USB audio hardware) report a short chunk of audio being cut off either at the beginning or the end of speech. This may be caused by the fact that NVDA opens and closes the audio device for every speech utterance. It is possible that some audio drivers take slightly longer to open the device and drop some initial blocks. Similarly, when closing the device, some audio hardware may throw away the final blocks, rather than ensuring they have been played before closing. 
#### Implementation
We could consider keeping the audio device open for several seconds after speech finishes so that all audio is played, and so that the audio device does not have to be opened again if more speech is coming soon. We could also add a few milliseconds of silence to the start of the audio when first opening the device, to ensure that the device is truly ready when NVDA starts to speak.
We could also consider looking at using newer audio APIs available in Windows 7 and above, as this is now the minimum Windows version required by NVDA.
There is a possibility that several system crashes reported by users may be due to NVDA opening and closing the audio device too aggressively. Similarly, some users on low-end hardware report general lag and bad responsiveness. This may possibly be due to the  audio driver taking time to open the device for all speech utterances.
We also may have multiple code paths opening, writing to and closing the audio device at the same time. E.g. the tones module for beeps, may hold the audio device open all the time. It may be an idea to somehow integrate all this so that audio only goes through one final code path that serializes access to the audio device.
There are several locks in place currently, but this should be reviewed.
See the [nvWave](https://github.com/nvaccess/nvda/blob/master/source/nvwave.py) module in the NVDA source code.
#### Impact
Improving the audio in NVDA will improve both stability and performance of NVDA. NVDA will be able to be used efficiently on a wider range of audio hardware, which means NVDA can be used in more situations and possibly on lower-end devices, ensuring NVDA is helping the greatest amount of blind and vision impaired people possible.

### 64 bit NVDA
#### The problem
Although NVDA runs on both x86 and x64 variants of Windows, and there is some x64 c++ code for NVDA that runs in-process,  the main NVDA application is only itself x86.
As x64 processors can run x86 instructions natively, it is the current belief of NV Access that no major performance benefit would be seen by moving the NVDA application to x64. However, we are not 100% sure of this, and only doing it would answer the question once and for all.
There would however be one definite benefit to going x64, which is that it would resolve #7724 where NVDA cannot currently interact with 64 bit Java applications because there is no x86 Java Access Bridge client dll packaged with the x64 Java VM.
Some theoretical arguments to why going x64 may improve performance are:
- NVDA receives a great deal more events from the system than other standard applications. Perhaps there is a cost involved with constant thread context switching between architectures.
- NVDA is the gateway through which blind Windows users perceive the Operating System and its applications. If there is any performance cost for thread switching between architectures, users will notice, as it will affect anything they do.
#### Implementation
The majority of the work to make an x64 variant of NVDA is to change the build process to incorporate and use an x64 build of Python. However, there may be a lot of small assumptions in NVDA's code base about the architecture. Right now there are some specialized situations where NVDA must use specific 64 bit structures when using some Windows APIs to access 64 bit apps. This logic would need to be possibly reversed.

### Lazy population of Elements list
Related issue: #7197

#### The problem
To aide in locating information in large documents, NVDA provides an Elements List (a treevew of available elements in the document) which can be filtered by type or name. For instance, on a web page, the Elements List can be used to quickly search through a list of links.
However, depending on the size of the document, the Elements list can take a long time to become fully populated with content. While this is happening, the user is blocked from doing anything else in NVDA.
#### Implementation
We should consider rewriting the Elements List so that it only loads as many elements as actually fit in the treeview visibly on screen, and then either fetch more in the background or on demand when the user causes the treeview to scroll with the mouse or by moving past the first or last visible element.

### Performance measuring system for NVDA
We would like to gather information about the performance of NVDA's various subsystems within day to day usage, so that we can better understand the performance issues that some people are reporting, especially those on low-end hardware.
Collection and submission of performance data should be opt-in, and should not in itself cause negative impact on performance.
Information such as how often the core is woken up, how long a core cycle takes on average, number of accessibility API events are received, how long navigating to the next or previous line in a document takes etc.
At very least this data could be stored locally with the ability for the user to send it to NV Access manually. At best, this data would be sent directly to NV Access servers automatically, assuming the user has allowed this.

### Improve the UX of the NVDA updater
Related issues: [#2257](https://github.com/nvaccess/nvda/issues/2257), [#7451](https://github.com/nvaccess/nvda/issues/7451), [#9174](https://github.com/nvaccess/nvda/issues/9174) 

#### The problem
Currently if there is an update available for NVDA, a dialog comes to the foreground notifying the user. this can interrupt the user and or the user may miss it or even accidentally activate it. 
#### Implementation
We should consider providing a UX for updates similar to other software, that makes use of modern notification APIs such as toasts and the Windows 10 notification API.
Perhaps included in this work could be also improving the update process so that:
- Administrative access is no longer required to update NVDA (we could use a service like Mozilla products)
- Unpack NVDA in the background, so updating only takes as long as renaming a folder and registering some shortcuts etc. Rather than the user having to wait for all files to be copied.
 
### Customize order and inclusion of object and formatting information to speech and braille
 Related issues: #7232

#### The problem
When NVDA reports a particular control in speech or braille, it includes information such as the control's name, role (button, checkbox, slider etc), states (checked, pressed, collapsed etc), its value if it has one (100% for example), description, keyboard shortcut, position in group, and several other possible properties. 
The order in which NVDA reports these properties is hard-coded, and is roughly the same for both speech and braille.
We should consider allowing the user to customize the order in which this information is presented, and allow it to be configured separately for speech and braille.
 Perhaps some kind of template language could be used to represent the order, along with a suitable UI that could allow the average user to be able to insert, remove and reorder properties.
 This UI would have to allow separate configuring for both speech and braille, and may go as far as separate configurations for both browse mode and focus mode (i.e. reporting controls embedded in a document such as a link, verses a stand-alone control in a dialog).
Similar to reporting controls, NVDA reports many text formatting attributes. Again, currently the order of this information is hard-coded and is pretty much the same in both speech and braille. Example formatting attributes are font name, font size, attributes such as bold, italic and underline, font and background color, paragraph alignment and much more.
We should consider allowing the user to customize the order of this information, and allow them to configure it separately for both speech and braille.

### Integrate NVDA with the Windows Magnifier
In the 2019.3 release a framework for visual tools was added to NVDA, this could be extented with a Windows Magnifier integration. There are a number of NVDA users who use NVDA in conjunction with the [Magnifier built into Windows](https://support.microsoft.com/en-au/help/11542/windows-use-magnifier). We should consider a tighter integration between NVDA and the Windows Magnifier. Examples:
- Allow the user to configure all Magnifier settings directly from NVDA. This means they do not have to learn two different assistive programs, and their preferences can be saved in the same configuration.
- Synchronize the Magnifier with NVDA's focus / object navigation. I.e. if the user specifically navigates with NVDA, the Magnifier should follow along.
- Learn from the innovative ideas in the free [Glassbrick](https://www.glassbrick.org/) magnifier, and ensure that NVDA can offer the same if not better interaction and configurability.
 
### Improve performance of reading/navigating Microsoft excel by batching COM calls in process
Related issue: [#7348](https://github.com/nvaccess/nvda/issues/7348)
Note that much of this idea has already been implemented in NVDA, see pr #9257.
However, further work can be done to extend this to fetching of text formatting which is still slow.

#### The problem
NVDA provides broad support for reading and interacting with spreadsheets in Microsoft Excel. This support is implemented by using [Excel's COM object model](https://docs.microsoft.com/en-us/office/vba/api/overview/excel/object-model) in a cross-process fashion.
Partly due to the amount of information NVDA must fetch, and partly due to recent slowdowns in the object model itself, NVDA's access for Microsoft Excel is becoming slower, and in some cases  totally impractical. Although NV Access is working closely with the Excel team at Microsoft to rectify the recent slowdowns, and has in some cases improved performance in the last few months, we should definitely consider further actions we can take in NVDA to limit or batch object model calls in order to provide the best performance.
#### Implementation
Similarly to our [in-process support for Microsoft Word](https://github.com/nvaccess/nvda/blob/master/nvdaHelper/remote/winword.cpp), work has already begun to batch cross-process COM calls. we should consider fetching all possible information needed for a given cell in one call, via NVDA's in-process code in c++. While these calls are being made, we should also consider instructing Excel to pause [screen updating](https://docs.microsoft.com/en-us/office/vba/api/excel.application.screenupdating). 
Although all the work to run NVDA's in-process code in Excel already exists, we would need to still write the actual COM calls, plus come up with an appropriate serialized format in which to represent all the information for a given cell, for sending back to NVDA.
#### Impact
Many blind and vision impaired people use Excel either in their education or employment. Speeding up support for Microsoft Excel will allow NVDA users to be much more efficient at their work.
