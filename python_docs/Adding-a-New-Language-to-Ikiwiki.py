# -*- coding: utf-8 -*-
documentation = [
_(u"""# Adding a New Language to Ikiwiki"""),
"",_(u"""Following are instructions for adding a new language to the addons.nvda-project.org website, which uses Ikiwiki."""),
"",_(u"""1. Edit the `ikiwiki.setup` file in the `ikiwiki-ctl` repository. The Git repository URL is: git@bitbucket.org:nvdaaddonteam/ikiwiki-ctl"""),
_(u"""2. Add a new entry under the `po_slave_languages` option for the new language, following the format of the other entries."""),
_(u"""3. Save, commit and push."""),
_(u"""4. Log into `exbi` and su to `nvdal10n`."""),
_(u"""5. `cd ~/ikiwiki/ctl`"""),
_(u"""6. `git pull`"""),
_(u"""7. `ikiwiki --setup ikiwiki.setup --verbose`"""),
]