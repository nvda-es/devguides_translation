# Creating PR's on the NVDA project

This page is meant to serve as an explanation for how to fill out [our Github pull request template](https://github.com/nvaccess/nvda/blob/master/.github/PULL_REQUEST_TEMPLATE.md)

## The template
At the start of the template there is a HTML comment block which points to this wiki page, it can be left in place and will not appear once the issue is saved. Feel free to delete it.

### Link to issue number:
Please include the issue number here. This helps us to keep the information linked together. If this is a minor/trivial change an issue does not need to be created. If in doubt, please create one.

### Summary of the issue:
A quick summary of the problem you are trying to solve.

### Description of how this pull request fixes the issue:
Please include a quick discussion of how this change addresses the issue. Please also include any links or external information you may have used in order to address the issue. This helps others to have the same background as you and learn from this work.

### Testing performed:
How have you tested to ensure that your change works as intended, across all supported operating systems, without introducing regressions? Please use this section as an opportunity to try to convince us (and yourself) that your proposed change should be merged. 

### Known issues with pull request:
Are there any known issues or downsides of this approach. For instance: _Will not work with python 3_

### Change log entry:
The section and description of this change to use for the changes file. The valid sections are:
 
* New features
* Changes
* Bug fixes

For examples see the [changes.t2t file](https://github.com/nvaccess/nvda/blob/master/user_docs/en/changes.t2t)