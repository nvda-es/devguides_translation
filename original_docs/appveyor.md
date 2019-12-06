# Using AppVeyor to manage NVDA add-ons 

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

	Note: you could need to set the following token scopes to avoid  inconvenience when releasing tags:

	- notifications
	- public_repo
	- repo:status
	- repo_deployment

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

Bonus track: Also, Abdel has created an [appveyorForFTP.yml file](https://gist.githubusercontent.com/nvdaes/a486e45b98566d530688f6da9ce75f84/raw/46236e04b02de117f9edbb30aaf626692116b6c3/appveyorForFTP.yml) for releasing using an FTP server.

## Personal deployment environment

In the example above, we've described how to introduce the encrypted key of your GitHub personal token in the appveyor.yml file.

If you want to keep this personal key, without sharing it in your repo, you can create a personal deployment environment.

For that, go to [your appveyor environment page](https://ci.appveyor.com/environments) and click on the "New environment" link.

Once in the new environment creation page, we describe below the procedure for creating a deployment for GitHub, as well as an FTP deployment:

### Creating a personal deployment environment for GitHub

To create a personal deployment environment for GitHub, you should make the following choices.

The $(REPO_NAME) environment variable used in the release description was created in the before_deploy section of [this appveyor.yml configuration file](https://gist.githubusercontent.com/abdel792/708a787bb79b265c32b66e363e9cb5c1/raw/3757add3bd8a3d872453f949109b38769d28592d/appveyor.yml).

You must use this personal deployment environment with its appropriate configuration file so that it can recognize the name of the add-on in its description.

1. Provider: GitHub Releases

2. Environment name: GitHub_deployment

3. Tag name: $(APPVEYOR_REPO_TAG_NAME)

4. Release name: Release $(APPVEYOR_REPO_TAG_NAME)

5. Release description: This is the release $(APPVEYOR_REPO_TAG_NAME) of the $(REPO_NAME) addon for the NVDA screen reader built and uploaded to GitHub using Appveyor.

6. GitHub authentication token: Your personal GitHub token. (Warning: This is your personal GitHub token, not your encrypted key with Appveyor)

7. Repository name: Leave empty, this field is optional
 
8. Artifact(s) to deploy: addon

This done, submit your form by validating "Add environment" button.

### Creating a personal deployment environment for FTP

To create a personal deployment environment for FTP, you should make the following choices:

1. Provider: FTP 

2. Environment name: ftp_deployment

3. Protocol: FTP 

4. Host: Your host.

5. Active mode: Leave empty, this field is optional 

6. Username: Your username

7. Password: Your password

8. Remote folder: The name of the folder that will contain the add-on on your FTP server. (It can be something like /nvda-addons or /add-ons)

9. Artifact(s): addon

10. Application: Leave empty, this field is optional
 
11. Use alternative FTP library (beta): Leave empty, this field is optional 

This done, submit your form by validating "Add environment" button.

### Adding the deploy section for personal environments

Once your personal environment has been added, you'll just have to add the following deploy section to your appveyor.yml file, mentioning only the name you have chosen for your environment

1. For GitHub deployment:

	```
	deploy:
	- provider: Environment
	  name: GitHub_deployment
	  on:
	    APPVEYOR_REPO_TAG: true
	```
	Example of [appveyor configuration file for GitHub personal deployment environment](https://gist.githubusercontent.com/abdel792/708a787bb79b265c32b66e363e9cb5c1/raw/3757add3bd8a3d872453f949109b38769d28592d/appveyor.yml)
2. For FTP deployment:

	```
	deploy:
	- provider: Environment
	  name: ftp_deployment
	  on:
	    APPVEYOR_REPO_TAG: true
	```
	Example of [appveyor configuration file for FTP personal deployment environment](https://gist.githubusercontent.com/abdel792/58c7fa82c44df08b06d2674bb8bd6c70/raw/75eede89b1702df923d36fdccc2ccc47b7046cc1/appveyorForFTP.yml)


## Procedure to receive notifications about commits

For notifications about push events (recommended for add-ons review), please see:
https://github.com/nvdaaddons/nvdaaddons.github.io/wiki/githubWebhooks

Anyway, if you want to use AppVeyor: 

1. Create an email address to receive notifications. For instance, you may use the [groups.io email integration](https://groups.io/static/features).

2. In the appveyor.yml file, add these lines:

	```

	notifications:
	  - provider: Email
	    to:
	      - notificationsEmailAddress.example.com

	```

	Replace notificationsEmailAddress.example.com with a valid email address.

	Here is a [topic in groups.io mailing list as a real example](https://nvdaes.groups.io/g/NVDAADDONSCOMMITS/topic/build_completed/27377767).

## References

- [Appveyor.yml reference](https://www.appveyor.com/docs/appveyor-yml/)
- [Publishing artifacts to GitHub Releases | AppVeyor](https://www.appveyor.com/docs/deployment/github/#configuring-in-appveyoryml)
- [Syntax of the release name value in the deploy section of the appveyor.yml configuration file](http://help.appveyor.com/discussions/questions/9221-syntax-of-the-release-name-value-in-the-deploy-section-of-the-appveyoryml-configuration-file)
- [mesa/appveyor.yml at master · anholt/mesa](https://github.com/anholt/mesa/blob/master/appveyor.yml)
- [Discussion on the NVDA add-ons mailing list](https://nvda-addons.groups.io/g/nvda-addons/topic/6220467)
- [Updates for appveyor by Abdel on the NVDA add-ons mailing list](https://nvda-addons.groups.io/g/nvda-addons/topic/31686195#7943)

## Acknowledgements

Thanks to @abdel792, @derekriemer and @tuukao for making this possible.
