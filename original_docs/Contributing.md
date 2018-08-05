# Contributing documentation

We welcome community contributions for documentation collection repository. Please read this document to learn about how you can contribute your article(s).

## Requirements

It is recommended that you have practical knowledge of programming and Python (NVDA is a Python application). For certain topics, you'll need a detailed knowledge of NVDA source code. We accept documentation written using Markdown syntax.

## Contribution steps

### If you have Git and;or have commit access to NVDA Add-ons organization repository on GitHub

1. Clone the following two repos:
git clone https://github.com/nvdaaddons/devguide
git clone https://github.com/nvdaaddons/devguide.wiki.git
The first repo is the home page (readme.md), and the second is the wiki where the pages will be stored.
2. When wikifying your documentation, use Markdown syntax (not Txt2Tags (T2T) syntax).
3. You need your GitHub credentials (user name and password) to commit changes.
4. When adding a new documentation into the wiki repo, use git add command. Push to the wiki repo first, then modify the main readme.md (first repo) to point to the wiki link then do a git push.
5. When adding a new documentation entry for an add-on, please write the following information:
	* Add-on author name.
	* Where to download the add-on and/or its source code
	* Link to the add-on wiki documentation in the wiki repo.

### If you don’t have access to Git or don’t have commit access to NVDA Add-ons organization

1. Write your documentation using a text editor. Try using Markdown syntax.
2. Send your documentation to the NVDA Add-ons list (nvda-addons@groups.io). You can send it as an attachment to that list or you can leave the URL from where add-ons list members can read your documentation (if you have a website; in case you’ve uploaded your docs to a service such as Dropbox or OneDrive, please let the add-ons list know the URL to download your file).

### If you want to submit pull requests

1. Fork the one or both repositories from above (if you want to work on the wiki, it is best to modify the wiki directly via the web interface).
2. After writing changes, send a pull request for review.

## Documentation guidelines

Following are some guidelines when submitting your contributions (you don’t have to follow all of them and we’ll leave room for exceptions):

1. If you are writing an add-on internals article (or a series of articles), please write your name (so that we can give you authorship credit) and the version of the add-on you are writing about. Don’t forget to include copyright notices (for the add-on and any libraries it uses) and disclaimer (if you are writing about an add-on that isn’t yours).
2. If you’ll be documenting NVDA Core modules or functions, please base it from the latest official release or master branch at the time of your writing, and please give the full signature of the function you’re writing about (example, if writing about message function in the UI module, please use ui.message; similarly , if documenting various UIA objects, please use NVDAObjects.UIA.ClassName e.g. NVDAObjects.UIA.Toast). Let us not forget that Mick and Jamie are the real experts of NVDA source code.
3. If your article references Windows API functions, please specify which DLL exposes this function (e.g. FindWindow is exposed by user32.dll). This is a must, as NVDA provides wrappers for various Windows API functions, housed in wrapper modules (for example, various wrappers for user32.dll functions live in winUser.py).
4. Please provide references at the end of articles (you don’t have to, but it is encouraged). References may include links to MSDN entry for a particular Windows API function, documentation to third-party libraries mentioned and third-party resources. This helps readers learn more about how certain functions work, read more about libraries used and so on (to research them further).
5. Note that this may change based on community feedback. Please let me (Joseph Lee) and other add-ons list members know if you find some flaws with these and things that need changing.

## Frequently Asked Questions

### Add-on readme

Q. What information should I include in my add-on readme?

The readme should include name of the author, download links if any, a brief description of the add-on, command summary, and if needed, a changelog.

Q. What language should I write my readme in?

It is up to you, but English is prefered.

Q. Should I write my readme with translations in mind?

Again this is up to you.

### NVDA Core internals articles

Q. Do I have to be a programmer or an employee of nV Access to write articles?

No, although a background in programming may help you organize your thoughts better.

Q. Should I include examples people can try out in Python Console?

Yes if you can. Note that not all NVDA functions can be tested in Python Console.

Q. What if I want to write about something incubating in next snapshots?

You are welcome to do so, provided that you add a disclaimer that says features may change. Once the feature you are talking about graduates to master, make a note about which stable NVDA build the feature will be included in.

### Add-on internals articles

Q. Do I have to be the author of the add-on in order to write these articles?

No. If you are a user though, then yes, it may help you with organizing your writings.

Q. What is the difference between add-on readme and internals articles?

Add-on readme is mostly meant for users to get to know the add-on. Add-on internals is mostly meant for developers (inside and outside the NVDA community) and other people who are curious about internal workings of an add-on.

Q. I found a bug with the add-on I'm writing an internals article about. What should I do?

First, report the bug to the add-on author and the add-ons community. Then once the bug is fixed, write a note explaining what happened in the article.

Thanks, and we look forward to your contributions.

The NVDA Community Add-ons Team
