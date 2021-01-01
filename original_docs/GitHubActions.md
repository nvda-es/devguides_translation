# Using GitHub Actions to manage NVDA add-ons 

This document is based on the [article about Appveyor](https://github.com/nvdaaddons/nvdaaddons.github.io/wiki/appveyor).

## Procedure to build, test with NVDA, lint diffs and attach addon binaries to releases on GitHub

### Setting GitHub Actions for add-ons

This works for add-ons based on the [Add-on Template](https://github.com/nvdaaddons/addontemplate).

1. Get the code of an add-on.

	Example:

	```
	git clone https://github.com/username/repo

	git pull
	```
2. In the root of the add-on folder (where the sconstruct file is placed), paste this [Flake8 configuration file](https://gist.githubusercontent.com/nvdaes/9caffa59ebbdcfd3e69f8a200b512be9/raw/3cbaaff48239b1b98e863901cf6a76b955412df7/setup.cfg), which uses [Flake8 rules configured for NVDA](https://raw.githubusercontent.com/nvaccess/nvda/master/tests/lint/flake8.ini). This must be named setup.cfg

3. In the same folder, paste this [requirements.txt file](https://raw.githubusercontent.com/nvaccess/nvda/master/tests/lint/lintInstall/requirements.txt)

4. In the same folder, create a file named `changelog.md`. This file should be empty or include changes for the current release.

5. Under the root folder of the add-on repository, create a `.github/workflows` subdirectory.

6. Inside the `repositoryRootFolder/.github/workflows` subfolder, you can include GitHub workflow files (.yml or .yaml). Feel free to use, for example, workflows available at <https://github.com/nvdaes/clipContentsDesigner/tree/master/.github/workflows>

Here is info about [managing workflow runs](https://docs.github.com/en/free-pro-team@latest/actions/managing-workflow-runs).

### Releasing

To post a new release of an add-on, you can create a tag and push it to GitHub:

Example

```
git tag 1.0

git push origin 1.0
```

Now, the release will be created and binary-1.0.nvda-addon will be attached on GitHub.

With the provided yaml file, releases created from tags ending with "-dev" will be marked as prereleases.

Example

```
git tag 1.0-dev

git push origin 1.0-dev
```

## References

### Documentation

- [GitHub Actions documentation](https://docs.github.com/en/free-pro-team@latest/actions)
- [Flake8 documentation](https://flake8.pycqa.org/en/latest/)

### Used actions

- [actions/checkout: action for checking out a repo](https://github.com/actions/checkout)
- [actions/upload-artifact](https://github.com/actions/upload-artifact): action for uploading artifacts
- [actions/download-artifact](https://github.com/actions/download-artifact): an action for downloading artifacts
- [unsplash/comment-on-pr@master](https://github.com/unsplash/comment-on-pr): an action to comment on a PR (may not work on Windows)
- [action/GitHubScript](https://github.com/actions/github-script): scripting GitHub API in JavaScript
- [actions/create-release: An Action to create releases via the GitHub Release API](https://github.com/actions/create-release)
- [svenstaro/upload-release-action: Upload files to a GitHub release](https://github.com/svenstaro/upload-release-action)

## Aknowledgements ###

The above workflows are created or based on work performed by @mhameed

<https://github.com/nvdaaddons/l10ntest>

Thanks also to @Josephsl and @CyrilleB79 for replies, as mentioned on this [message about GitHub workflows](https://nvda-addons.groups.io/g/nvda-addons/message/13492)
