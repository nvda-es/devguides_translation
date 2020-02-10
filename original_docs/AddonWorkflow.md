Definitions:

In the below text, for brevity we will write he, him, his, but of course it applies to both sexes.

Author: the standard meaning of author, or the current maintainer of an addon.

Supporting reviewer: A member of the nvda addon team, that has shown technical ability, fairness, dedication and willingness to help others.

An author can not act as a supporting reviewer if he is the author of the addon, even if he is a member of the addon team.
For a different addon, roles may be switched.

## Workflow

1. An author wishes to create an addon, so he forks the community supplied addonTemplate to their personal github space, and rename it to the name of the new addon.
2. He proceeds to develop the addon, committing and pushing to his personal repo.
3. When he is ready with the addon, he informs the addon list, and requests general feedback.
4. At this point, most feedback is probably user testing, but hopefully also some code review.
	Please note that the community can not guarantee the quality or the content of the addon, so if you as a user run the addon without having looked at the code, it is at your own risk.
5. The feedback is processed by the author, goto step 2, or when sufficient feedback has been processed goto step 6.

	It is not expected that the author will accept all requests, so if you are a user, and the author does not think your feature request fits with his addon, both authors and users are reminded to remain civil to all parties.

	All reasonable requests such as reminder of copyright info, license, improvements to the readme etc are expected to be fixed by the author.

6. Assuming sufficient user interest for the addon to be available on the community website then the author requests that the addon is forked to the nvdaaddons organisation by a supporting reviewer.
7. Please remember that addons are accepted at the discretion of the community reviewers. Everyone is a volunteer, and is under no obligation to do anything. Of course if you take part in the community and help by reviewing other peoples code, you will build up good will and others will be more likely to review your code.
8. The supporting reviewer makes sure there is a license, copyright information, a readme file, that the addon does what it is suppose to do, and is ok in terms of security.

	It is expected that the supporting reviewer will have read each line of the addon code global plugin, app modules or other files (not external libraries), for security risks before forking it.

	Security in this context means: that the addon does not read any unexpected files from the users computer, does not upload anything, and does not download anything unexpected.

9. The supporting reviewer forks the addon to the nvda addons organisation.
10. Issues, pull requests should go to the author, and to the authors repo, not to the community fork.

	Users can of course still continue interacting with the addon author using the addon mailing list.

11. The addon author is expected to add the community copy of the repo as a remote, so that he can merge in translations.
12. Supporting reviewer might have to do the following tasks to the community repo after forking:

	Delete any other branches than master, add additional information for automatic building, webhooks etc.

	Add a protection rule on master so that it is not accidentally pushed to, and that it needs a pr with a minimum of 1 reviewer (even admins).

	Other translation workflow related steps [see here][1].

	Create a stable branch.

	Add protection rules to stable so that the translation system can push, every one else needs a pr (even admins).

13. Supporting reviewer merges master into stable.
14. Supporting reviewer triggers a release.

	This should only bump the patch number (last digit of the version number), i.e. v1.0.0 becomes v1.0.1.

15. After a period of time, the addon author wishes to make a new release, he makes a release pull request from his master to the master of the community copy.
16. A supporting reviewer, reviews the pull request, again, for security, for updated readme etc, and may request further work to be done before the pr is accepted. Only the changes since the last release needs to be reviewed.
17. Once the pr is excepted into master, the supporting reviewer will bump the major or minor version as agreed with author, i.e. just delete the "-dev" from version variable.

	Loop back to step 13.

## Considerations

The following considerations were taken into account when proposing this addon workflow.

1. Addon security.

	As the community of nvda users and addon authors grow, we want to promote a sense of trust to do the correct thing, so that a user should feel confident in installing or updating addons, so that addons can be installed alongside NVDA in schools, universities, public libraries etc.

	That as adon authors we take our volunteer work seriously, and we appreciate the trust that we have been given.

	Therefore the final step of making a release is with the community, not with the addon author, as we want the final product to be fully trusted.

2. Shared learning environment.

	By giving each other constructive criticism, suggestions etc, we build something better and stronger, because no one is perfect, and we all learn from each other.

	Criticism of code is not a criticism against the author, it is simply recommendations to improve the code, because the reviewer cares about the quality of your code.

	If you feel that a reviewer overlooked something when reviewing someone elses addon, please do not hesitate to provide your review as no one has monopoly on giving feedback.

3. Reducing the existing workload of addon reviewers.

	At the point of writing, we have approx 70 addons, and managing all this is not simple or straightforward.

	Unfortunately we ended up in a messy situation, with repos in github, on bitbucket, and some other manual work that needed to be done on a server.

	It was felt that more time was spent trying to administrate the system, than to be able to do the interesting work of reviewing and giving feedback, therefore more steps should be automated.

	This automation is not yet in place, but if the consensus is that this is a reasonable workflow, then work on the additional automation will begin.

	With less complex requirements for a potential addon reviewer, hopefully more people will become community reviewers and can take an active and responsible role, as then it is simply about reviewing and merging code, and does not require such a time investment.

## Things for future discussions.

1. Minimum time between releases?
2. How can (if we should?), accommodate dev releases?

[1]: https://github.com/nvdaaddons/nvdaaddons.github.io/wiki/MakeAddonsTranslatable
