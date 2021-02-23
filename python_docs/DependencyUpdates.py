# -*- coding: utf-8 -*-
documentation = [
_(u"""IMPORTANT: draft document, subject to change without notice, guidance from NV Access superseeds this document."""),
"",_(u"""This document describes procedure to use when updating dependencies."""),
"",_(u"""## Background"""),
"",_(u"""NVDA project uses third-party modules for operations such as compiling NVDA from source code, speech output, user interface, and other tasks. Key dependencies include Python, wxPython, SCons, and Liblouis."""),
"",_(u"""As dependencies are updated from time to time, it is important for NVDA project to use recent versions of these dependencies. However, the community must consider factors such as stability, compatibility, and security when choosing dependencies and their versions."""),
"",_(u"""## General rules"""),
"",_(u"""* Dependency checks should be done at least once a year."""),
_(u"""* For critical dependencies such as Python (those that are required to build and run NVDA), updates should target year.1 (backwards incompatible) release."""),
_(u"""* For dependencies with predictable release schedule such as Liblouis, most recent public release should be attempted."""),
"",_(u"""## Specific dependencies"""),
"",_(u"""### Python"""),
"",_(u"""### wxPython"""),
"",_(u"""### eSpeak NG"""),
"",_(u"""### Liblouis"""),
"",_(u"""### Visual Studio and Windows SDK"""),
"",_(u"""## Other dependencies"""),
"",]