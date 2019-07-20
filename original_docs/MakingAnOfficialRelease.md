# Making an Official Release

The following instructions are for the release manager and detail how to make an official release.

## Betas
* Ensure beta branch has required changes:
  - Choose a point where master is healthy (all checks passing and no known regressions)
  - Merge master into beta
* Ensure these changes have had some alpha level testing.
  - The most recent (significant) change on beta should have had at least one week of alpha testing.
* Tag beta1. E.g. release-2019.1beta1.
  - ?? command line or via Github new release url (with pre-release)?
  - beta will now show up on the snapshots page
  - the auto update system will start offering it to those checking for betas
* Periodically look at recent issues filed, specifically looking for those with `p1`, `crash` or `appcrash` labels.
* Periodically look for PRs based on beta and ensure they are reviewed then merged or rejected.
  - As PRs based on the beta branch are merged, periodically tag further betas.
* After the final beta, [call a translation freeze](https://github.com/nvaccess/nvda/wiki/StartingTranslationFreeze) for 2 weeks. No more commits should be made to the beta branch at this time.

## Release candidates
* Ensure it is safe to release an rc by looking at recent issues filed, specifically looking for those with p1, crash or appcrash labels.
* If this is rc1, update translations:
    1. Log into exbi and su to nvdal10n.
    2. `cd ~/mr/mainNVDACode`
    3. `mr up`
    4. `cd ../srt`
    5. `mr up`
    6. `mr svn2nvda`
* If this is rc1, reset the rc branch to beta. Otherwise, merge rc into beta if necessary.
* For all other RCs, look for any prs based on rc, and review and approve/merge or reject them.
* Create an annotated tag for the release with a "release-" prefix; e.g. release-2016.1rc1.
* This will start an AppVeyor build, so wait for the build to complete. As part of this, the release will be staged.
* Publish the staged release. On exbi, su to the nvaccess user and run `nvdaRelease`
* If this is an rc, make a blog post on www.nvaccess.org, placing it in the Development category. It should never be placed in the News category.
    * Use a previous blog post as a base.
    * If this is not the first pre-release, include a list of changes since the last pre-release.
* Spread the word via the nvda-devel and nvda-translations lists and Twitter.
* Scan the launcher executable with [VirusTotal](http://www.virustotal.com/). Just submit the direct download URL.

If this is a final release:
* Mark the release milestone as done on GitHub.
* Change the milestone set for issues and pull requests automatically closed by GitHub to the next release:
    1. Get the milestone id for the new release. The easiest way to do this is to go to https://github.com/nvaccess/nvda/milestones and look at the link URL for the relevant milestone. The number at the end is the id.
    2. On exbi, edit ~nvaccess/data/nvaServer.conf.
    3. In the `[nvdaGithub]` section, change the value of `autoCloseMilestone` to the milestone id obtained in step 1.
    4. Reload uwsgi so the change takes effect: `sudo systemctl reload uwsgi`
* Make a blog post on www.nvaccess.org in the Releases category.
* Post on Facebook.
* Post to the NV Access News email list.
* If it hasn't been done already, prepare for the next version (after the one just published) in master:
    1. In `source/versionInfo.py`, update the `version_year` and/or `version_major` variables for the next version. If the next version is the first version for that year (e.g. 2018.1), also update `copyrightYears`.
    2. Add a heading for the next version in `user_docs/en/changes.t2t`.