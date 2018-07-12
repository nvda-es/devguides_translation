In most files (covered by the GNU GPL) use the following copyright header:

Replacing:
- `<YOUR NAME>` with your name.
- `<CREATED YEAR>` the year the file was created
- `<LAST UPDATED YEAR>`when the file was last updated. For new files this can be missing. E.g. a file created in 2017 might have `#Copyright (C) 2017`
```
# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) <CREATED YEAR>-<LAST UPDATED YEAR> NV Access Limited, <YOUR NAME>
# This file may be used under the terms of the GNU General Public License, version 2 or later.
# For more details see: https://www.gnu.org/licenses/gpl-2.0.html
```

Some files are covered by the GNU LGPL, for example the the controller client, and the examples. This allows someone to use them (or parts of them) as-is. In this case use the following header:

```
# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) <CREATED YEAR>-<LAST UPDATED YEAR> NV Access Limited, <YOUR NAME>
# This file may be used under the terms of the GNU Lesser General Public License, version 2.1.
# For more details see: https://www.gnu.org/licenses/lgpl-2.1.html
```

In some files an older style of referring to the contributors is used. The contributors is not a list of names and may just say something like:
`Copyright (C) 2006-2016 NVDA Contributors`. We are in the process of trying to convert these to the new style of explicit contributors. That process is a bit tricky. You have to use the git logs to figure out when the file was created and who touched it and then build a copyright line accordingly.

**Note:**
We decided to remove the filename comment from the top of the file, since it doesn't really add anything, and is a source of error on file rename / copying copyright headers between files.
