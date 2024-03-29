# -*- coding: utf-8 -*-
documentation = [
_(u"""The NVDA API must maintain compatibility with add-ons throughout yearly development cycles."""),
_(u"""The first release of a year, i.e. `20XX.1`, is when the NVDA API can introduce breaking changes."""),
"",_(u"""In order to improve the NVDA API, changes that will break future compatibility can be implemented, as long they retain backwards compatibility until the `20XX.1` release."""),
"",_(u"""This can be done by using a version check to automate deprecation. For example, if you wish to replace usages of `foo` with `bar`. When we begin work on `NEXT_YEAR`, `foo` will no longer be part of the NVDA API and all internal usages must be removed prior. """),
_(u"""```python"""),
_(u"""from buildVersion import version_year"""),
_(u"""if version_year < NEXT_YEAR:"""),
_(u"""	foo = bar"""),
_(u"""```"""),
"",_(u"""To ensure a module retains the same symbol names being importable, check across versions what is imported using the NVDA python console."""),
_(u"""```python"""),
_(u"""import controlTypes"""),
_(u"""dir(controlTypes)"""),
_(u"""```"""),
"",_(u"""Changes different to moving or renaming symbols need to be considered carefully with a different approach. """),
"",_(u"""Any API breaking changes such as deprecations marked for removal should be commented with the year of intended removal, and notes on how to implement the API change as an add-on developer and NVDA developer."""),
]