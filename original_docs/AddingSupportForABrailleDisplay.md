# Adding Support for a Braille Display

There are two options if you'd like to see an additional braille display supported by NVDA:

1. Request that NV Access develops a driver; or
2. Write a driver yourself.

## Request that NV Access Develops a Driver
Given our extremely limited resources and other priorities, it may be months before we can consider such a request.
However, we will endeavour to support additional displays if we are able.

In order for NV Access to develop a driver, we will need:

* Access to a physical display at our offices in Queensland, Australia for at least a month at no cost to NV Access (which means we will not cover the cost of any shipping to or from Australia);
* Technical documentation from the braille display vendor regarding how to communicate with the display;
* Permission from the vendor to distribute the NVDA driver as open source code;
* Any drivers, libraries, etc. from the vendor necessary to communicate with the display;
* Permission from the vendor to freely redistribute any drivers, libraries, etc. with NVDA; and
* Information about any key commands, etc. for the display that are common across screen raeders.

Note that if there are any significant changes to either NVDA or the display after the driver is initially developed, we may need further access to a physical display as above.

If you'd like to request that we support a display, please file [an issue on GitHub](https://github.com/nvaccess/nvda/issues/new) including as much of the above as you can.
At the very least, you should contact the braille display vendor and facilitate contact between them and us.

## Write a Driver Yourself
Since NVDA is open source, we will gladly accept braille display drivers written by others.
As with most of the rest of NVDA, braille display drivers are written in Python and must be licensed under the GNU General Public License version 2.

A braille display driver is a Python module containing a `BrailleDisplayDriver` class which inherits from the `braille.BrailleDisplayDriver` base class.
See [the code documentation for the `braille.BrailleDisplayDriver` class](https://github.com/nvaccess/nvda/blob/master/source/braille.py#L1751) for further details.

For drivers that should be integrated into the braille display auto detection framework, driver specific meta data has to be added to the [`bdDetect` module](https://github.com/nvaccess/nvda/blob/master/source/bdDetect.py). Note that, in order for braille display auto detection to be supported, a driver has to be thread safe. Data is written to thread-safe braille display drivers in the background, thus improving performance.

Here are some quick tips:

* If you want to communicate with the display via raw serial, HID or Bulk, see the [`hwIo` module](https://github.com/nvaccess/nvda/blob/master/source/hwIo.py).
 This is the preferred form of communication, since thread safety as well as support for automatic detection of displays can be guaranteed using this method.
The following drivers are considered good examples.
 * [`baum`](https://github.com/nvaccess/nvda/blob/master/source/brailleDisplayDrivers/baum.py)
 * [`brailliantB`](https://github.com/nvaccess/nvda/blob/master/source/brailleDisplayDrivers/brailliantB.py)
 * [`eurobraille`](https://github.com/nvaccess/nvda/blob/master/source/brailleDisplayDrivers/eurobraille.py)
 * [`hims`](https://github.com/nvaccess/nvda/blob/master/source/brailleDisplayDrivers/hims.py)
 * [`superBrl`](https://github.com/nvaccess/nvda/blob/master/source/brailleDisplayDrivers/superBrl.py)

 Also, the [`handyTech`](https://github.com/nvaccess/nvda/blob/master/source/brailleDisplayDrivers/handyTech.py) driver might be a good example of a driver that should support multiple models or protocols.
* If you need to use a dll to communicate with the display, you can use the Python `ctypes` module.
 However, we will generally not accept dlls, unless it is strictly necessary to use them.
 Also, dlls larger than 300 kb are generally not accepted for distribution with NVDA.
 Furthermore, note that problems in dlls are harder to debug, and that implementing support for the braille display auto detection framework might be impossible due to the non thread safety of the dll.
 The [`freedomScientific`](https://github.com/nvaccess/nvda/blob/master/source/brailleDisplayDrivers/freedomScientific.py) driver is a good example.
* If you need to use a COM object to communicate with the display, you can use the `comtypes` module.
 The same notes as for dlls apply.

See the [Contributing to NVDA](https://github.com/nvaccess/nvda/wiki/Contributing) document for information about code style, etc.
Once you have completed your driver, you can submit a pull request.