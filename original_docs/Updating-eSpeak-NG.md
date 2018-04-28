### Background
The main authority on build requirements should be `<nvda repo root>/include/espeak/Makefile.am`. The `*.vcxproj` files
in `<nvda repo root>/include/espeak/src/windows/` can also be considered, however these are not always kept up to date.

We dont use the auto make files or the visual studio files, we maintain our own method of building espeak. Modifications will need to be made in `<nvda repo root>/nvdaHelper/espeak`

* `sconscript` for the build process.
* `config.h` to set the eSpeak-ng version that NVDA outputs to the log file.

### Doing the update

1. Start from a clean branch off of NVDA `master`
	1. Check out the latest NVDA `origin/master` and create a new branch.
	2. Do a git clean to ensure the working directory is clean.
2. Ensure submodules are up to date
	1. Synchronize submodules with `git submodule sync`
	2. Update submodules with `git submodule update --init --recursive`
3. Checkout the new eSpeak-ng revision to try.
	1. Change to the `include/espeak/` directory
	2. Do `git fetch` to get the latest from the espeak-ng repo
	3. Do `git checkout origin/master` or whichever espeak-ng ref you wish.
4. Update our record of the version number and build.
	1. Change back to the NVDA repo root
	2. Update the package version in `<nvda repo root>/nvdaHelper/espeak/config.h` you can use `<nvda repo root>/include/espeak/src/windows/config.h` to double check this is what you expect.
	3. Do a build of NVDA
5. Run NVDA (set eSpeak-ng as the synthesizer) and test.
6. Ensure that the log file contains the new version number for eSpeak-NG

### Troubleshooting

If python crashes while building, check the log. If the last thing is compiling some dictionary try excluding it. This
can be done in `<nvda repo root>/nvdaHelper/espeak/sconscript`. Remember to report this to the eSpeak-ng project.

If the build fails, take note of the error, compare the diff of the `Makefile.am` file and mirror any changes in our `sconscript` file.

### Known issues
Due to problems with emoji support (causing crashes), emoji dictionary files are being excluded from the build, they are deleted prior to compiling the dictionaries in the `<nvda repo root>/nvdaHelper/espeak/sconscript` file.