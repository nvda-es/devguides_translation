## Introduction
This [project](https://summerofcode.withgoogle.com/projects/#4878633951297536) for the 2019 [Google Summer of Code](http://summerofcode.withgoogle.com) aimed to improve NVDA's performance and stability in Command Prompt, Power Shell, and the Windows Subsystem for Linux. In particular, new Windows Console support was written that took advantage of modern Windows APIs, such as Microsoft UI Automation, which were previously unavailable in consoles.

## Work performed
A series of pull requests (PRs) have been submitted to NVDA as part of this project.

### Merged PRs
The following pull requests have been incorporated into the NVDA codebase:

* [x] Preliminary support for UI Automation in Windows Console ([#9614](https://github.com/nvaccess/nvda/pull/9614))
* [x] UI Automation in Windows Console: limit blank lines in review and initial word movement support ([#9647](https://github.com/nvaccess/nvda/pull/9647))
* [x] UI Automation in Windows Console: make speaking of passwords configurable ([#9649](https://github.com/nvaccess/nvda/pull/9649))
* [x] UI Automation in Windows Console: only enable UIA when available ([#9650](https://github.com/nvaccess/nvda/pull/9650))
* [x] UI Automation in Windows Console: add STABILIZE_DELAY and improve "speak typed words" ([#9651](https://github.com/nvaccess/nvda/pull/9651))
* [x] UI Automation in Windows Console: remove the `isTyping` logic from UIA consoles ([#9673](https://github.com/nvaccess/nvda/pull/9673))
* [x] UI Automation in Windows Console: add focus redirection for the UIA console main window ([#9674](https://github.com/nvaccess/nvda/pull/9674))
* [x] UI Automation in Windows Console: Remove "Text area", replace isAtLeastWin10, and code cleanup ([#9761](https://github.com/nvaccess/nvda/pull/9761))
* [x] UI Automation in Windows Console: Make UIA the default for Windows 10 1803 and later ([#9771](https://github.com/nvaccess/nvda/pull/9771))
* [x] V2 of UI Automation in Windows Console: work around Microsoft bugs on Windows 10 version 1903 and improve caret movement ([#9802](https://github.com/nvaccess/nvda/pull/9802))
* [x] UI Automation in Windows Console: fix `ConsoleUIATextInfo.collapse(end=True)` ([#9887](https://github.com/nvaccess/nvda/pull/9887))
* [x] Improve keyboard support for some terminal programs ([#9915](https://github.com/nvaccess/nvda/pull/9915))
* [x] UI Automation in Windows Console: fix "review start of line" script ([#9944](https://github.com/nvaccess/nvda/pull/9944))
* [x] UI Automation in Windows Console: improve reliability of visible range checks ([#9957](https://github.com/nvaccess/nvda/pull/9957))
* [x] V2 of disable caret events in the UIA console ([#9986](https://github.com/nvaccess/nvda/pull/9986))
* [x] UI Automation in Windows Console: Always use `ConsoleUIATextInfo` in UIA consoles ([#10052](https://github.com/nvaccess/nvda/pull/10052))
* [x] V2 of UI Automation in Windows Console: fix setEndPoint/compareEndPoints ([#10057](https://github.com/nvaccess/nvda/pull/10057))
* [x] UI Automation in Windows Console: fix bugs in the set/compare endPoint overrides ([#10091](https://github.com/nvaccess/nvda/pull/10091))

### PRs awaiting review
The following pull requests are awaiting review as of 20 August 2019:

* [ ] Disable caret events in all terminal programs ([#10118](https://github.com/nvaccess/nvda/pull/10118))
* [ ] UI Automation in Windows Console: Don't automatically enable UIA in consoles on Windows 10 version 1803 ([#10129](https://github.com/nvaccess/nvda/pull/10129))

### Unmerged PRs
The following pull requests were not merged:

* [ ] UI Automation in Windows Console: add STABILIZE_DELAY, only enable UIA when available, limit blank lines in review, make speaking of passwords configurable, improvements to "speak typed words", and initial word movement support ([#9646](https://github.com/nvaccess/nvda/pull/9646)): Split off into smaller PRs, which were merged separately.
* [ ] UI Automation in Windows Console: make review bounds configurable ([#9687](https://github.com/nvaccess/nvda/pull/9687)): A more generic, deeply integrated version of this feature was preferred (see below PR).
* [ ] Allow the review cursor to be bounded to onscreen text ([#9735](https://github.com/nvaccess/nvda/pull/9735)): Since the Windows Console supports scrolling with the keyboard, no more use cases seem to exist for this feature.
* [ ] UI Automation in Windows Console: work around Microsoft bugs on Windows 10 version 1903 and improve caret movement ([#9773](https://github.com/nvaccess/nvda/pull/9773)): This PR caused [#9786](https://github.com/nvaccess/nvda/issues/9786) so was reverted.
* [ ] Fix [#9786](https://github.com/nvaccess/nvda/issues/9786) ([#9787](https://github.com/nvaccess/nvda/pull/9787)): superseded by [#9802](https://github.com/nvaccess/nvda/pull/9802).
* [ ] UI Automation in Windows Console: disable some GetVisibleRanges dependent logic when consoles are maximized ([#9899](https://github.com/nvaccess/nvda/pull/9899)): Eventually superseded by [#9957](https://github.com/nvaccess/nvda/pull/9957).
* [ ] UI Automation in Windows Console: disable filtering when tab is pressed ([#9936](https://github.com/nvaccess/nvda/pull/9936)): A change backported from [#9915](https://github.com/nvaccess/nvda/pull/9915) as a quick fix for 2019.2 which couldn't be integrated in time.
* [ ] Disable caret events in the UIA console ([#9985](https://github.com/nvaccess/nvda/pull/9985)): Closed by mistake.
* [ ] UI Automation in Windows Console: fix setEndPoint/compareEndPoints ([#10043](https://github.com/nvaccess/nvda/pull/10043)): Closed since a Github bug was preventing some newer commits from being included.
* [ ] Revert "V2 of UI Automation in Windows Console: fix setEndPoint/compareEndPoints" ([#10088](https://github.com/nvaccess/nvda/pull/10088)): The regressions which this functionality introduced were fixed, making this reversion no longer necessary.

## Testing performed
UIA console support has been tested on Windows 10 versions 1803, 1809 and 1903 according to the following test plan. Tests passed unless otherwise indicated.

### Switching console implementation
1. In NVDA advanced preferences, change the "Windows Console support" setting to "prefer UIA".
2. Open Command Prompt.
3. Check the console's type: with Command Prompt in focus, open a Python console with NVDA+control+z and enter "nav" at the prompt. NVDA should report that the object is of type `WinConsoleUIA` on Windows 10 version 1709 and later, `WinConsole` otherwise.
4. If you are not testing on at least Windows 10 version 1709, skip to step 7. Otherwise, close the Python console and enable the "use legacy console" option in Command Prompt properties. Restart Command Prompt for the change to take effect.
5. Check the console's type again (as shown in step 3). NVDA should report that the object is of type `WinConsole`.
6. Disable "use legacy console" and restart Command Prompt.
7. Close the Python console and change "Windows Console support" to "legacy".
8. Check the console's type again (as shown in step 3). NVDA should report that the object is of type `WinConsole`.
9. Close the Python console and change "Windows Console support" to "automatic".
10. Check the console's type again (as shown in step 3). NVDA should report that the object is of type `WinConsoleUIA` on Windows 10 version 1803 and later, WinConsole otherwise.

### Text editing
1. Open Command Prompt.
2. Enter testing text: type "echo cactus", but do not press enter when finished. Depending on the states of the "speak typed characters" and "speak typed words" options, typed characters should be announced while typing (speak typed characters), and the word "echo" should be announced when space is pressed (speak typed words). This test should be repeated for all possible combinations of speak typed characters/words.
3. Press left arrow repeatedly. NVDA should announce the previously entered string backwards with each press of left arrow (i.e. s, u, t, c, a, c, space, o, h, c, e).
4. Press right arrow repeatedly. NVDA should announce the entered string in order, character-by-character.
5. Use control+leftArrow and control+rightArrow to move by word. NVDA should announce each word encountered.
6. Press home. NVDA should announce "e" (the first character entered).
7. Press end. NVDA should announce "blank".
8. Use the left arrow to position the caret on the "c" in "cactus".
9. Press backspace. NVDA should announce "space" to indicate the deleted character.
10. Press the space bar to re-insert the space. Use caret movement commands to verify that the space has been replaced.
11. Quickly and repeatedly press backspace to delete by character. NVDA should read the string backwards as text is deleted (as in step 3). The final character of the prompt (">") should not be announced. (Fails on Windows 10 version 1803, 1809 and 1903 as "space" is read as "blank" in only this instance, see [#10036](https://github.com/nvaccess/nvda/issues/10036)).
12. Re-enter the testing text, as shown in step 2.
13. Press control+backspace repeatedly to delete by word. NVDA should report each word as it is deleted.
14. Re-enter the testing text, as shown in step 2.
15. Press home.
16. Press shift+rightArrow repeatedly. NVDA should announce each  character as it is selected (i.e. "e selected", "c selected", "h selected", etc). (fails on Windows 10 1803 and 1809 likely due to a Microsoft bug).
17. Press control+shift+leftArrow repeatedly. NVDA should announce each word as it is unselected (i.e. "cactus unselected", "echo unselected"). (fails on Windows 10 version 1803, 1809 and 1903, but may be fixed once [#9660](https://github.com/nvaccess/nvda/pull/9660) is completed and merged)
18. With a Braille display connected, move the system caret. The Braille display should properly track caret movement. (Testing performed by [Leonard](https://github.com/leonardder) on Windows 10 version 1903).

### Automatic readout
1. Open Command Prompt.
2. With "report dynamic content changes" enabled, enter "echo". NVDA should report that echo is on and read the prompt automatically.
3. Enter "ping google.com". On Windows 10 version 1607 and later, NVDA should say "pinging google.com" (as words) and read the responses automatically. It should not read the output as characters (i.e. p i n g i n g etc). Pressing control+c should read the results and prompt.
4. Run the C program attached in [#6291](https://github.com/nvaccess/nvda/issues/6291). If many `textChange` events are fired very quickly, automatic readout should stop to maintain system stability, but NVDA should not freeze and full console functionality should be restored when NVDA is restarted.
5. Maximize the window and enter "echo" again, as shown in step 2. Automatic readout should remain functional.
6. Restore the window and enter "echo" again, as shown in step 2. Automatic readout should still work.
7. Repeat steps 2–6 with "report dynamic content changes" disabled. No output should be automatically reported.

### Text review
1. Open Command Prompt.
2. Attempt to review the console window by character, word, and line. The console contents should be accessible via text review. (on Windows 10 1803, movement by character is not constrained to the current line, and word movement across lines is sometimes unreliable, see [#10120](https://github.com/nvaccess/nvda/issues/10120)).
3. Attempt to review beyond the console bounds (such as by manually using review previous/next line to go to the top and bottom of the window). The review cursor should be constrained to the text visible onscreen.
4. Invoke review top line (desktop layout: shift+numpad 7). The first visible line of the console should be read.
5. Invoke review bottom line (desktop layout: shift+numpad 9). The last visible line of the console should be read. (On Windows 10 version 1803, "review bottom line" causes the review cursor to be placed outside the visible text, disabling range checks. On Windows 10 version 1903, the review cursor is placed near the bottom line but NVDA says "blank". See [#10119](https://github.com/nvaccess/nvda/issues/10119)).
6. Move the review cursor a few characters/words, and then invoke review first character (desktop layout: shift+numpad 1). The first character of the line under review should be read.
7. Invoke say all in review (desktop layout: numpad +). NVDA should read from the current review cursor position to the end of the visible text.
8. Move the caret to a line of output (desktop layout: NVDA+shift+numpad minus twice quickly), then perform a say all (desktop layout: NVDA+downArrow). NVDA should read from the current caret position to the end of the visible text.
9. Maximize the console window and attempt review. While the review cursor may no longer be constrained to the visible text, it should remain functional.
10. Restore the console window and attempt review. While the review cursor may no longer be constrained to the visible text, it should remain functional.

### Password entry
1. Open Command Prompt.
2. Use `ssh` to connect to a remote system with password authentication, then enter text at the password prompt. If "speak passwords in Windows Console" is enabled, NVDA should respect "speak typed characters" and "speak typed words" settings for password entry. If disabled, NVDA should not announce any password characters as they are entered.
3. With password announcement disabled, press enter after typing the password. Password characters should not be spoken once enter is pressed.
4. Attempt password authentication again, as shown in step 2, but press control+c during password entry. NVDA should not announce the previously typed characters.

### Speak typed words
1. Enable "speak typed words".
2. Open Command Prompt and navigate to a `git` repository.
3. Enter "git log". After pressing enter, the word "log" should not be announced.
4. Press q to close the log pager, then type "git" and press space. Nvda should say "git", not "qgit".
5. Type "ec", then Press control+c, then type "ho" and press space. NVDA should say "ho", not "echo".
6. Access a Debian-based Linux system, either in the Windows Subsystem for Linux or Command Prompt over `ssh`.
7. Enter "apt inst", and press tab. Nvda should say "all" (the characters which complete the word "install"), not "inst all".

### Short tab completions
1. Open Command Prompt.
2. Create a directory called abc ("md abc").
3. type "cd a", and then press tab. NVDA should report "bc".
4. Delete the entered text, then type “cd ab” followed by tab. NVDA should report “c”. (fails even in legacy console, see [#6095](https://github.com/nvaccess/nvda/issues/6095)).

### Speech interrupt
1. Disable "speech interrupt for typed characters" and "speak typed characters".
2. Open Command Prompt.
3. Type "date". While NVDA is reading, enter text. NVDA should continue reading the text during user input.

### Console focus
1. Open Command Prompt.
2. Press alt+space to invoke the system menu, and select paste from the edit menu.
3. Attempt to review text. The console should remain functional.
4. Switch away from the console (such as with alt+tab).
5. Switch back to Command Prompt. NVDA should not report a selection. (No selection was reported, but the terminal is announced twice, see [#10030](https://github.com/nvaccess/nvda/issues/10030)).

## Next steps
### Consider not enabling UIA console by default on Windows 10 version 1803
Due to text review issues ([#10119](https://github.com/nvaccess/nvda/issues/10119) and [#10120](https://github.com/nvaccess/nvda/issues/10120)), we may wish not to enable UIA in consoles automatically on Windows 10 1803 unless or until solutions can be found. The needed changes to implement this have been made in [#10129](https://github.com/nvaccess/nvda/pull/10129).

### Investigate outstanding console UIA issues
The following issues with UIA console support should be prioritized for investigation before the 2019.3 release:

* repetition when focusing a console window ([#10030](https://github.com/nvaccess/nvda/issues/10030))
* UIA in Windows consoles: spaces are stripped from end of line, blank reported when arrowing through them ([#10036](https://github.com/nvaccess/nvda/issues/10036))
* Incorrect behavior of "review bottom line" in Windows Console ([#10119](https://github.com/nvaccess/nvda/issues/10119))

### Automated tests
Manually running through the console test plan is time consuming, doubly so when testing across Windows versions and system configurations. System tests should be written to automate this testing, so that full console functionality can be verified when code changes are made.

Much of this project involved finding and fixing bugs in the UIA console's `textInfo` implementation. Since `textInfo` objects are expected to implement a common interface, it would be useful to write a testing module for these objects. Given a predefined initial state and a `textInfo` from a running application (i.e. one set at `POSITION_CARET`), the module would perform all of the operations `textInfo` objects should support and compare observed and expected outputs. Such a module would help insure that further breaking changes are not implemented in the console's `textInfo` in later Windows releases.