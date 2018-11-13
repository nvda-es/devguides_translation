# Translating using the automatic workflow process
This page describes the process of translating NvDA and related files using the automatic workflow process. For more information about the overall translation process, please read the translate intro page.

The automatic workflow process consists of receiving translation files, working on your translations, then submitting your translations to the translations server. This is done via a version control system called Subversion (SVN). From time to time, you'll receive new translations (along with new translation notices via email or Twitter( optional; follow "@SRT_" for tweets), and your translations are included in NVDA periodically so you can test your translations.

Note that you need to keep the translations up to date and test your translation work to make sure it works as intended. Also, read the release process document to remind yourself about release dates.

The workflow details are described below.

## Creating an account

To begin the workflow process, start by subscribing to the NVDA translations mailing list and request an invitation to join the workflow. Once you receive your [assembla http://www.assembla.com] invitation, you can proceed by creating a username/password so that you can use the svn server. Once you are logged in, you need to accept the invitation to the screenReaderTranslations team. After that, you don't need to come back to the website.

## Download and install Subversion

Currently we recommend Tortoise svn. Download it from http://tortoisesvn.net and install it.

The default TortoiseSVN settings and properties are fine, so no need to change anything.

## First time checkout (To download the repository)

To checkout the screenreader translations repository, create a directory e.g. named Translations, right click on it and select "SVN Checkout..." from the context menu. Copy and paste the following url into the repository url edit box:  
`http://subversion.assembla.com/svn/screenReaderTranslations`

You can see that it is successful when the last line that it printed says something like `Completed; Path: At revision: 1234`

## Repository structure

The layout of the repository is as follows:

- Folders of two character language codes (such as es for Spanish, fr for French), as used by nvda, contains all the translation documents for this language.
- scripts: the scripts that are run on the server, should generally not be changed.
- some t2tconf files, standard config files that should not need to be changed.

Each language directory contains:

- add-ons, the translatable messages for various add-ons (if enabled for your language).
- changes-newRevisions, directory containing updates that need to be translated for the changes.t2t (read only).
- userGuide-newRevisions, directory containing updates that need to be translated for the userGuide.t2t (read only).
- symbols-newRevisions, directory containing updates that need to be translated for the symbols.dic (read only).
- changes.t2t, localized list of changes (you should edit).
- changes.html, automatically generated html from t2t, so that you can check your syntax.
- userGuide.t2t, localized manual (you should edit).
- userGuide.html, automatically generated html from your t2t, so that you can check your syntax.
- userGuide-structureDifferences.txt, automatically generated diffrence between the english user guide statistics, and the localized user guide stats (very useful).
- nvda.po, the nvda interface file, new messages from pot are automatically merged, and you will be sent an email (or a tweet) when there are new messages to be translated.
- characterDescriptions.dic, your localized character descriptions file (you should edit).
- symbols.dic, your localized symbols file (you should edit).
- Settings, various meta information to help the automated translation system, also used to indicate when you want to translate a specific addon.



## Workflow

To minimize merge problems, and letting the automated system work 
effectively it is strongly recommended that you:

- SVN update before you start working.
- SVN Commit when you finish working with a section.

The workflow is something like this:

1. You receive an email telling you that nvda.po has been updated, and it will tell you how many messages are untranslated, and how many are fuzzy.
1.1 svn update to get the modifications
1.2 Localize the new messages/fuzzy messages.
1.3 Commit, in the commit message you say if the work was finished or not.
2. You receive an email (or a tweet) telling you that there are new revisions for the changes or userGuide documents to be translated
2.1 You svn update, you find one new directory for example 10289 in changes-newRevisions.
2.2 Inside 10289 you will find the changes.t2t, differences.txt, wordDifferences.txt and log.txt
2.3 differences.txt will show you exactly what line has been added/changed/removed.
2.4 if your localization is complete, the line numbers of each difference block should be close to  where you need to do your changes.
2.5 If differences.txt showed you a line that was modified, and it isn't easy to see what changed, (for example an inserted punctuation mark, or corrected spelling) you can see the word by word change by looking inside wordDifferences.txt.
2.6 log.txt, sometimes helpful to see the commit message from nvda authors, so it is provided in case it is useful.
2.7 When we finished with all the differences blocks for 10289, we check to make sure that nothing has been missed (see svn diff, svn status)
2.8 We svn commit, and in the message we say we completed the translation for 10289.


## Useful svn commands

### Download new changes from the server

To update the repository simply select the Translations folder in your explorer right click on it and activate SVN update.
The last line of the output window should be something like updated to revision 1234.

The other lines will show a list of files that have been effected.


        added file1.txt # meens that file.txt has been added to svn, and you are getting your copy.
        updated file2.txt # means that file2.txt has been updated
        deleted file3.txt # means that someone removed the file and svn is also removing your copy of the file.
        g file4.txt # means that you have changed the file , and it was also changed by someone else, but svn was happy merging the changes.
        c file5.txt # means that you have modified the file and it has been  modified by someone else, but svn could not automatically merge, this causes a problem, so ask for help if you get it.

### Committing (sending the modifications to the server)

If you translated new revisions, changed userguide and so on you can commit the changes by right clicking on your language code
inside the translation folder and select SVN commit from the menu.

In the dialog you should write a Commit message with your language code and a description of the work that was done.
You can check/uncheck the files to be committed.
Changed files are checked automatically.
If you deleted a file or folder in windows, 
by default it is unchecked in this dialog, so you have to check it for it to be deleted from the repository on the server.

### unintended modification to file

If you deleted a file by mistake or something like that you can revert the changes by right clicking on the Translations folder, and select TortoiseSVN -> revert out of the menu.


## missing info

If you have any tips or additional info please update this page.