# -*- coding: utf-8 -*-
documentation = [
_(u"""# Espeak-ng submodule"""),
"",_(u"""The submodule contained in the espeak directory is a cross platform open source speech synthesizer."""),
"",_(u"""### Background"""),
_(u"""The main authority on build requirements should be `<nvda repo root>/include/espeak/Makefile.am`."""),
_(u"""The `*.vcxproj` files in `<nvda repo root>/include/espeak/src/windows/` can also be considered,"""),
_(u"""however these are not always kept up to date."""),
"",_(u"""We don't use the auto make files or the visual studio files, we maintain our own method of building espeak."""),
_(u"""Modifications will need to be made in `<nvda repo root>/nvdaHelper/espeak`"""),
_(u"""* `sconscript` for the build process."""),
_(u"""* `config.h` to set the eSpeak-ng version that NVDA outputs to the log file."""),
"",_(u"""### Doing the update"""),
"",_(u"""1. Start from a clean branch off of NVDA `master`"""),
_(u"""   1. Check out the latest NVDA `origin/master` and create a new branch."""),
_(u"""   1. Do a git clean to ensure the working directory is clean."""),
_(u"""1. Ensure submodules are up to date"""),
_(u"""   1. Synchronize submodules with `git submodule sync`"""),
_(u"""   1. Update submodules with `git submodule update --init --recursive`"""),
_(u"""1. Checkout the new eSpeak-ng revision to try."""),
_(u"""   1. Change to the `include/espeak/` directory"""),
_(u"""   1. Do `git fetch` to get the latest from the espeak-ng repo"""),
_(u"""   1. Do `git checkout origin/master` or whichever espeak-ng ref you wish."""),
_(u"""1. Look at changes in `Makefile.am` and update our build."""),
_(u"""   1. Diff `Makefile.am` with the previously used commit of espeak."""),
_(u"""   1. Some modules are intentionally excluded from the build."""),
_(u"""      If unsure, err on the side of including it and raise it as a question when submitting a PR."""),
_(u"""   1. Modify the `<nvda repo root>/nvdaHelper/espeak/config.h` file as required."""),
_(u"""1. Update our record of the version number and build."""),
_(u"""   1. Change back to the NVDA repo root"""),
_(u"""   1. Update the package version in `<nvda repo root>/nvdaHelper/espeak/config.h`"""),
_(u"""      - Compare to espeak source info: `<nvda repo root>/include/espeak/src/windows/config.h`."""),
_(u"""   1. Update NVDA `readme.md` with espeak version and commit."""),
_(u"""   1. Build NVDA"""),
_(u"""1. Run NVDA (set eSpeak-ng as the synthesizer) and test."""),
_(u"""1. Ensure that the log file contains the new version number for eSpeak-NG"""),
"",_(u"""### Troubleshooting"""),
"",_(u"""If python crashes while building, check the log."""),
_(u"""If the last thing is compiling some dictionary try excluding it."""),
_(u"""This can be done in `<nvda repo root>/nvdaHelper/espeak/sconscript`."""),
_(u"""Remember to report this to the eSpeak-ng project."""),
"",_(u"""If the build fails, take note of the error, compare the diff of the `Makefile.am` file and mirror """),
_(u"""any changes in our `sconscript` file."""),
"",_(u"""### Known issues"""),
_(u"""Due to problems with emoji support (causing crashes), emoji dictionary files are being excluded"""),
_(u"""from the build, they are deleted prior to compiling the dictionaries in the"""),
_(u"""`<nvda repo root>/nvdaHelper/espeak/sconscript` file."""),
"",]