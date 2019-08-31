# Making an Official Release

The following instructions are for the release manager and detail how to make an official release.

## Starting the beta
* Decide which commit to start the beta from.
  - Generally master should be healthy (all checks passing and no known regressions).
  - The most recent (significant) change should have had at least one week of alpha testing.
* Merge this commit into beta
* Create a new pre-release with the [Github new release page](https://github.com/nvaccess/nvda/releases/new)
  - Tag Version example: `release-2019.2beta3`
  - Target: `beta`
  - Release Title example: `Release 2019.2beta3`
  - No description necessary for first beta, subsequent betas can describe important additions / removals.
  - Ensure option "This is a pre-release" is checked.
  - The tag must have a `release-` prefix.
  - This creates a new annotated tag. E.g. release-2019.2beta3
  - beta will now show up on the snapshots page
  - Auto update system will start offering it to those checking for betas
* Do a review of the `user_docs/en/changes.t2t` file.
  - Ask for a second review.

## During the Beta period
* Periodically look at recent issues filed, specifically looking for those with `p1`, `crash` or `appcrash` labels.
* Periodically look for PRs based on beta and ensure they are reviewed then merged or rejected.
  - As PRs based on the beta branch are merged, periodically tag further betas.

## End of Beta period
* After the final beta, [call a translation freeze](https://github.com/nvaccess/nvda/wiki/StartingTranslationFreeze) for 2 weeks. No more commits should be made to the beta branch at this time.

## Second translation freeze
Normally not required, however, if it is discovered that translations need to be updated after the translation freeze has started/completed then:
* Ensure `beta` has the changes requiring re-translation.
* Re complete the steps in calling a translation freeze.
* Send an email to the translation mailing list describing the need for new changes and deadline.
* After translation freeze, 

## Release candidates
* Ensure it is safe to release an RC.
  - Looking at recent issues filed, specifically looking for those with `P1`, `crash` or `appcrash` labels.
* If this is `RC1`, update translations:
    1. Log into exbi and su to nvdal10n.
    2. `cd ~/mr/mainNVDACode`
    3. `mr up`
    4. `cd ../srt`
    5. `mr up`
    6. `mr svn2nvda`
  - Note, this updates `beta` with the new translations.
* Update the `rc` branch
  - For RC1, reset the `rc` branch to `beta`
  - For RC1+, merge `beta` to `rc`
* Check for PRs against `rc`
  - look for any PRs based on `rc`, and review and approve/merge or reject them.
* Create a new pre-release with the [Github new release page](https://github.com/nvaccess/nvda/releases/new)
  - Tag Version example: `release-2019.2rc1`
  - Target: `rc`
  - Release Title example: `Release 2019.2rc1`
  - No description necessary for first RC, subsequent RCs can describe important additions / removals.
  - Ensure option "This is a pre-release" is checked.
  - The tag must have a `release-` prefix.
  - This creates a new annotated tag. E.g. release-2019.2rc1
* Wait for the appVeyor build to complete.
  - Tagging the release triggers this automatically.
  - As part of this, the release will be staged.
* Publish the staged release.
  - On exbi: `su` to the `nvaccess` user and run `nvdaRelease`
* Publicise the release.
  - Add a blog post on  www.nvaccess.org
    - Put post in the `Development` category. It should never be placed in the `News` category.
    - Use a previous blog post as a base.
    - If this is not the first pre-release, include a list of changes since the last pre-release.
  - Email nvda-devel list
  - Email nvda-translations list
  - Post to Twitter
* Scan the launcher executable
  - Use [VirusTotal](http://www.virustotal.com/). Just submit the direct download URL.

## Final release
* Create a new release with the [Github new release page](https://github.com/nvaccess/nvda/releases/new)
  - Tag Version example: `release-2019.2`
  - Target: `rc`
  - Release Title example: `Release 2019.2`
  - No description necessary for final release
  - Ensure option "This is a pre-release" is **not** checked.
  - The tag must have a `release-` prefix.
  - This creates a new annotated tag. E.g. release-2019.2
* Wait for the appVeyor build to complete.
  - Tagging the release triggers this automatically.
  - As part of this, the release will be staged.
* Publish the staged release.
  - On exbi: `su` to the `nvaccess` user and run `nvdaRelease`
* Close the release [milestone](https://github.com/nvaccess/nvda/milestones).
* Ensure the subsequent milestone is set on issues and pull requests now closed by GitHub automatically.
  1. Get the milestone id for the new release.
     - Go to https://github.com/nvaccess/nvda/milestones
     - Look at the link URL for the relevant milestone.
     - The number at the end is the id.
  2. On exbi, edit `~nvaccess/data/nvaServer.conf`
  3. In the `[nvdaGithub]` section, change the value of `autoCloseMilestone` to the milestone id obtained in step 1.
  4. Reload `uwsgi` so the change takes effect: `sudo systemctl reload uwsgi`
* Publicise the release.
  - Add a blog post on  www.nvaccess.org
    - Put post in the `Releases` category.
    - Use a previous blog post as a base.
  - Email nvda-devel list
  - Email nvda-translations list
  - Post to Twitter
  - Post on Facebook.
  - Post to the NV Access News email list.
* Ensure `master` version number and changes file are correct
    1. In `source/buildVersion.py`, update the `version_year` and/or `version_major` variables for the next version.
       - If the next version is the first version for that year (e.g. 2018.1), also update `copyrightYears`.
    2. Add a heading for the next version in `user_docs/en/changes.t2t`.
* Scan the launcher executable
  - Use [VirusTotal](http://www.virustotal.com/). Just submit the direct download URL.