# -*- coding: utf-8 -*-
documentation = [
_(u"""# Creating PR's on the NVDA project"""),
"",_(u"""This page is meant to serve as an explanation for how to fill out"""),
_(u"""[our Github pull request template](https://github.com/nvaccess/nvda/blob/master/.github/PULL_REQUEST_TEMPLATE.md)"""),
"",_(u"""## The template"""),
_(u"""At the start of the template there is a HTML comment block (starting with `<!--`),"""),
_(u"""which points to this wiki page, it can be left in place and will not appear once the issue is saved."""),
_(u"""Feel free to delete it, i.e. all text up to and including `-->`."""),
"",_(u"""### Link to issue number:"""),
_(u"""Please include the issue number here, including information on how this pull request is related to """),
_(u"""it."""),
_(u"""This helps us to keep the information linked together."""),
_(u"""If this is a minor/trivial change an issue does not need to be created."""),
_(u"""If in doubt, please create one."""),
_(u"""Note that Github """),
_(u"""[allows you to automatically close issues using keywords](https://help.github.com/en/articles/closing-issues-using-keywords)."""),
_(u"""For example, when writing `closes #7777` or `fixes #4242` in the body of the description,"""),
_(u"""the mentioned issue will automatically be closed when the pull request is merged into the master"""),
_(u"""branch."""),
_(u"""If your pull request is filed against another branch, such as beta, the particular issue will have"""),
_(u"""to be close manually after merging the pull request."""),
"",_(u"""### Summary of the issue:"""),
_(u"""A quick summary of the problem you are trying to solve."""),
"",_(u"""### Description of how this pull request fixes the issue:"""),
_(u"""Please include a quick discussion of how this change addresses the issue."""),
_(u"""Please also include any links or external information you may have used in order to address the"""),
_(u"""issue."""),
_(u"""This helps others to have the same background as you and learn from this work."""),
"",_(u"""### Testing strategy:"""),
_(u"""Outline the steps you took to test the change."""),
_(u"""This should allow someone else to reproduce your testing."""),
"",_(u"""More broadly, try to answer the following questions:"""),
_(u"""- How have you tested to ensure that your change works as intended?"""),
_(u"""- Have you ensured testing coverage across all supported operating systems?"""),
_(u"""- Have you considered possible regressions (related features or behaviours that may break)?"""),
"",_(u"""Please use this section as an opportunity to try to convince us (and yourself) that your proposed """),
_(u"""change should be merged. """),
"",_(u"""Often in face to face development it's useful to demonstrate a change, quite often bugs are noticed"""),
_(u"""at this point when the new person asks for some variation in testing approach."""),
_(u"""Since we unlikely to be able to demonstrate a feature in an interactive way, an easy-to-follow list"""),
_(u"""of steps for a \"demo\" allows others check themselves without having to work out all the details."""),
_(u"""It also serves as a starting point for members of the community who are testing the changes that go"""),
_(u"""into NVDA."""),
"",_(u"""Example:"""),
_(u"""> In NVDA settings ensure that:"""),
_(u"""> - Keyboard category"""),
_(u""">   - \"speak typed characters\" is unchecked"""),
_(u""">   - \"speak typed words\" is checked"""),
_(u""">"""),
_(u"""> 1. Open notepad"""),
_(u"""> 2. Type \"hello\""""),
_(u"""> 3. Press space"""),
_(u""">"""),
_(u"""> Expect \"hello\" to be announced."""),
"",_(u"""- If many NVDA settings are required, consider attaching a sample `nvda.ini` file to the PR."""),
_(u"""- If a complicated document is required to test with a 3rd party application, consider attaching it"""),
_(u"""  to the PR for others to test with."""),
"",_(u"""### Known issues with pull request:"""),
_(u"""Are there any known issues or downsides of this approach."""),
_(u"""For instance: _Will not work with python 3_"""),
"",_(u"""### Change log entry:"""),
_(u"""An entry intended to explain changes in NVDA to end users."""),
_(u"""Your proposed entry will be added to the `changes.t2t` file which is converted to html and used as a"""),
_(u"""what's changed / change log document."""),
_(u"""See """),
_(u"""[`user_docs/en/changes.t2t`](https://github.com/nvaccess/nvda/blob/master/user_docs/en/changes.t2t)"""),
"",_(u"""Because the `changes.t2t` file is prone to conflicts, we ask contributors not to edit the file directly, but instead add the entry to the bottom of the PR description."""),
_(u"""A lead developer will update file when merging the pull request."""),
"",_(u"""For instance:"""),
_(u"""```"""),
_(u"""*New features*"""),
_(u"""`Added a command to announce useful thing. (#WXYZ, #ABCD)`"""),
"",_(u"""*Changes*"""),
_(u"""`Old command, now also uses new useful command. (#WXYZ)`"""),
_(u"""```"""),
"",_(u"""These descriptions should be in the format: `\"{Description of change}. (#{issue number})\"`"""),
"",_(u"""You may suggest descriptions for multiple sections."""),
_(u"""The usual sections are:"""),
_(u""" """),
_(u"""* New features"""),
_(u"""* Changes"""),
_(u"""* Bug fixes"""),
"",_(u"""Multiple issue numbers can be included, separated by comma."""),
_(u"""If there is no issue number, you can use the PR number."""),
"",_(u"""For examples see the"""),
_(u"""[changes.t2t file](https://github.com/nvaccess/nvda/blob/master/user_docs/en/changes.t2t)"""),
"",_(u"""## Code Review Checklist"""),
"",_(u"""Code must be reviewed (via a Pull Request on GitHub) before it can be accepted into the project."""),
_(u"""The Pull Request template (``.github/PULL_REQUEST_TEMPLATE.md``) asks authors (and reviewers) to"""),
_(u"""consider several aspects of the change."""),
"",_(u"""The aim of this checklist is to ensure each item has been considered by both the author and the"""),
_(u"""reviewer."""),
_(u"""Hopefully it helps to prevent items being forgotten."""),
_(u"""After reviewing the checklist the reviewer and author need to use their best judgement on whether"""),
_(u"""they think further changes need to be made."""),
_(u"""Reviewers are invited to start a conversation about items in the list, to provide guidance on how to"""),
_(u"""improve the PR."""),
_(u"""Not all items will be applicable for all situations, in this case checking the item lets reviewers"""),
_(u"""know it's been considered."""),
_(u"""If the reviewer reaches the same conclusion as the author, no further work is necessary."""),
_(u"""Most items in the checklist have a section in the PR template where you can add your thoughts, doing"""),
_(u"""so may preempt questions from the reviewer ensuring you are on the same page, and speed up the"""),
_(u"""review process."""),
"",_(u"""### Pull Request description is up to date."""),
_(u"""Authors must keep the PR description up to date."""),
_(u"""- Even if changes to the approach are described in the comments for the PR."""),
_(u"""- Future developers need a concise explanation of a change."""),
_(u"""After each modification, check that the PR description is still accurate."""),
"",_(u"""### Unit tests"""),
_(u"""- Discuss under \"testing strategy\" heading."""),
_(u"""- Describe the coverage of automated unit tests?"""),
_(u"""- Is the changed code already, or can it be covered by automated unit tests?"""),
"",_(u"""### System tests"""),
_(u"""- Discuss under \"testing strategy\" heading."""),
_(u"""- Describe the coverage of automated system tests?"""),
_(u"""- Is the changed code already, or can it be covered by automated unit tests?"""),
"",_(u"""### Manual tests"""),
_(u"""- Discuss under \"testing strategy\" heading. """),
_(u"""- How did you manually test the change?"""),
_(u"""- Be clear on steps another user can take to replicate your testing."""),
_(u"""- Is the described manual testing appropriate for the change?"""),
_(u"""- Clearly describing this helps alpha testers, and future developers."""),
_(u"""- As a reviewer, please use this description to replicate the testing (if possible)."""),
"",_(u"""### User Documentation"""),
_(u"""- Does the user documentation need updating?"""),
"",_(u"""### Change log entry"""),
_(u"""Has an appropriate change log entry been supplied."""),
_(u"""As a reviewer, please review it."""),
"",_(u"""### Context sensitive help for GUI changes."""),
_(u"""- New GUI options require context sensitive help assignment."""),
"",_(u"""### UX of all users considered"""),
_(u"""- Users of NVDA are diverse, and rely on different parts of NVDA."""),
_(u"""  Ensure the change caters to users of the following:"""),
_(u"""  - Speech"""),
_(u"""  - Braille"""),
_(u"""  - Low Vision"""),
_(u"""  - Different web browsers (Firefox, Chrome, Edge)"""),
_(u"""- When one of these can not be supported with this change,"""),
_(u"""  highlight it under the \"Known issues\" heading"""),
]