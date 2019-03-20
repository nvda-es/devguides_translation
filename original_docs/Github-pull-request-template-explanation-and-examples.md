# Creating PR's on the NVDA project

This page is meant to serve as an explanation for how to fill out [our Github pull request template](https://github.com/nvaccess/nvda/blob/master/.github/PULL_REQUEST_TEMPLATE.md)

## The template
At the start of the template there is a HTML comment block (starting with `<!--`), which points to this wiki page, it can be left in place and will not appear once the issue is saved. Feel free to delete it, i.e. all text up to and including `-->`.

### Link to issue number:
Please include the issue number here, including information on how this pull request is related to it. This helps us to keep the information linked together. If this is a minor/trivial change an issue does not need to be created. If in doubt, please create one.
Note that Github [allows you to automatically close issues using keywords](https://help.github.com/en/articles/closing-issues-using-keywords). For example, 
when writing `closes #7777` or `fixes #4242` in the body of the description, the mentioned issue will automatically be closed when the pull request is merged into the master branch. If your pull request is filed against another branch, such as beta, the particular issue will have to be close manually after merging the pull request.

### Summary of the issue:
A quick summary of the problem you are trying to solve.

### Description of how this pull request fixes the issue:
Please include a quick discussion of how this change addresses the issue. Please also include any links or external information you may have used in order to address the issue. This helps others to have the same background as you and learn from this work.

### Testing performed:
How have you tested to ensure that your change works as intended, across all supported operating systems, without introducing regressions? Please use this section as an opportunity to try to convince us (and yourself) that your proposed change should be merged. 

### Known issues with pull request:
Are there any known issues or downsides of this approach. For instance: _Will not work with python 3_

### Change log entry:
The section and description of this change to use for the changes file (used as a whats changed / change log document). Because this file (`user_docs/en/changes.t2t`) is prone to conflicts, we ask contributors not to edit the file directly, but instead add the entry to the bottom of the PR description.

For instance:
```
*New features*
`Added a command to announce useful thing. (#WXYZ, #ABCD)`

*Changes*
`Old command, now also uses new useful command. (#WXYZ)`
```

These descriptions should be in the format: `"{Description of change}. (#{issue number})"`

You may suggest descriptions for multiple sections. The usual sections are:
 
* New features
* Changes
* Bug fixes

Multiple issue numbers can be included, separated by comma. If there is no issue number, you can use the PR number.

For examples see the [changes.t2t file](https://github.com/nvaccess/nvda/blob/master/user_docs/en/changes.t2t)