IMPORTANT: draft document, subject to change without notice, guidance from NV Access superseeds this document.

This document describes procedure to use when updating dependencies.

## Background

NVDA project uses third-party modules for operations such as compiling NVDA from source code, speech output, user interface, and other tasks. Key dependencies include Python, wxPython, SCons, and Liblouis.

As dependencies are updated from time to time, it is important for NVDA project to use recent versions of these dependencies. However, the community must consider factors such as stability, compatibility, and security when choosing dependencies and their versions.

## General rules

* Dependency checks should be done at least once a year.
* For critical dependencies such as Python (those that are required to build and run NVDA), updates should target year.1 (backwards incompatible) release.
* For dependencies with predictable release schedule such as Liblouis, most recent public release should be attempted.

## Specific dependencies

### Python

### wxPython

### eSpeak NG

### Liblouis

### Visual Studio and Windows SDK

## Other dependencies

