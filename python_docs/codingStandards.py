# -*- coding: utf-8 -*-
documentation = [
_(u"""## Code Style"""),
"",_(u"""Python code style is enforced with the flake8 linter, see"""),
_(u"""[`tests/lint/readme.md`](https://github.com/nvaccess/nvda/tree/master/tests/lint)"""),
_(u"""for more information."""),
"",_(u"""### Encoding"""),
_(u"""* Where Python files contain non-ASCII characters, they should be encoded in UTF-8."""),
_(u"""    * There should be no Unicode BOM at the start of the file, as this unfortunately breaks one of"""),
_(u"""      the translation tools we use (`xgettext`)."""),
_(u"""      Instead, include this as the first line of the file (only if the file contains non-ASCII"""),
_(u"""      characters):"""),
_(u"""        ```"""),
_(u"""        # -*- coding: UTF-8 -*-"""),
_(u"""        ```"""),
_(u"""    * This coding comment must also be included if strings in the code (even strings that aren't"""),
_(u"""      translatable) contain escape sequences that produce non-ASCII characters; e.g. `\"\\xff\"`."""),
_(u"""      This is particularly relevant for braille display drivers."""),
_(u"""      This is due to a `gettext` bug; see"""),
_(u"""      https://github.com/nvaccess/nvda/issues/2592#issuecomment-155299911."""),
_(u"""* Most files should contain `CRLF` line endings, as this is a Windows project and can't be used on"""),
_(u"""  Unix-like operating systems."""),
"",_(u"""### Indentation"""),
_(u"""* Indentation must be done with tabs (one per level), not spaces."""),
_(u"""* When splitting a single statement over multiple lines, just indent one or more additional levels."""),
_(u"""  Don't use vertical alignment; e.g. lining up with the bracket on the previous line."""),
_(u"""  - Be aware that this requires a new-line after an opening parenthesis/bracket/brace if you intend"""),
_(u"""    to split the statement over multiple lines."""),
_(u"""  - For the parameter list of function definitions, double indent, this differentiates the"""),
_(u"""    parameters and the body of the function."""),
"",_(u"""### Identifier Names"""),
_(u"""* Use descriptive names"""),
_(u"""  - name constants to avoid \"magic numbers\" and hint at intent or origin of the value."""),
_(u"""    Consider, what does this represent?"""),
_(u"""* Functions, variables, properties, etc. use mixed case to separate words, starting with a lower"""),
_(u"""  case letter; e.g. `speakText`."""),
_(u"""* Boolean functions or variables"""),
_(u"""  - Prefer positive form of the language."""),
_(u"""    Avoid double negatives like `shouldNotDoSomething = False`"""),
_(u"""  - Start with a \"question word\" to hint at their boolean nature. EG `shouldX`, `isX`, `hasX`"""),
_(u"""* Classes should use mixed case to separate words, starting with an upper case letter;"""),
_(u"""  - E.G. `BrailleHandler`."""),
_(u"""* Constants should be all upper case, separating words with underscores;"""),
_(u"""  - E.G. `LANGS_WITH_CONJUNCT_CHARS`."""),
_(u"""  - Avoid unnecesary shared prefixes in constants. Instead, use an enum for related constants."""),
_(u"""* Event handlers are prefixed with \"event_\", subsequent words in camel case."""),
_(u"""  Note, `object` and `action` are separated by underscores."""),
_(u"""  - E.G.: `event_action` or `event_object_action`."""),
_(u"""  - `object` refers to the class type that the `action` refers to."""),
_(u"""  - Examples: `event_caret`, `event_appModule_gainFocus`"""),
_(u"""* Extension points:"""),
_(u"""  * `Action`"""),
_(u"""    - Prefixed with `pre_` or `post_` to specify that handlers are being notified before / after the"""),
_(u"""      action has taken place."""),
_(u"""  * `Decider`"""),
_(u"""    - Prefixed with `should_` to turn them into a question eg `should_doSomething`"""),
_(u"""  * `Filter`"""),
_(u"""    - TBD. Ideally follows a similar style the others, and communicates if the filtering happens"""),
_(u"""      before or after some action."""),
_(u"""    - It would also be nice to have a naming scheme that differentiates it from the others."""),
_(u"""* Enums should be formatted using the expected mix of above eg:"""),
_(u"""  ```python"""),
_(u"""  class ExampleGroupOfData(Enum):"""),
_(u"""      CONSTANT_VALUE_MEMBER = auto()"""),
_(u"""      @property"""),
_(u"""      def _formatMember(self): pass"""),
_(u"""  ```"""),
"",_(u"""### Translatable Strings"""),
_(u"""* All strings that could be presented to the user should be marked as translatable using the `_()`"""),
_(u"""  function; e.g. `_(\"Text review\")`."""),
_(u"""* All translatable strings should have a preceding translators comment describing the purpose of the"""),
_(u"""  string for translators. For example:"""),
_(u"""```"""),
_(u"""# Translators: The name of a category of NVDA commands."""),
_(u"""SCRCAT_TEXTREVIEW = _(\"Text review\")"""),
_(u"""```"""),
_(u"""* Lengthy translatable strings can be split across multiple lines, taking advantage of Python's"""),
_(u"""  implicit line joining inside parentheses."""),
_(u"""  Translators comment can span multiple lines as well."""),
_(u"""  For example:"""),
_(u"""```"""),
_(u"""self.copySettingsButton = wx.Button("""),
_(u"""	self,"""),
_(u"""	label=_("""),
_(u"""		# Translators: The label for a button in general settings to copy"""),
_(u"""		# current user settings to system settings (to allow current"""),
_(u"""		# settings to be used in secure screens such as User Account"""),
_(u"""		# Control (UAC) dialog)."""),
_(u"""		\"Use currently saved settings during sign-in and on secure screens\""""),
_(u"""		\" (requires administrator privileges)\""""),
_(u"""	)"""),
_(u""")"""),
_(u"""```"""),
"",_(u"""### Imports"""),
_(u"""* Unused imports should be removed where possible."""),
_(u"""  - Anything imported into a (sub)module can also be imported from that submodule."""),
_(u"""  - As a result, removing unused imports may break compatibility, and should be done in compatibility breaking releases (see `deprecations.md`)."""),
_(u"""* Unused imports will give a lint warning. These can be handled the following ways: """),
_(u"""  - If these imports are inteded to be imported from other modules, they can be done included in a definition for `__all__`. This will override and define the symbols imported when performing a star import, eg `from module import *`."""),
_(u"""  - Otherwise, with a comment like `# noqa: <explanation>`."""),
]