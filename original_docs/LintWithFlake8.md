# Lint with Flake8

## Introduction

For many years, NV Access and the NVDA community have received hundreds of pull requests from many contributors, including new features, bug fixes, and translations. While many pull request discussion centered around implementation, there were several that needed to be edited to make the new code compliant with NVDA's coding guidelines.

In 2019, as part of a broader effort to port NVDA to Python 3 and to ease pull request review process, NV Access introduced linting tools, specifically Flake8. Linting allows source code to be checked for coding guidelines and gives a chance for contributors to correct mistakes before submitting changes for review by the community.

For help with coding standards or gotchas with linting messages see:
- https://github.com/nvaccess/nvda/wiki/Contributing
- [`tests/lint/readme.md`](https://github.com/nvaccess/nvda/blob/master/tests/lint/readme.md)