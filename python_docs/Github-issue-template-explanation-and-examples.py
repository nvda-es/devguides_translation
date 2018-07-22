# -*- coding: utf-8 -*-
documentation = [
_(u"""# Creating new issues on the NVDA project"""),
"",_(u"""This page is meant to serve as an explanation for how to fill out [our Github issue template](https://github.com/nvaccess/nvda/blob/master/.github/issue_template.md)."""),
"",_(u"""The template uses github markdown, to provide formatting for headings, lists, quotes etc. If you are not familiar, please take some time to learn about [Github markdown](https://guides.github.com/features/mastering-markdown/)"""),
"",_(u"""**Warning**: In all but exceptional circumstances we require this template to be completed. Your issue will likely be closed if this template has not been followed."""),
"",_(u"""## Attachments / Images"""),
"",_(u"""It's important to include any files that are required to reproduce an issue. This might be a required file for an office suite, or a link to a code playground such as CodePen or JSFiddle, or perhaps a standalone HTML file. Github does not allow all [file types to be attached](https://help.github.com/articles/file-attachments-on-issues-and-pull-requests/), however, zip files are allowed, so you can always zip your file and attach that instead."""),
"",_(u"""### Logs"""),
_(u"""In most cases an NVDA log file is incredibly helpful when trying to understand/fix an issue, please remember to attach one. More [instructions are available on the wiki](https://github.com/nvaccess/nvda/wiki/LogFilesAndCrashDumps). If you are getting a crash dump file (nvda_crash.dmp) please also include it."""),
"",_(u"""### Screenshots"""),
_(u"""While we welcome **images/screenshots** to help explain a problem, be aware that many of the developers of NVDA are blind and will greatly appreciate this image being described in text. Most tools allow you to copy text out of them."""),
"",_(u"""## Tips"""),
_(u"""* Consider swapping to the preview tab in order to read through your issue at any stage to confirm the issue reads as expected."""),
_(u"""* If you have trouble following this template, or with the initial investigation that is required, please politely ask for assistance from the fantastic community of people on the [NVDA users mailing list](https://github.com/nvaccess/nvda-community/wiki/Connect#international-users-mailing-list-english)"""),
"",_(u"""## The template"""),
"",_(u"""At the start of the template there is a HTML comment block which points to this wiki page, it can be left in place and will not appear once the issue is saved. Feel free to delete it."""),
"",_(u"""After the HTML comment, you may provide a brief overview of the issue. Then fill in each of the following sections:"""),
"",_(u"""### Steps to reproduce:"""),
"",_(u"""This section should contain a list of the steps you take to demonstrate the problem. While you are working out the steps required, please make a copy of your [NVDA log to attach to the issue](https://github.com/nvaccess/nvda/wiki/LogFilesAndCrashDumps)."""),
"",_(u"""*Example:*"""),
_(u"""> 1. Open Chrome"""),
_(u"""> 1. Browse to www.google.com"""),
_(u"""> 1. Type \"Hello\""""),
_(u"""> 1. Press Enter"""),
"",_(u"""### Actual behavior:"""),
_(u"""This section should tell us what actually happens when these steps are taken."""),
"",_(u"""*Example:*"""),
_(u"""> An NVDA error sound is heard."""),
"",_(u"""### Expected behavior:"""),
_(u"""This section should tell us what you expect to happen when these steps are taken."""),
"",_(u"""*Example:*"""),
_(u"""> There should be no error sound, and the page should change to show the search results."""),
"",_(u"""### System configuration:"""),
"",_(u"""This section has several sub-sections. These are all about the system you are using when encountering the issue. If you are encountering the issue with multiple different configurations, please list them. This helps us to be able to reproduce the issue, or help us to investigate why this issue occurs for some users and not others."""),
"",_(u"""#### NVDA Installed/portable/running from source:"""),
_(u"""This tells us how you are using NVDA."""),
"",_(u"""*Example:*"""),
_(u"""> Installed"""),
"",_(u"""#### NVDA version:"""),
_(u"""The version of NVDA that you are using when demonstrating the issue. This can be copied from the about option, in the NVDA help menu."""),
"",_(u"""*Example:*"""),
_(u"""> next-15370,21fd217a"""),
"",_(u"""#### Windows version:"""),
_(u"""The version of Windows that you are using. You can copy this from the \"System Information\" application:"""),
"",_(u"""1. Press `Windows+r` to open the run dialog"""),
_(u"""1. Type `msinfo32` and press enter"""),
_(u"""1. From the \"System summary\" treeview item, press tab to get to the right pane."""),
_(u"""1. Press down arrow twice to get to \"Version\""""),
_(u"""1. Press `Control+C` to copy the version information."""),
"",_(u"""*Example:*"""),
_(u"""> Windows 10 Version 1607 Build 14393.1066"""),
"",_(u"""#### Name and version of other software in use when reproducing the issue:"""),
_(u"""Typically you can get this information from the \"About\" dialog of the software."""),
"",_(u"""*Example:*"""),
_(u"""> Chrome version: 67.0.3396.87"""),
"",_(u"""#### Other information about your system:"""),
_(u"""This is other information about your setup that you think might be relevant to us."""),
"",_(u"""*Example:*"""),
_(u"""> Running Windows 10 in a VM"""),
"",_(u"""### Other questions:"""),
_(u"""This section has sub-sections, asking about the basic investigation steps you may have completed. Please feel free to add more information here to tell us about what you have tried."""),
"",_(u"""#### Does the issue still occur after restarting your PC?"""),
"",_(u"""Restarting your computer will help to ensure that software is in a fresh state."""),
"",_(u"""#### Have you tried any other versions of NVDA?"""),
"",_(u"""Knowing whether this issue occurs in previous releases helps us to understand if this is a newly introduced issue, and gives us an indication as to whether it is a change in our software or others that has introduced the problem."""),
"",_(u"""*Example:*"""),
_(u"""> * NVDA 2018.1 - no error sound"""),
_(u"""> * NVDA 2018.2 - has error sound"""),
"","","",]