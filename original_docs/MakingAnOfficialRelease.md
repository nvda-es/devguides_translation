# Making an Official Release

The following instructions are for the release manager and detail how to make an official release.
See [the release process](https://github.com/nvaccess/nvda/wiki/ReleaseProcess) for details on timing.

## Starting a new dev cycle
* Create PR to set the branch off point **(merge commit - not squash merge)**
  - First create a new branch (eg `branchFor2020.3`) based on the master commit that should be used for the beta.
      - Using a separate branch is so that master can continue to move on without affecting the PR. 
      - The PR allows for others to review the selected commit, and what will be included in the release
      - The PR makes reviewing the changes file easier.
  - Do a review of the `user_docs/en/changes.t2t` file, but don't add highlights, see next step.
  - Ask for a second review, use the PR and add a link to the diff for the changes file since the diff will be quite large.
  - Deciding which commit to start the beta from:
    - This will be the branch off point for the new release.
    - Before the branch off happens (but after the previous "final" release), master can be merged into beta at any point.
    - After the branch of point master will move on and PR's required in this release should target the beta branch.
    - Generally master should be healthy (all checks passing and no known regressions).
    - In the past, the commit chosen should ensure that the most recent (significant) change should have had at least one week of alpha testing. This restriction has been relaxed somewhat to speed up the beta process. Lead developers should use their discretion to choose an appropriate branching point. If necessary, changes can be reverted or new changes added to the beta to address issues.
* Create a PR adding highlights for the release **(squash merge)**.
  - Based on `branchForX`
  - Targeting either `branchForX` or beta dependent on whether the branching PR has been merged yet. 
* Create a PR to move master on to the next release dev cycle **(squash merge)**.
  * [Add a new section to the change log](#new-section-in-changes-file).
  * [Update NVDA version in `master`](#update-nvda-version-in-master)
  * When merging [update auto milestone ID](#update-auto-milestone-id)
* Create a PR to update espeak, and create and issue on the [espeak-ng repo asking for a new release](https://github.com/espeak-ng/espeak-ng/issues/new). [See discussion](https://github.com/espeak-ng/espeak-ng/issues/792).
* If this is a 20XY.1 release, create a PR to update the Addon API `BACK_COMPAT_TO` version to match this version number for this release cycle.
  - This PR does not need be merged until branching for the beta of the 20XY.1 release.
  - The existence of the PR is intended to act as an early warning for add-on developers of the coming change.

## Beta release (pre-release)
* Create a [new annotated tag](#create-the-release--annotated-tag)
  - A beta doesn't need a pre-release entry on GitHub. Save that for RC and releases
* Wait for the [`appVeyor` build](https://ci.appveyor.com/project/nvaccess/nvda/history) to complete.
  - Consider writing a draft of the release post.
* [Scan the launcher executable](#scan-the-build)
* Create a [new pre-release on GitHub](#convert-annotated-tag-into-a-gitHub-release)
* [Publish the staged release](#publish-the-staged-release)
* [Publicize the release.](#publicize-the-release)

### During the Beta period
* Periodically look at recent issues filed, specifically looking for those with `p1`, `bug/crash` or `bug/app-crash` labels.
* Periodically look for PRs based on beta and ensure they are reviewed then merged or rejected.
  - As PRs based on the beta branch are merged, periodically tag further betas.

## Translation Freeze
* End of Beta period, after the final beta.
* [Call a translation freeze](https://github.com/nvaccess/nvda/wiki/StartingTranslationFreeze) for 2 weeks.
  - No more commits should be made to the beta branch at this time.

### Second translation freeze
Normally not required, however, occasionally to fix a critical issue requires changes to the translation strings after the translation freeze has started/completed then:
* Ensure `beta` has the changes requiring re-translation.
* Re complete the steps in calling a translation freeze.
* Send an email to the translation mailing list describing the need for new changes and deadline.

## Release candidates (pre-release)
* Ensure it is safe to release an RC.
  - Looking at recent issues filed, specifically looking for those with `p1`, `bug/crash` or `bug/app-crash` labels.
* Check for PRs against `beta`.
  - Use [search on PR page `is:pr is:open base:beta`](https://github.com/nvaccess/nvda/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aopen+base%3Abeta)
  - Look for any PRs based on `beta`, and review and approve/merge or reject them.
* Check for PRs against `rc`, this is more likely after the first RC release.
  - Use [search on PR page `is:pr is:open base:rc`](https://github.com/nvaccess/nvda/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aopen+base%3Arc)
  - Look for any PRs based on `rc`, and review and approve/merge or reject them.
* If this is `RC1`, update translations:
    1. Log into `exbi`
    1. Switch user to nvdal10n: `sudo su nvdal10n`
    1. `cd ~/mr/mainNVDACode`
    1. `mr up`
    1. `cd ../srt`
    1. `mr up`
    1. `mr svn2nvda` **Note:**
        - This may take a few minutes
        - Watch for errors such as `unable to push`.
    1. `exit` To return to your own user.
    - **Note:** This updates `beta` with the new translations.
* Locally, update the `rc` branch and push to GitHub
  - For RC1, reset the `rc` branch to `beta`
  - For RC1+, merge `beta` to `rc`
* Create a [annotated tag](#create-the-release--annotated-tag)
* Wait for the [`appVeyor` build](https://ci.appveyor.com/project/nvaccess/nvda/history) to complete.
  - Consider writing a draft of the release post.
* [Scan the launcher executable](#scan-the-build)
* Create a [new pre-release on GitHub](#convert-annotated-tag-into-a-gitHub-release)
* [Publish the staged release](#publish-the-staged-release)
* [Publicize the release.](#publicize-the-release)

## Final release
* Create a [annotated tag](#create-the-release--annotated-tag)
* Wait for the [`appVeyor` build](https://ci.appveyor.com/project/nvaccess/nvda/history) to complete.
  - Consider writing a draft of the release post.
* [Scan the launcher executable](#scan-the-build)
* [Publish the staged release](#publish-the-staged-release)
* Create a [new release on GitHub](#convert-annotated-tag-into-a-gitHub-release)
* [Publicize the release.](#publicize-the-release)
* Close the release [milestone](https://github.com/nvaccess/nvda/milestones).

## Create the release / annotated tag
* Checkout the version to release.
  - `git fetch`
  - `git checkout origin/<branch>`
  - Where `<branch>` is:
    - For a beta: `beta`
    - For an RC: `rc`
    - For a release: `rc`
* Create a new annotated tag in git, and push to GitHub.
  - Create tag: `git tag -a <tag name> -m "<message>"`
    - The tag must have a `release-` prefix. EG:
      - Beta: `release-2019.2beta3`
      - RC: `release-2019.2rc1`
      - Release: `release-2019.2`
    - The first line of the message should contain the name of the release. EG:
      - Beta: `Release 2019.2beta3`
      - RC: `Release 2019.2rc1`
      - Release: `Release 2019.2`
    - The message may contain extra information (after a blank line) relevant to this specific release.
  - Push to GitHub: `git push origin <tag name>`
  - Tagging the release triggers a build on `appveyor` automatically, as part of this the release will be staged.
  - The release will now show up on the snapshots page (under `beta` or `RC`)
  - Auto update system will start offering it to those checking for betas

## Convert annotated tag into a GitHub release

- Visit the [GitHub new release page](https://github.com/nvaccess/nvda/tags)
- Click on the tag menu button, shown as "..." and choose "Create Release"
- Release Title example: `Release 2019.2beta3`, 
- No description necessary for first RC / Release
  - Subsequent RC / Release can describe important additions & removals.
- For `RC` or `Beta`, ensure option "This is a pre-release" is checked.

### Reasoning

GitHub "releases" are formatted differently, can include metadata such as 'pre-release' and can have binaries attached. In the future, we would like to move to a more automated system that creates this release from the appveyor script and attaches the binaries. Unfortunately GitHub releases don't create an "annotated tag" in git, as such the tag for the release does not have a date or message.

## Scan the build
- Use [VirusTotal](http://www.virustotal.com/).
- Just submit the artifact download URL from `appveyor`
- Recently, using the appveyor URL has resulted in 1 ("CRDF) of the 72 scanners reporting an issue.
- Follow up by scanning with the NV Access URL, which the "CRDF" scanner does not flag as an issue.

## Publish the staged release
- Connect to `exbi`
- Switch user to nvaccess: `sudo su nvaccess`
- Run `nvdaRelease`
  - This will confirm the file currently staged.
  
## Publicize the release
- Add a blog post on  www.nvaccess.org
  - Use a previous blog post as a base.
  - Use a link to the file on NVAccess.org, appveyor build artifacts expire after 6 months.
  - **For RC and Beta:** Put post in the `Development` category.
    - Excluding the first pre-release, include a list of changes since the last pre-release.
  - **For Final release:** Put post in the `Releases` category.
  - It should never be placed in the `News` category.
- Post to [nvda-devel list](https://groups.io/g/nvda-devel/post)
- Post to [nvda-translations list](https://groups.io/g/nvda-translations/post)
- Post to Twitter
- Post on Facebook.
- Post to the NV Access News email list.

## Update auto milestone ID
This ensures correct milestone is set on issues and pull requests now closed by GitHub automatically.
1. Get the milestone id for the new release.
   - Go to https://github.com/nvaccess/nvda/milestones
   - Look at the link URL for the relevant milestone.
   - The number at the end is the `id`.
1. Log into exbi
1. Swap to nvaccess user: `sudo su nvaccess`
1. Edit `~nvaccess/data/nvaServer.conf`
1. In the `[nvdaGithub]` section, change the value of `autoCloseMilestone` to the milestone `id` obtained in step 1.
1. Save the file and `exit` to return to your user.
1. Reload `uwsgi` so the change takes effect: `sudo systemctl reload uwsgi`

## Update NVDA version in `master`
In NVDA source, ensure the `master` branch version number and changes file are correct
1. In `source/buildVersion.py`, update the `version_year` and/or `version_major` variables for the next version.
   - If the next version is the first version for that year (e.g. 2018.1), also update `copyrightYears`.
2. Add a heading for the next version in `user_docs/en/changes.t2t` if it is not there already.

## New section in changes file
Add to the top of the changes file:
```
= 20XY.Z =

== New Features ==


== Changes ==


== Bug Fixes ==


== Changes for Developers ==


```
* If this is a 20XY.1 release add to the "Changes for Developers" section:
`- Note: this is a Add-on API compatibility breaking release. Add-ons will need to be re-tested and have their manifest updated.`