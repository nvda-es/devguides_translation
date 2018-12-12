# Adding a New Language to Ikiwiki

Following are instructions for adding a new language to the addons.nvda-project.org website, which uses Ikiwiki.

1. Edit the `ikiwiki.setup` file in the `ikiwiki-ctl` repository. The Git repository URL is: git@bitbucket.org:nvdaaddonteam/ikiwiki-ctl
2. Add a new entry under the `po_slave_languages` option for the new language, following the format of the other entries.
3. Save, commit and push.
4. Log into `exbi` and su to `nvdal10n`.
5. `cd ~/ikiwiki/ctl`
6. `git pull`
7. `ikiwiki --setup ikiwiki.setup --verbose`
