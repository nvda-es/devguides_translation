# Using GitHub Actions to manage NVDA add-ons 

This document is based on the [article about Appveyor](https://github.com/nvdaaddons/nvdaaddons.github.io/wiki/appveyor).

## Procedure to build, lint and attach nvda-addon files to releases on GitHub

### Setting GitHub Actions for add-ons

This works for add-ons based on the [Add-on Template](https://github.com/nvdaaddons/addontemplate).

1. Get the code of an add-on.

	Example:

	```
	git clone https://github.com/username/repo

	git pull
	```
2. In the root of the add-on folder (where the sconstruct file is placed), paste this [Flake8 configuration file](https://gist.githubusercontent.com/nvdaes/9caffa59ebbdcfd3e69f8a200b512be9/raw/3cbaaff48239b1b98e863901cf6a76b955412df7/setup.cfg), which uses [Flake8 rules configured for NVDA](https://raw.githubusercontent.com/nvaccess/nvda/master/tests/lint/flake8.ini). This must be named setup.cfg

3. Under the root folder of the add-on repository, create a `.github/workflows` subdirectory.

4. Inside the `repositoryRootFolder/.github/workflows` subfolder, you can paste this [GitHub workflow file](https://gist.githubusercontent.com/nvdaes/05451e4e6065bf67a2f121b3028de5ec/raw/5fc51f0b0bbeb807d22f5bceb7eafcec1e0911c1/addon.yml). File extension should be .yml (or .yaml).

- The above workflow will be triggered on push and pull request events.
- Errors detected by Flake8 will be shown, but won't stop the workflow, so that the add-on can be built or released even when syntax or style errors are found.

Here is info about [viewing and managing GitHub workflows](https://help.github.com/en/actions/configuring-and-managing-workflows/managing-a-workflow-run).

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

- [GitHub Actions documentation](https://help.github.com/en/actions)
- [Flake8 documentation](https://flake8.pycqa.org/en/latest/)

### Used actions

- [actions/checkout: Action for checking out a repo](https://github.com/actions/checkout)
- [actions/create-release: An Action to create releases via the GitHub Release API](https://github.com/actions/create-release)
- [svenstaro/upload-release-action: Upload files to a GitHub release](https://github.com/svenstaro/upload-release-action)

### Real example

- [clipContentsDesigner NVDA add-on](https://github.com/nvdaes/clipContentsDesigner)
