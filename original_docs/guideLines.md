# Add-on guidelines #

The following is a set of guidelines that current and potential add-on authors should use when writing add-ons:

## General ##

1. Use the addonTemplate from https://github.com/nvdaaddons/addonTemplate
2. Addon name should not contain "nvda", "plugin", "appmodule", "globalPlugin" as part of its name, the user should not have to worry about implementational issues.
3. Addon name should be of the form "name", or "firstSecond" or "first_second"
examples: "word", "dropbox", "extendedWinamp", "resourceMonitor" or "resource_monitor". Dashes in names are currently not supported by the automated system.
4. Make sure that your add-on is released under GPL license or an equivalent that is GPL compatible, as NVDA itself is GPL and add-ons are hosted by NVDA.

## Versioning ##

1. Use major dot minor revision, example: 1.0, 1.1 etc. A date-based versioning such as 2016.1 or 16.07 are also supported (termed continuous delivery).
2. When new functionality is added, update major revision, i.e. 2.0, 3.0. For date-based version, designate a version as a major version.
3. When making a release that has only translation updates, update the minor revision, 3.1, 3.2 etc. Making sure that the new languages are mensioned in a commit message. There is no need to add the new languages to the readme.md.
4. git tag the release, note special git push for tags.

## Release process ##

1. After releasing an add-on version, if you know that you will be making changes to both old and new major versions, use a separate maintenance branch for the old version (e.g. 1.x, 2.x, etc.) with the maintenance release committed from the old version branch. Then merge the old changes to the new major version. If continuous delivery/date-based versioning is in use, perform development from master.
2. After making a stable release (and generating the add-on installation package), update the version to indicate that its under development for the next version, i.e. 3.1-dev. Note this means that the version number should only be 3.0 for a few minutes, and should be changed to  3.1-dev to indicate new development. The version number can be changed from 3.1-dev to 4.0-dev if/when new features are added.
3. A stable release (such as 1.0, 2.0, 2.1, etc.) should be posted as a stable add-on, provided that there are no critical bugs reported within the past two weeks after the last commit. An add-on (or a version of an add-on) under active development and for which regular commits are made should be listed as a development add-on for testing by users.
4. Stable releases should be made no closer than 2 weeks apart, to allow translators to do their work, unless fixing a chritical/showstopper bug.
5. Announce the availibility of the new version on various NVDA mailing lists (e.g. NVDA add-ons list).
6. If possible, add-on authors should release the add-on and responsible for pulling in translations via translations workflow. For more information, see the [Make add-ons translatable](https://github.com/nvdaaddons/nvdaaddons.github.io/wiki/MakeAddonsTranslatable)) article.

## Coding Style ##

1. Indent with either 4 spaces or 1 tab. Tab-based indentation is strongly encouraged.
2. All messages presented to the user should be translatable (with some exceptions), if we are the creator of the message.
3. Messages containing multiple '%s' or %'d' or are of the form
"%(name)s .. %(name2)s" should be rewritten to _("{name1} .. {name2}").format(name1=v1, name2=v2)
4. Translatable messages should have a translator comment to explain where/when the message is presented, so that the translator can test the  message easily when s/he installs the addon. If the translatable string is similar to main NvDA messages, indicate this as well.
5. If your addon needs to store any configuration:
    - dont use:
    config_file = os.path.join(config.getUserDefaultConfigPath(),"addonName.ini")
    - do use:
    config_file = os.path.join(globalVars.appArgs.configPath,"addonName.ini")
6. Unless there is a good reason for it, it is recommended to use config.conf so add-on settings (particularly for global plugins) can be made available to configuration profiles.
7. When working on a new or modifying a major feature, create/use branches other than master branch, as it helps merging and code review (via pull request) process and to find bugs easily.

## Documentation and key bindings ##

1. If you are adding new keyboard commands as part of your add-on, be sure to consult NVDA Command Quick Reference and other community supported add-on commands before assigning a new command.
2. For NvDA 2013.3 or later: If you wish to categorize your keyboard bindings (for easier identification so the user can change it), either assign the same category as NVDA script categories (if your add-on enhances some parts of NVDA such as adding a shortcut to a preferences dialog) or create new categories if needed (if the add-on provides other features such as support for advanced features of a program).
3. Please provide a readme.md file listing changes between versions, shortcut keys (if any) and usage notes and other information, see one of the other git repos for examples.
4. Files addon/doc/*/readme.md should not be translated by hand and committed to the repository, but should be generated and committed from the translation system.
5. If you translate an addon to your language and commit to git, please inform your nvda translation maintainer for your language so that work is not duplicated, in any case it is better to keep translations on the translation system.

## Sharing and add-on reviews ##

1. If you haven't, subscribe to NVDA Add-ons list located at Groups.IO.
2. Request a basic review (license and copyright, documentation, basic user experience, security, etc.). When doing so, be sure to provide the link to the add-on source code along with installers if any.
3. If the basic review passes, you can declare the add-on stable or wait a while so you can work on addressing review comments before releasing a stable version. If you choose to wait, you have an option of releasing a development version for wider testing.
4. If the review does not pass, you are asked to address comments from reviewers. Once you address review comments, ask the reviewer to go over your add-on once more. This is done until the add-on passes basic review, and this is rare.
5. If your add-on passes basic review, you have an option of asking for a more thorough review. These may involve looking at add-on messages, GUI widget toolkit compatibility, potential bugs and so on. It is up to you to respond to comments on thorough reviews and address them when you have time.
