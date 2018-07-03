# Log Files and Crash Dumps

## Log Files
When reporting problems, it is often useful to provide an NVDA log file. This file shows what NVDA was doing when the problem occurred. Sometimes, a particular problem is difficult to reproduce or not reproduceable at all on other systems, so the log file can act as a further description or recording of the problem as it happened.

A log file should be attached to a GitHub issue at the same time or after it is created. It is important not to simply paste fragments or entire log files in to an issue comment, as this clutters the issue and may mangle certain information needed from the log.

### Log levels

By default, NVDA's log level is set to `Info`. This means that only informational messages, warning messages and major error messages are logged. This level of logging may be useful for crashes of NVDA or when nothing better is available. However, in order to provide much more detail, you can set NVDA's log level to `Debug` (In General Settings under Preferences in the NVDA menu) before the error occurs. Setting the log level to `Debug` tells NVDA to also log information such as what keys were pressed, what was spoken and other messages to help developers diagnose problems. Although this detail will help a great deal in solving the issue, please be aware that because key presses and spoken messages are logged, the log may contain personal information.

### Collecting the log file

To retrieve a log file to be attached to an issue, after the problem occurs and before closing NVDA, do the following:

1. Open the log viewer found under Tools in the NVDA menu. 
2. In the log viewer, choose Save As from the Log menu, and save the file to a place of your choice.
3. Finally, this file you have saved can be attached to an issue on GitHub.

If you have already closed NVDA or NVDA crashed, you can always find the log file for the last time NVDA was running. For most users, this file can be found in the [user temporary folder](#user-temporary-folder) `%temp%`. If you have not started NVDA since it last exited (e.g. you have some sight or are using another screen reader), the file you want is `nvda.log`. If you have started NVDA since it last exited, the file you want is `nvda-old.log`. For those running from source, these files are in the source directory.

## Crash Dumps
This applies to NVDA 2014.1 and later. Earlier versions do not generate crash dumps.

If NVDA crashes, it will generate a file called a minidump which will help developers to determine the cause of the crash. In addition, minidumps can also be generated on request for other applications which crash if NVDA is suspected as the cause of the crash.

### Minidumps for NVDA Itself
When NVDA crashes, it will usually restart itself. In some rare circumstances, this may not work. If NVDA crashes, a minidump will be generated in a file called nvda_crash.dmp. For most users, this file can be found in the [user temporary folder](#user-temporary-folder) `%temp%`. For users running from source, `nvda_crash.dmp` will be placed in the source directory.

### Minidumps for Other Applications
If an application you are using is crashing and NVDA is the suspected cause, you can request that a minidump be generated when that application crashes. You should generally only do this if requested by a developer or if you are an advanced user. This is not enabled by default and it needs to be enabled for each application after it is started. To enable it for a given application:

1. Switch to the application.
2. Press `NVDA+control+z` to open the NVDA Python console.
3. Type the following command exactly as it appears (you will probably want to copy and paste it):

    ```
    focus.appModule.dumpOnCrash()
    ```

4. Press enter.
5. The path to the file that will be generated will be presented. If you wish to copy it, you can press `F6` to move to the console output.

These dumps will always be placed in the [user temporary folder](#user-temporary-folder) `%temp%`. They are named in the form nvda_crash_appName_processId.dmp, where appName is the name of the application's executable file.

### Alternative Way to Get Minidumps for Other Applications
Sometimes, the method described above (having NVDA generate a minidump when an application crashes) doesn't work; no minidump is generated. Instead, you can configure Windows to collect minidumps when any application crashes. To do this:

For users experienced with the Registry: Create the following (empty) key: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps`

More detailed instructions for users who aren't familiar with the registry (though this should generally not be attempted by users without some technical knowledge of Windows):

1. Press Windows+r and type `regedit` to open the Registry Editor.
2. Move to the following key: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Windows Error Reporting`
    - If you're running Windows 10, you can simply paste this into the address bar in the Registry Editor and press enter.
    - Otherwise, use the tree to locate the key, where the backslashes indicate deeper levels of the tree.
3. Open the context menu for the `Windows Error Reporting` key and select New -> Key.
4. Type `LocalDumps` exactly as it appears and press enter.

When an application crashes, it will display the standard Windows application crash dialog. Once that dialog is closed, the crash dump will be placed in `%localappdata%\CrashDumps`.

You should disable this once you have collected the dump you're interested in, as otherwise, dumps will be collected for all future crashes and consume disk space. To disable this, just delete the `LocalDumps` key you created earlier.

See the [Collecting User-Mode Dumps MSDN article](https://msdn.microsoft.com/en-us/library/windows/desktop/bb787181(v=vs.85).aspx) for more information about this functionality.

### Attaching Minidumps to Issues
In order to attach a minidump to a GitHub issue, you will need to place it in a zip archive. You can do this by navigating to the minidump file in File Explorer, activating the context menu, selecting Send to and then selecting Compressed (zipped) folder.

## User Temporary Folder
The user temporary folder can be accessed by typing `%temp%` in most places where a folder name can be typed. For example, you can type this in the address bar of File Explorer, the Run dialog accessed by pressing `Windows key+r` or a file open or browse dialog.