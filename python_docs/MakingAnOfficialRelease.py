# -*- coding: utf-8 -*-
documentation = [
_(u"""# Making an Official Release"""),
"",_(u"""The following instructions are for the release manager and detail how to make an official release."""),
_(u"""See [the release process](https://github.com/nvaccess/nvda/wiki/ReleaseProcess) for details on timing."""),
"",_(u"""## Beta release (pre-release)"""),
_(u"""* Decide which commit to start the beta from."""),
_(u"""  - Generally master should be healthy (all checks passing and no known regressions)."""),
_(u"""  - In the past, the commit chosen should ensure that the most recent (significant) change should have had at least one week of alpha testing. This restriction has been relaxed somewhat to speed up the beta process. Lead developers should use their discretion to choose an appropriate branching point. If necessary, changes can be reverted or new changes added to the beta to address issues."""),
_(u"""* Create a branch from this commit, create a PR from this branch targeting beta"""),
_(u"""  - This allows for others to review the selected commit, and what will be included in the release"""),
_(u"""  - It makes reviewing the changes file easier."""),
_(u"""  - Do a review of the `user_docs/en/changes.t2t` file."""),
_(u"""  - Ask for a second review, use the PR and add a link to the diff for the changes file since the diff will be quite large."""),
_(u"""  - Once all approved merge to beta."""),
_(u"""* Create a [new annotated tag](#create-the-release--annotated-tag)"""),
_(u"""  - A beta doesn't need a pre-release entry on GitHub. Save that for RC and releases"""),
_(u"""* Wait for the [`appVeyor` build](https://ci.appveyor.com/project/nvaccess/nvda/history) to complete."""),
_(u"""* [Scan the launcher executable](#scan-the-build)"""),
_(u"""* [Publish the staged release](#publish-the-staged-release)"""),
_(u"""* [Publicize the release.](#publicize-the-release)"""),
"",_(u"""### During the Beta period"""),
_(u"""* Periodically look at recent issues filed, specifically looking for those with `p1`, `bug/crash` or `bug/app-crash` labels."""),
_(u"""* Periodically look for PRs based on beta and ensure they are reviewed then merged or rejected."""),
_(u"""  - As PRs based on the beta branch are merged, periodically tag further betas."""),
"",_(u"""## Translation Freeze"""),
_(u"""* End of Beta period, after the final beta."""),
_(u"""* [Call a translation freeze](https://github.com/nvaccess/nvda/wiki/StartingTranslationFreeze) for 2 weeks."""),
_(u"""  - No more commits should be made to the beta branch at this time."""),
"",_(u"""### Second translation freeze"""),
_(u"""Normally not required, however, occasionally to fix a critical issue requires changes to the translation strings after the translation freeze has started/completed then:"""),
_(u"""* Ensure `beta` has the changes requiring re-translation."""),
_(u"""* Re complete the steps in calling a translation freeze."""),
_(u"""* Send an email to the translation mailing list describing the need for new changes and deadline."""),
"",_(u"""## Release candidates (pre-release)"""),
_(u"""* Ensure it is safe to release an RC."""),
_(u"""  - Looking at recent issues filed, specifically looking for those with `p1`, `bug/crash` or `bug/app-crash` labels."""),
_(u"""* Check for PRs against `beta`."""),
_(u"""  - Use [search on PR page `is:pr is:open base:beta`](https://github.com/nvaccess/nvda/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aopen+base%3Abeta)"""),
_(u"""  - Look for any PRs based on `beta`, and review and approve/merge or reject them."""),
_(u"""* Check for PRs against `rc`, this is more likely after the first RC release."""),
_(u"""  - Use [search on PR page `is:pr is:open base:rc`](https://github.com/nvaccess/nvda/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aopen+base%3Arc)"""),
_(u"""  - Look for any PRs based on `rc`, and review and approve/merge or reject them."""),
_(u"""* If this is `RC1`, update translations:"""),
_(u"""    1. Log into `exbi`"""),
_(u"""    1. Switch user to nvdal10n: `sudo su nvdal10n`"""),
_(u"""    1. `cd ~/mr/mainNVDACode`"""),
_(u"""    1. `mr up`"""),
_(u"""    1. `cd ../srt`"""),
_(u"""    1. `mr up`"""),
_(u"""    1. `mr svn2nvda` **Note:**"""),
_(u"""        - This may take a few minutes"""),
_(u"""        - Watch for errors such as `unable to push`."""),
_(u"""    1. `exit` To return to your own user."""),
_(u"""    - **Note:** This updates `beta` with the new translations."""),
_(u"""* Locally, update the `rc` branch and push to GitHub"""),
_(u"""  - For RC1, reset the `rc` branch to `beta`"""),
_(u"""  - For RC1+, merge `beta` to `rc`"""),
_(u"""* Create a [annotated tag](#create-the-release--annotated-tag)"""),
_(u"""* Create a [new pre-release on GitHub](#convert-annotated-tag-into-a-gitHub-release)"""),
_(u"""* Wait for the [`appVeyor` build](https://ci.appveyor.com/project/nvaccess/nvda/history) to complete."""),
_(u"""* [Scan the launcher executable](#scan-the-build)"""),
_(u"""* [Publish the staged release](#publish-the-staged-release)"""),
_(u"""* [Publicize the release.](#publicize-the-release)"""),
"",_(u"""## Final release"""),
_(u"""* Create a [annotated tag](#create-the-release--annotated-tag)"""),
_(u"""* Create a [new release on GitHub](#convert-annotated-tag-into-a-gitHub-release)"""),
_(u"""* Wait for the [`appVeyor` build](https://ci.appveyor.com/project/nvaccess/nvda/history) to complete."""),
_(u"""* [Scan the launcher executable](#scan-the-build)"""),
_(u"""* [Publish the staged release](#publish-the-staged-release)"""),
_(u"""* [Publicize the release.](#publicize-the-release)"""),
_(u"""* Close the release [milestone](https://github.com/nvaccess/nvda/milestones)."""),
_(u"""* Ensure the subsequent milestone is set on issues and pull requests now closed by GitHub automatically."""),
_(u"""  1. Get the milestone id for the new release."""),
_(u"""     - Go to https://github.com/nvaccess/nvda/milestones"""),
_(u"""     - Look at the link URL for the relevant milestone."""),
_(u"""     - The number at the end is the `id`."""),
_(u"""  1. Log into exbi"""),
_(u"""  1. Swap to nvaccess user: `sudo su nvaccess`"""),
_(u"""  1. Edit `~nvaccess/data/nvaServer.conf`"""),
_(u"""  1. In the `[nvdaGithub]` section, change the value of `autoCloseMilestone` to the milestone `id` obtained in step 1."""),
_(u"""  1. Save the file and `exit` to return to your user."""),
_(u"""  1. Reload `uwsgi` so the change takes effect: `sudo systemctl reload uwsgi`"""),
_(u"""* In NVDA source, ensure the `master` branch version number and changes file are correct"""),
_(u"""    1. In `source/buildVersion.py`, update the `version_year` and/or `version_major` variables for the next version."""),
_(u"""       - If the next version is the first version for that year (e.g. 2018.1), also update `copyrightYears`."""),
_(u"""    2. Add a heading for the next version in `user_docs/en/changes.t2t` if it is not there already."""),
"","",_(u"""## Create the release / annotated tag"""),
_(u"""* Checkout the version to release."""),
_(u"""  - `git fetch`"""),
_(u"""  - `git checkout origin/<branch>`"""),
_(u"""  - Where `<branch>` is:"""),
_(u"""    - For a beta: `beta`"""),
_(u"""    - For an RC: `rc`"""),
_(u"""    - For a release: `rc`"""),
_(u"""* Create a new annotated tag in git, and push to GitHub."""),
_(u"""  - Create tag: `git tag -a <tag name> -m \"<message>\"`"""),
_(u"""    - The tag must have a `release-` prefix. EG:"""),
_(u"""      - Beta: `release-2019.2beta3`"""),
_(u"""      - RC: `release-2019.2rc1`"""),
_(u"""      - Release: `release-2019.2`"""),
_(u"""    - The first line of the message should contain the name of the release. EG:"""),
_(u"""      - Beta: `Release 2019.2beta3`"""),
_(u"""      - RC: `Release 2019.2rc1`"""),
_(u"""      - Release: `Release 2019.2`"""),
_(u"""    - The message may contain extra information (after a blank line) relevant to this specific release."""),
_(u"""  - Push to GitHub: `git push origin <tag name>`"""),
_(u"""  - Tagging the release triggers a build on `appveyor` automatically, as part of this the release will be staged."""),
_(u"""  - The release will now show up on the snapshots page (under `beta` or `RC`)"""),
_(u"""  - Auto update system will start offering it to those checking for betas"""),
"",_(u"""## Convert annotated tag into a GitHub release"""),
"",_(u"""- Visit the [GitHub new release page](https://github.com/nvaccess/nvda/tags)"""),
_(u"""- Click on the tag menu button, shown as \"...\" and choose \"Create Release\""""),
_(u"""- Release Title example: `Release 2019.2beta3`, """),
_(u"""- No description necessary for first RC / Release"""),
_(u"""  - Subsequent RC / Release can describe important additions & removals."""),
_(u"""- For `RC`, ensure option \"This is a pre-release\" is checked."""),
"",_(u"""### Reasoning"""),
"",_(u"""GitHub \"releases\" are formatted differently, can include metadata such as 'pre-release' and can have binaries attached. In the future, we would like to move to a more automated system that creates this release from the appveyor script and attaches the binaries. Unfortunately GitHub releases don't create an \"annotated tag\" in git, as such the tag for the release does not have a date or message."""),
"",_(u"""## Scan the build"""),
_(u"""- Use [VirusTotal](http://www.virustotal.com/)."""),
_(u"""- Just submit the artifact download URL from `appveyor`"""),
_(u"""- Recently, using the appveyor URL has resulted in 1 (\"CRDF) of the 72 scanners reporting an issue."""),
_(u"""- Follow up by scanning with the NV Access URL, which the \"CRDF\" scanner does not flag as an issue."""),
"",_(u"""## Publish the staged release"""),
_(u"""- Connect to `exbi`"""),
_(u"""- Switch user to nvaccess: `sudo su nvaccess`"""),
_(u"""- Run `nvdaRelease`"""),
_(u"""  - This will confirm the file currently staged."""),
_(u"""  """),
_(u"""## Publicize the release"""),
_(u"""- Add a blog post on  www.nvaccess.org"""),
_(u"""  - Use a previous blog post as a base."""),
_(u"""  - Use a link to the file on NVAccess.org, appveyor build artifacts expire after 6 months."""),
_(u"""  - **For RC and Beta:** Put post in the `Development` category."""),
_(u"""    - Excluding the first pre-release, include a list of changes since the last pre-release."""),
_(u"""  - **For Final release:** Put post in the `Releases` category."""),
_(u"""  - It should never be placed in the `News` category."""),
_(u"""- Post to [nvda-devel list](https://groups.io/g/nvda-devel/post)"""),
_(u"""- Post to [nvda-translations list](https://groups.io/g/nvda-translations/post)"""),
_(u"""- Post to Twitter"""),
_(u"""- Post on Facebook."""),
_(u"""- Post to the NV Access News email list."""),
]