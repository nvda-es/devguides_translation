# Using AppVeyor to release NVDA add-ons 

## Procedure to build and attach nvda-addon files to releases on GitHub

This can be used to automate the building of NVDA add-ons (binaries with the .nvda-addon extension), which will be uploaded from Appveyor to GitHub, and attached to the created release.

It works for add-ons based on the [Add-on Template](https://github.com/nvdaaddons/addontemplate).

### Setting AppVeyor for add-ons

1. Get the code of an add-on.

Example:

```
git clone https://github.com/username/repo

git pull
```

2. In the root of the add-on folder (where the sconstruct file is placed), paste this [AppVeyor configuration file](https://gist.github.com/nvdaes/a486e45b98566d530688f6da9ce75f84/raw/d05b620185a58327b39da1215cf3c13c01249031/appveyor.yml) (appveyor.yml).

3. If you don't have it, [create a personal API access token](https://github.com/settings/tokens) and [encrypt it](https://ci.appveyor.com/tools/encrypt).

4. In the appveyor.yml file, replace the value provided for the secure key with your encrypted token. For instance, instead of

```
  auth_token:
    secure: 3yxF2EQ/wfLKNEobcRfdNL6srjXjoMdRa/LSQ7z2PJNqOL3IEyiFtlnxxHeIQskH
```

```
auth_token:
    secure: yourEncryptedToken
```

Now, you can paste your appveyor.yml file to any add-on posted on your GitHub account.

5. [Sign in with AppVeyor](https://www.appveyor.com/).

6. From AppVeyor, select New Project. (If needed, choose GitHub and authorize it).

7. Locate the name of the repo you're interested in, move the mouse over it (for instance pressing NVDA+numpadDivide or NVDA+shift+m), and activate the "Add" link below.

### Releasing

To post a new release of an add-on, you can create a tag and push it to GitHub:

Example

```
git tag 1.0

git push origin 1.0
```

Now, the release will be created and binary-1.0.nvda-addon will be attached on GitHub.

## References

- [Appveyor.yml reference](https://www.appveyor.com/docs/appveyor-yml/)
- [Publishing artifacts to GitHub Releases | AppVeyor](https://www.appveyor.com/docs/deployment/github/#configuring-in-appveyoryml)
- [Syntax of the release name value in the deploy section of the appveyor.yml configuration file](http://help.appveyor.com/discussions/questions/9221-syntax-of-the-release-name-value-in-the-deploy-section-of-the-appveyoryml-configuration-file)
- [mesa/appveyor.yml at master · anholt/mesa](https://github.com/anholt/mesa/blob/master/appveyor.yml)
- [Discussion on the NVDA add-ons mailing list](https://nvda-addons.groups.io/g/nvda-addons/topic/6220467)

## Aknowledgements

Thanks to @abdel792, @derekriemer and @tuukao for making this possible.
