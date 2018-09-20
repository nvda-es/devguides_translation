This document outlines rationale and steps for moving NVDA from Python 2.7 to 3.x.

IMPORTANT: this document is a draft document that can change periodically.

## Background

Python is one of the popular programming languages for various projects. Its ease of learning, extensive standard library modules and third-party extensions, as well as extensive documentation and clear syntax makes it an ideal choice for scripting.

Currently there are two major branches of Python: 2.x, released in early 2000's, and 3.x, first released in 2008. At first glance, Python 3 may seem similar to Python 2, but there are numerous deeper differences, including extensive Unicode support in Python 3, module renames and so on.

## Rationale

When NVDA began in 2006, it used python 2.4. Over the years, NvDA and its add-ons were written in Python 2.7. By moving to Python 3, NVDA project seeks to provide improvements in Unicode support, improved performance in various operations and other benefits, which goes beyond just the screen reader.

## Advantages of moving to Python 3

* Better Unicode support, thus leading to improved internationalization efforts.
* Using newer techniques for screen reading purposes.
* Major overhaul of NVDA's code base.

## Drawbacks of moving to Python 3

* Many add-ons not updated will no longer work.
* Renamed modules.
* Being careful about syntax and internal differences.

## Transition workflow

The following is a roughh overview of Python 2 to 3 transition for NVDA screen reader. As this is in draft stage, this is subject to change.

### Notable issues and solutions:

* Renamed modules in Python 3 such as _winreg -> winreg, SocketServer -> socketserver, Queue -> queue and so forth.
	* Try using Python 3 version before falling back to Python 2 names.
	* For certain modules (especially those written in C), make sure new modules won't break functionality.
* Reorganized modules in Python 3, including urllib and io.
	* Try loading specific attributes from reorganized modules.
* Absolute versus relative imports, especially when aliasing is involved (imports of the form 'from mod import *", observed mostly in app modules).
	* Use relative imports of the form "from .mod import attr".
* Replacement of some private attributes of logging module.
	* These should be changed on a case-by-case basis.
* Inability to print a meaningful log text to log file.
	* Investigate streaming/file handler/redirection issue.
* Use of "async" in Python 3, which affects nvwave.playWaveFile(async=True) as this raises syntax error.
	* Rename the keyword to "asynchronous".
* Division differences (/ versus //), most notably in nvwave.WavePlayer and manipulating mouse cursor.
	* Standardize around floor division (//) for integer values, regular division (/) for floats.
* Bytes versus strings caused by encoding.
	* Try unifying under Unicode.
	* This is pronounced when working with C functions (Espeak DLL, for example) where ANSI strings are expected by C functions but Python prefers Unicode.
* Removed and incompatible modules, including new.instancemethod.
	* Either find a Python 3 equivalent, or use built-in Python features.
	* Same can be said about dependencies (txt2tags, for example).
* Provide __hash__ method for classes implementing __eq__ method (NVDAObjects.NVDAObject, for instance).
	* This is required due to hash randomization in python 3.3 and later.
	* One of the simplest solutions is to use the parent object's __hash__ method (__hash__ = parentClass.__hash__).
* Object methods of the form _get_property does not work, noticeable when trying to set initial synthesizer, braille display, focus object and so on.
	* Caused by metaclass syntax differences between Python 2 and 3.
	* Use metaclass specifier of the form "metaclass=someclass".
* Incompatible dictionary methods.
	* dict.has_key(key): use "key in dict".
	* dict.iter*: use attributes directly (e.g. "dict.items()" instead of "dict.iteritems()").
* No more unichr.
	* Standardize around "chr".

### Needed dependencies:

* Python 3.7.x 32-bit
* Visual Studio 2017 (Community, Professional, Enterprise)
* Windows 10 SDK (build 17134)
* wxPython 4.0.3 for Python 3.x
* Six 1.11.0
* SCons 3.0.1
* comtypes 1.1.7
* Pywin32 extensions build 223 for Python 3.x
* pyserial for Python 3.x
* Configobj 5.1.0
* Any other dependencies advertising support for Python 2.x in one package or a separate release for Python 3.x
* A replacement for py2exe for binary distribution
* A replacement for txt2tags for generating documentation

### Before transition:

Start date: September 17, 2018 (tentative designation)

1. An NVDA version with wxPython 4 must be released. This is needed, as wxPython 4 supports Python 3, which is a stepping stone for Python 3 transition.
	* Requirement met on September 17, 2018 with release of NVDA 2018.3.
2. Source code level dependencies must be satisfied. This includes not only wxPython 4, but also ConfigObj, Comtypes, Pyserial, Pywin32 and others.
	* Requires editing Git submodule config.
3. Transition issues must be researched and documented (see above for known issues and proposed workarounds). Use "python 3" label.
	* As of September 20, 2018, at least 15 issues were identified, along with several pull requests.
4. If needed, create pull requests dealing with pre-transition workflow such as making NVDA source code Python 2 and 3 aware (imports, for instance).
	* As of September 20, 2018, at least one transition related pull request was submitted and merged into master branch.

Ideal completion: between NVDA 2018.4 and 2019.1 releases (tentatively by March 31, 2019)

### Transition:

Start date: TBD

1. A group of developers (code contributors, add-on developers, Python programmers outside of NVDA project and others) should work on transforming NVDA's source code to Python 3.
	* Do not run 2to3 and tell the script to replace files, as further tweaking is required for some files.
	* For each transformation iteration, test the source code to make sure features are identical (or almost identical) with older NVDA releases.
2. Issues related to transition must be documented.
	* Issues must be labeled as "Python 3" in GitHub.
	* If needed, proposed solutions and workarounds should be documented in the issue tracker.
3. Source code developers must test NVDA and add-ons to make sure no major issues are encountered while working on python 3 transition. During this phase, binary builds will not be released until the below condition is met.
	* Gather dependencies and make sure they are compatible with Python 3.
	* Try running SCons under Python 3 to make sure source code is prepared.
	* If features are working, compare it against latest stable NVDA release in hopes of catching regressions.
4. A suitable binary distribution packager must be found, tested, and documented. A series of binary builds must be created to make sure the combination of NVDA's own python 3 code, dependencies, binary packagers, and others work seamlessly.
	* Py2exe was considered, but it does not support Python 3.7.
	* A promising alternative is cx_freeze.
5. Members of the public should be invited to test a series of try builds meant to test transition work, test add-ons, documentation purposes, community outreach and other steps.

Estimated completion: four to six months after pre-transition steps are completed.

### After transition:

Start date: TBD

1. A beta of NVDA powered by python 3 must be released.
2. Members of the public should provide beta-level feedback.
3. Add-on developers are asked to start porting their add-ons to Python 3.
4. A stable version of NVDA powered by Python 3 is released.
5. Post-transition evaluation should take place, including documenting issues found during field testing, more community outreach and other activities.

Estimated completion date: no later than twelve to fifteen months after pre-transition activities are completed.

## Transition progress

1. Before transition (in progress):
	1. July 17, 2018: NVDA alpha snapshot powered by wxPython 4.0.3 was released.
	2. August 17, 2018: NVDA 2018.3 beta 3, the first beta release powered by wxPython 4.0.3, was released.
	3. August 21, 2018: alpha snapshots include Python 3 import edits. Source code changed to use Python 3 module names in most cases.
	4. September 17, 2018: NVDA 2018.3 powered by wxPython 4.0.3 released, with a follow-up release (2018.3.1) 48 hours later.
2. Transition: Not yet begun.
3. After transition: not yet begun.

## Notes for various audiences

### For code contributors:

* Document potential and actual issues when working with Python 3, including changed modules, attribute name changes, internal changes and so on.
* When importing a built-in Python module, use try/except when importing modules.
	* Try importing Python 2 names as Python 3 name, switching to Python 3 version when Python 2 module is not found or renamed.
	* See NVDA source code for implementation steps.
	* This is for work prior to transition. During transition, Python 3 import should be attempted first.
* Issues should be labeled as "python 3".
* Pull requests should be based on master branch unless specified by lead developers.
* Try using branch name of the form "py3*" where "*" denotes Python 3 feature e.g. py3socketserver for changes to socket server module.
* If working with built-in Python modules, be sure to test your code via Python 2.7 and 3.7 interpreter before making changes to NVDA source code.
	* Create a standalone script that'll use features from Python 2 and/or 3.
	* After testing this script and if it works in Python 3, make changes to NVDA source code and add comments regarding differences between Python 2 and 3.
	* Source code should target both Python 2 and 3 unless the pull request is submitted during active transition period.
* Edit this page whenever major changes are committed to master branch or pull request is merged, including import changes and such.

### For add-on developers:

* Try using Python modules that are known to be compatible with both Python 2 and 3.

### For testers:

Nothing yet, as transition hasn't begun.

### For translators:

Nothing yet.

### For users:

nothing yet.

### For organizations:

* Stay informed on Python 3 transition workflow.

### For Python community:

* During pre-transition period, please help NVDA project spot potential issues with Python 3 transition so they can be noted.
* During transition, please help write and test Python 3 code and provide additional comments.
