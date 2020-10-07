# Starting a Translatable String Freeze

Three weeks before the release is due (two weeks before rc1), beta should enter a translatable string freeze. These instructions are for the release manager and document the process for beginning this freeze.

* If you haven't already, make any final corrections to the What's New and add a release blurb.
* If there have been any changes in beta since the last automated merge to srt (Friday 00:05 AEST), translations should be merged to srt manually:
    1. Log into exbi and su to nvdal10n; e.g. `sudo su - nvdal10n`
    2. `cd ~/mr/mainNVDACode`
    3. Run: `mr up`
    4. `cd ~/mr/srt`
    5. Run: `mr up`
    6. Run: `mr mergePot`
    7. Run: `mr findRevs`
* Announce the freeze on the nvda-devel and nvda-translations email lists. Use the example below as a base, ensuring you edit all instances of the version number and dates:

    > Subject: Translatable string freeze for NVDA 2017.2
    >
    > Hi all,
    >
    > We have now entered the translatable string freeze for NVDA 2017.2.
    >
    > Translators, you have until UTC 00:00 on 22 May to ensure your translation is up to date in order for it to be included in NVDA 2017.2. Work submitted after this time will not be included in NVDA 2017.2.
    >
    > Thanks to everyone for their valuable work!