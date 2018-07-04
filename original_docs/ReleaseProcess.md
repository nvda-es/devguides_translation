# Release Process

This document provides rough guidelines for the process of developing NVDA releases. All current and potential developers and translators should read and follow this document. These guidelines may be broken under special circumstances. Any concerns should be discussed with the lead developers: Mick Curran (@michaelDCurran) and Reef Turner (@feerrenrut).

## Changes to the existing process
The process outlined later in this document has only been implemented very recently. Therefore this first section talks specifically about the changes from the older process. 
### Goals and reasoning
The main goal of these changes is to remove the need for a "next" branch and pr incubation. Reasons for this are:

* The next branch required manual merging of prs. This did not fit in well with Github's infrastructure in that these incubation merges were not tracked very well, reverts were messy and sometimes required next to be totally re-created, prs on next would frequently become conflicted with other prs, which meant manually fixing conflicts in both next and master.
 * Up until recently incubation was the only way we could guarantee some kind of code quality. Now we have a growing number of unit tests, system testing is well under way, and Github's management of prs (including mandatory code reviews) ensure a minimum code quality we did not have before.
### Changes for developers
* Once a pr is approved by reviewers and all build checks pass, the pr will be merged straight to master. There is no longer incubation on next.
* If a merged pr results in a regression, new bug or does not work as advertised, the lead developers will be a little more strict on reverting the pr than in the past.
### Changes for testers
* The next branch and next snapshots will no longer exist. Anyone currently on a next snapshot will be automatically updated to master snapshots.
 * Anyone currently on master snapshots will stay on master snapshots, however it is important to note that these snapshots should now be considered less stable than they were previously as code is no longer incubated first. Having said this though, as we have also now put in place automated checks testing the code, we should be able to guarantee these snapshots will always run. We do advise though if you would prefer something a little more stable, to consider testing our new beta releases, that will start coming out about 5 weeks before the official release.

## Release Workflow
This is the general release workflow. Information for specific community groups is provided in later sections.

### Development Phase
* Work should be done in topic branches.
* A topic branch should be submitted for inclusion using a pull request.
* All pull requests must be reviewed by one of the lead developers.
* "master" is the mainline branch for NVDA development. Once a pull request has been reviewed and approved by at least one lead developer and all build checks have passed, it will be squash merged into master.
* If the merging of a pr to master causes any build checks on master to fail, the pr is reverted without question. This is however unlikely to be an issue as build checks on the PR itself must have already passed.
* If a merged pr has been identified as causing a regression, new bug, or does not work as originally reported, the pr may be reverted at the discretion of the lead developers. Reasons in favor of not reverting the pr may be: 
    * The PR was submitted by an active collaborator and it is inevitable that they will follow through with a suitable pr to address the issues.
    * The bug is trivial enough to be fixed by a collaborator.
* Compiled snapshots of master will be made available to the public for very early testing. This is bleeding-edge code and should never be run in production environments.
* Up until 7 weeks before a release, a last known good commit of master (I.e. one that passes build checks) will be periodically merged into a "beta" branch, making that code available for early translation. The beta branch at this stage should still be considered bleeding-edge, and is not recommended for people than other to check early translation work.

### Beta phase
* From 7 weeks before the release, merges from master to beta will no longer occur. New pull requests may be now considered for squash merging straight to beta, if and only if they are addressing a bug introduced in the current release cycle or a critical Operating System change out of our control. 
* If any changes are made to beta, such as the merging of critical prs or translation merges, beta will be periodically merged back to master. 
* Starting from 5 weeks before final release, tagged beta releases will be published periodically, allowing the wider community to try out the betas. At this stage code originally introduced through master will have been tested for at least 2 weeks, thus the beta builds can be seen as beta quality.
* If a merged pr that reached beta has been identified as causing a regression, new bug, or does not work as originally reported, the pr may be reverted at the discretion of the lead developers. Reasons in favor of not reverting the pr may be: 
    * The bug is trivial enough to be fixed by a collaborator.
* If a pull request is reverted from beta, it is more than likely any new pull request replacing it will not get into the current release.

### Translatable String Freeze
* 3 weeks before the release is due, the beta branch will enter a translatable string freeze for 2 weeks. That is, no changes to text strings that affect translations are allowed. Minor spelling or grammatical fixes may be made to documentation files, but gettext strings in the code should not be changed at all.
* Only critical bug fixes and translation updates should be committed to the beta branch at this stage.

### Release Candidate
* After the translatable string freeze, the "rc" branch will be created based on the beta branch.
* The first release candidate will immediately be released from the rc branch.
* After this, only critical bug fixes should be committed to the rc branch.
* Subsequent release candidates may be released.
* The final release can only be made if there have been no commits and at least 1 week since the last release candidate.

### Representation on GitHub
* For most items, an issue will be filed and discussed before a pull request is submitted.
* If priority should be given to an issue for inclusion in a specific release, its milestone should be set to the appropriate release milestone (e.g. 2014.4).
* Once a pull request is squash merged to the master branch, the milestone for the issue (if any) and pull request should be set to the next release milestone (e.g. 2013.2) and it should be closed as fixed.
* Issues/pull requests for bug fixes for an rc should have their milestone set to the relevant release (e.g. 2013.2).

### Scheduled Releases
* Generally, final releases will be due around 22 February, 22 May, 22 August and 22 November. The exact date for each release will be determined by the lead developers.

### Maintenance Release
* Under rare circumstances, a maintenance release (e.g. 2013.1.1) may be made.
* A maintenance release may only include fixes for crashes and major security issues.
* Maintenance releases are made from the rc branch.

## For Developers
* GitHub issues should be created for most issues and discussed first before submitting a pull request. However, some trivial changes might not require an issue first. See [[Contributing]] for details.
* Work should be done in a separate topic branch.
* Any relevant documentation should be included in the topic branch.
* New commands, drivers, settings, dialogs, etc. must be documented in the User Guide.
* Topic branches should be submitted as pull requests against master, unless a lead developer has specifically requested  the pull request be made against beta or rc in the case of addressing bugs introduced in the current release cycle. 

## For Translators
* All translation should be based on the beta branch.
* Translators should ensure their translation is up to date a day before the translatable string freeze ends in order for it to be included in the upcoming final release. The lead developers will announce the deadline when the freeze begins, but it will generally be close to UTC 00:00 on 14 February, 14 May, 14 August and 14 November. Work submitted after this time will not be included in the upcoming release.

## For Testers
* beta releases are beta quality. They include code that will be in the next release and has been tested without reported issues for at least a week.
* The master branch is bleeding edge. It includes code that is being tested for possible inclusion in upcoming releases, but it may not yet be tested much (if at all) and there may be major bugs.