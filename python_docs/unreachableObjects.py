# -*- coding: utf-8 -*-
documentation = [
_(u"""# Garbage collection errors"""),
_(u"""NVDA's `garbageHandler.py` monitors Python's cyclic garbage collector and reports"""),
_(u"""on objects that are unreachable."""),
_(u"""Cyclic references are typically a symptom of bad design, and can cause major problems for certain objects."""),
_(u"""For instance, cyclic references involving COM objects may cause a deadlock if the garbage collector happens to break the cycle and release the COM object in the wrong thread."""),
"",_(u"""## How to know about a cyclic reference?"""),
_(u"""The log may contain errors like the following."""),
_(u"""```"""),
_(u"""WARNING - garbageHandler.notifyObjectDeletion (10:45:23.171) - MainThread (21820):"""),
_(u"""Garbage collector has found one or more unreachable objects. See further warnings for specific objects."""),
_(u"""..."""),
_(u"""WARNING - garbageHandler.notifyObjectDeletion (10:45:23.171) - MainThread (21820):"""),
_(u"""Deleting unreachable object <eventHandler._EventExecuter object at 0x1AC15350>"""),
_(u"""ERROR - garbageHandler._collectionCallback (10:45:23.172) - MainThread (21820):"""),
_(u"""Found at least 1 unreachable objects in run"""),
_(u"""```"""),
"",_(u"""## How to debug a cyclic reference?"""),
"",_(u"""Once you can reliably reproduce the log error, you can tell the garbage collector to save all unreachable objects."""),
_(u"""After an unreachable object is detected the references to the unreachable object can be inspected via the python console."""),
_(u"""Inspecting this should give you a fair idea of where the issue is occurring."""),
"",_(u"""1. Open the NVDA Python console `NVDA+control+z`"""),
_(u"""1. Enable saving all objects:"""),
_(u"""   ``` python"""),
_(u"""   import gc"""),
_(u"""   gc.set_debug(gc.DEBUG_SAVEALL)"""),
_(u"""   ```"""),
_(u"""1. Reproduce the unreachable object error."""),
_(u"""1. If garbage collection errors have not yet been logged, force a collect by calling:"""),
_(u"""   ``` python"""),
_(u"""   gc.collect()"""),
_(u"""   ```"""),
"",_(u"""1. All unreachable objects will now be stored in `gc.garbage`."""),
_(u"""   It may be a very large list."""),
_(u"""   Some tricks for narrowing this list down:"""),
_(u"""   - From the log, you can get the memory address (`id`) of the object."""),
_(u"""     Then use:"""),
_(u"""     ``` python"""),
_(u"""     memoryAddress = 0xabcd123"""),
_(u"""     obj = None"""),
_(u"""     for o in gc.garbage:"""),
_(u"""     	if memoryAddress == id(o)"""),
_(u"""     		obj = o"""),
_(u"""     ```"""),
_(u"""   - Listing the types collected, look for the type(s) matching the log message:"""),
_(u"""     ``` python"""),
_(u"""     for index, o in enumerate(gc.garbage):"""),
_(u"""     	print(index, type(o))"""),
_(u"""     ```"""),
_(u"""1. Once you have a reference (`obj`) to the unreachable object, see what other objects refer to an object you can call."""),
_(u"""   You can do this by using `gc.get_referrers`."""),
_(u"""   The python console has a reference to `obj`, there may be a lot of output."""),
_(u"""   You can reduce this by looking at the types and following the most relevant."""),
_(u"""   ``` python"""),
_(u"""   for index, o in enumerate(gc.get_referrers(obj)):"""),
_(u"""   	print(index, type(o))"""),
_(u"""   ```"""),
_(u"""1. Continue following the references to build a picture of the cycle."""),
"",_(u"""## Typical problems"""),
_(u"""Some examples of common issues:"""),
_(u"""- Exceptions caught and assigned to a local variable."""),
]