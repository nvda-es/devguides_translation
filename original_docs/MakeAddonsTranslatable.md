# Make add-ons translatable throught the NVDA's translation system #

## Steps ##

1. Authors request the inclusion of an add-on in the translation system via the [NVDA add-ons mailing list](https://nvda-addons.groups.io/g/nvda-addons).
2. A member of the NVDA add-on team creates a repo for the add-on at
<https://bitbucket.org/nvdaaddonteam>
	- If the author has a Bitbucket account, s/he can request admin access to the add-on repo, and write access to [add-on files](https://bitbucket.org/nvdaaddonteam/addonFiles).
	- The add-on repo must contain a branch named stable, where authors or other people with write access to the repo should merge code considered stable when the add-on is updated. This branch is used to send translatable messages to, and receive l10n updates from, the [NVDA translation repo](http://subversion.assembla.com/svn/screenReaderTranslations).

3. Admins register the add-on and commit settings for translators from Exbi server (nvdal10n@exbi.nvaccess.org):
	- cd into mr
	- mr up
	- cd available.d
	- mr registerAddon addonRepoName
	- git push
	- cd into mr
	- mr up
	- cd into addons/addonRepoName
	- mr addon2settings
	- cd ~/mr/srt
	- svn commit */settings -m "Make blah add-on available for translation."

4. edit addonFiles/automatic.crontab, so that l10n updates are merged into the stable branch, and translators receive new messages automatically.
	- Copy one of the lines for one of the existing addons, just change the addon name and paste it in the correct section, commit and push.
	- Note: Admins can perform the above process manually, running mr addon2svn and mr svn2addon from Exbi.

## Maintaining the add-on ##

Note: Maintainers may follow other procedures. This info is only provided for convenience, according to discussions like this [topic about repos management](https://nvda-addons.groups.io/g/nvda-addons/message/9418).

- Clone the maintainer repo:
	- ```git clone https://github.com/githubUserName/addonRepoName```
- Add remote for Bitbucket repo:
	- ```git remote add bitbucket https://bitbucket.org/nvdaaddonteam/addonRepoName```
- Fetch Bitbucket repo:
	- ```git fetch bitbucket```
- Track the stable branch:
	- ```git checkout -t bitbucket/stable```
- Periodically:
	- From stable branch:
		- ```git pull``` # Get translations
		- ```git merge master``` # Stable code containing translatable messages
		- ```git push bitbucket stable```
	- From master:
		- ```git pull```
		- ```git merge stable```
		- ```git push origin master``` # Update translations

### References for maintainers ###

- [Push to multiple repos in one step](https://gist.githubusercontent.com/bjmiller121/f93cd974ff709d2b968f/raw/8f17c4d72ba8bd36aea0ec0cf344a8197fa648e8/multiple-push-urls.md)
- [Book about Git](https://git-scm.com/book)

## Requirements ##

### Access to addonFiles ###

This will be granted only to people who have a track record of providing reviews and known to be reliable at their duties, all of this subject to a community-wide dialogue about repo management.

The maintainer should fulfill the following criteria:

1. Has done at least one basic review.
2. Known to be a reliable role model in terms of add-on authoring, reviewing, maintenance, and promotion (repo management is a job with tons of responsibilities).
3. Known to be responsive to communication to and from users and other developers.
4. Keeps an eye on NvDA Core development.

### Access to repos and add-on registration ###

- Registration or access to repos won't be denied for personal issues, such as differences in opinions, criticism to admins code or attitude based on evidence, etc. If an admin is not reliable at their duties, that person should be replaced by other maintainer.
- Anyway, if the registration or access request is done in a manner that is seen (perceived or actual) as threatening or harmful to the individual being asked to register a new maintainer, or for that matter, to the whole community, this request will be denied, and this will be archived forever (to serve as a lesson for the actual individual who did this in the first place, as well as for the community).


## Related links ##

- [Adding a New Language to Ikiwiki](https://github.com/nvaccess/l10n-code/wiki/Adding-a-New-Language-to-Ikiwiki)
- [mr documentation](https://www.systutorials.com/docs/linux/man/1-mr/)
- [Thread about repo management and registration, started by Joseph Lee](https://nvda-addons.groups.io/g/nvda-addons/message/6937)
## Aknowledgements ##

This document is based on work and information provided by Mesar Hameed and James Teh.

Thanks for making this possible.
