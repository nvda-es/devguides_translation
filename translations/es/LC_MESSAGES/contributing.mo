��    w      �  �   �      
  (   
  E   B
     �
  C   �
  >   �
  >   &     e  	   h     r     y     �  �   �  ]  �  /   �  !   '  E   I  '   �     �  `   �  v   6     �  G   -  �   u  K   0  W   |  �   �  Y   \  X   �  W     �   g  �   "  �   �  d   �  P   �  a   N  C   �  A   �     6      =     ^     u     �  ?   �  �   �  [   \  �   �  �   �  e   $  ]   �  �   �  _   l  �   �     X  z   x  w   �  ]   k     �  7   �          &  "   A  [   d  
   �     �     �     �     �          !  ,   :  ;   g  %   �  "   �  .   �  !         =   �   ?   �   �       O!  m   p!  j   �!  �   I"     �"  �   #  A   �#  �   �#     �$     #%  �   ;%  S   �%  �   G&     �&  %   '  �   5'  �   �'  D   �(      �(  T   �(  �   I)  �   �)  [   v*  ;   �*  Q   +  o   `+  Y   �+  [   *,  �   �,  N   !-     p-  N   �-  $   ?.  U   d.  3   �.  G   �.  T   6/    �/     �0  $   �0  l  �0  (   A2  E   j2     �2  C   �2  >   3  >   N3     �3  	   �3     �3     �3     �3    �3  �  �4  >   e6  &   �6  ^   �6  $   *7  %   O7  |   u7  �   �7  �   �8  }   "9    �9  M   �:  S   �:  �   I;  k   �;  m   L<  R   �<  �   =  �   �=  �   �>  |   I?  O   �?  {   @  L   �@  `   �@     @A      GA     hA     A     �A  ?   �A  �   �A  o   vB  �   �B  �   �C  q   xD  �   �D  �   rE  [   F  �   ^F     �F  �   G  }   �G  �   %H     �H  7   �H     �H  )   I  3   :I  �   nI  
   �I     J     J     .J     :J     YJ     gJ  2   J  A   �J  1   �J  9   &K  8   `K  )   �K     �K  �   �K  �   �L  !   ,M  �   NM  �   �M  �   iN     *O  �   BO  R   �O  �   6P  �   5Q     R  �    R  i   �R  �   9S     T  ,   T  �   CT  �   U  P   �U  0   OV  [   �V  �   �V  �   dW  o   X  J   �X  Q   �X  o   +Y  Y   �Y  [   �Y  �   QZ  O   [  �   b[  M   �[  $   =\  \   b\  3   �\  7   �\  z   +]  �   �]     �^  $   �^     "   0      \          _   H   F      V         h       B   .   N      [   J      g   i   T   ;      )   9                             a              M         u      '   l   ]       d   `   4       Z   R       m              c               E   !   X   r          3   ?   f   	   b      Q   q      L   I                       ,   Y   s                  -       /   w             n   o      C   8   p   S   A       @   &   <       (   +       7       :   U       1      >   P          v   #       
   5       W          =       %   j   2       G   k                  ^   6   e       D   K       *   $   O       t          		" (requires administrator privileges)" 		"Use currently saved settings during sign-in and on secure screens" 		# Control (UAC) dialog). 		# Translators: The label for a button in general settings to copy 		# current user settings to system settings (to allow current 		# settings to be used in secure screens such as User Account 	) 	label=_( 	self,         # -*- coding: UTF-8 -*-         ```     * There should be no Unicode BOM at the start of the file, as this unfortunately breaks one of the translation tools we use (`xgettext`). Instead, include this as the first line of the file (only if the file contains non-ASCII characters):     * This coding comment must also be included if strings in the code (even strings that aren't translatable) contain escape sequences that produce non-ASCII characters; e.g. `"\xff"`. This is particularly relevant for braille display drivers. This is due to a `gettext` bug; see https://github.com/nvaccess/nvda/issues/2592#issuecomment-155299911.    # Add a remote for the NV Access repository.    # Fetch the nvaccess branches.    # Set the local master to use the nvaccess master as its upstream.    # Switch to the local master branch.    # Update the local master.    - If possible for your PR, please consider creating a set of unit tests to test your changes.    - Run `rununittests` (`rununittests.bat`) before you open your Pull Request, and make sure all the unit tests pass.    - The lint check ensures your changes comply with our code style expectations. Use `runlint nvaccess/master` (`runlint.bat`)    After a PR is merged, watch for feedback from Alpha users / testers.    All code should usually be based on the latest commit in the official master branch at the time you start the work unless the code is entirely dependent on the code for another issue.    Being proactive will really help to speed up the process of code review.    However, this branch will not be updated when the official master branch is updated.    If you are adding a feature or changing something that will be noticeable to the user, you should update the User Guide accordingly.    If you have cloned your GitHub fork, you can do this from the command line as follows:    Please fill out the Pull Request Template, including the checklist of considerations.    Please participate in this process, answering questions, and discussing the changes.    The checklist asks you to confirm that you have thought about each of the items, if any of the items are missing it is helpful to explain elsewhere in the PR why it has been left out.    This process requires core NVDA developers to understand the intent of the change, read the code changes, asking questions or suggesting changes.    To ensure your work is always based on the latest commit in the official master branch, it is recommended that your master branch be linked to the official master branch, rather than the master branch in your GitHub fork.    When the PR is approved it will be merged, and the change will be active in the next Alpha build.    When you fork the repository, GitHub will create a copy of the master branch.    When you think a contribution is ready, or you would like feedback, open a draft pull request.    When you would like a review, mark the PR as "ready for review".    You may have to follow up to address bugs or missed use-cases.    ```    git branch -u nvaccess/master    git checkout master    git fetch nvaccess    git pull    git remote add nvaccess https://github.com/nvaccess/nvda.git   * `Action`: Prefixed with `pre_` or `post_` to specify that handlers are being notified before / after the action has taken place.   * `Decider`: Prefixed with `should_` to turn them into a question eg `should_doSomething`   * `Filter`: TBD. Ideally follows a similar style the others, and communicates if the filtering happens before or after some action. It would also be nice to have a naming scheme that differentiates it from the others.   - Be aware that this requires a new-line after an opening parenthesis/bracket/brace if you intend to split the statement over multiple lines.   - Consider starting a discussion on mailing lists (EG NVDA developers) to see if there is interest.   - E.G. a fix for a typo/obvious coding error or a simple synthesizer/braille display driver   - For the parameter list of function definitions, double indent, this differentiates the parameters and the body of the function.   - Please understand that we very likely will not accept changes that are not discussed first.   - This allows us to discuss these aspects and any other concerns that might arise, thus potentially avoiding a great deal of wasted time.   - This should be fairly rare.   - name constants to avoid "magic numbers" and hint at intent or origin of the value. Consider, what does this represent?   - should try to use the positive form of the language (to avoid double negatives like `shouldNotDoSomething = False`)   - start with a "question word" to hint at their boolean nature. EG `shouldX`, `isX`, `hasX` # Contributing to NVDA # Translators: The name of a category of NVDA commands. ## Code Style ## Code/Docs contributions ## Issue triage and investigation: ## Note: Currently only accepting bug-fix / maintenance PR's only while addressing backlog. ## Testing ### Encoding ### GitHub process: ### Guidelines: ### Identifier Names ### Indentation ### Translatable Strings #### 1. "fork" the NVDA repository on GitHub #### 2. Use a separate "topic" branch for each contribution #### 3. Run unit tests and lint check #### 4. Create a Pull Request (PR) #### 5. Participate in the code review process #### 6. Feedback from Alpha users ) * All strings that could be presented to the user should be marked as translatable using the `_()` function; e.g. `_("Text review")`. * All translatable strings should have a preceding translators comment describing the purpose of the string for translators. For example: * Boolean functions or variables * Classes should use mixed case to separate words, starting with an upper case letter; e.g. `BrailleHandler`. * Constants should be all upper case, separating words with underscores; e.g. `LANGS_WITH_CONJUNCT_CHARS`. * Event handlers are prefixed with "event_", and are often in the form "event_ACTION" or "event_OBJECT_ACTION". Where OBJECT refers to the class type that the ACTION refers to. * Extension points: * Functions, variables, properties, etc. should use mixed case to separate words, starting with a lower case letter; e.g. `speakText`. * Indentation must be done with tabs (one per level), not spaces. * Lengthy translatable strings can be split across multiple lines, taking advantage of Python's implicit line joining inside parentheses. Translators comment can span multiple lines as well. For example: * Most files should contain `CRLF` line endings, as this is a Windows project and can't be used on Unix-like operating systems. * Use descriptive names * When splitting a single statement over multiple lines, just indent one or more additional levels. Don't use vertical alignment; e.g. lining up with the bracket on the previous line. * Where Python files contain non-ASCII characters, they should be encoded in UTF-8. - A minor/trivial change which definitely wouldn't require design, user experience or implementation discussion, you can just create a pull request rather than using an issue first. - By testing NVDA - Code or documentation contributions - For anything other than minor bug fixes, please comment on an existing issue or create a new issue providing details about your proposed change. - If in doubt, use an issue first. Use this issue to discuss the alternatives you have considered in regards to implementation, design, and user experience. Then give people time to offer feedback. - Include information about use cases, design, user experience, etc. - Issue triage and investigation - It is recommended to wait for acceptance of your proposal before you start coding. - Recent change focused testing: By following the changes that are being made to NVDA and purposefully testing these changes and looking for edge-cases. - Regression testing: Testing older features and behavior to look for unintended regressions in behavior that don't seem related to recent changes. - Unfocused usage: Just use NVDA as you normally would, and try to complete everyday tasks. - Unrelated changes should be addressed in separate issues. - [label:Abandoned ](https://github.com/nvaccess/nvda/issues?q=label%3AAbandoned) - [label:closed/needs-new-author ](https://github.com/nvaccess/nvda/issues?q=label%3Aclosed%2Fneeds-new-author) - [label:goodForNewDev ](https://github.com/nvaccess/nvda/issues?q=label%3AgoodForNewDev) - [label:goodfirstissue](https://github.com/nvaccess/nvda/issues?q=label%3Agoodfirstissue+) Code style is enforced with the flake8 linter, see [`tests/lint/readme.md`](https://github.com/nvaccess/nvda/tree/master/tests/lint) for more information. For more information please see: https://github.com/nvaccess/nvda/issues/11006 Forming a group can help you to get good coverage, brainstorm on what should be tested, and perhaps learn new ways to use NVDA. If you are new to the project, or looking for some way to help take a look at: SCRCAT_TEXTREVIEW = _("Text review") Testing alpha / beta / and release candidates help to ensure the quality of the NVDA. There are several approaches you may take for this: There are several ways in which you can contribute to the NVDA project: User / community testing is particularly important for languages other than English. You can also make non-code contributions by helping process incoming GitHub issues. For information on this please see the [triage process](https://github.com/nvaccess/nvda/wiki/Triage-process) and [issue triage help](https://github.com/nvaccess/nvda/wiki/Issue-triage-help) on the wiki. ``` self.copySettingsButton = wx.Button( Project-Id-Version: 
Report-Msgid-Bugs-To: 
PO-Revision-Date: 2021-05-16 14:58+0200
Last-Translator: José Manuel Delicado <jmdaweb@hotmail.com>
Language-Team: 
Language: es
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Generated-By: pygettext.py 1.5
X-Generator: Poedit 2.4.3
Plural-Forms: nplurals=2; plural=(n != 1);
 		" (requires administrator privileges)" 		"Use currently saved settings during sign-in and on secure screens" 		# Control (UAC) dialog). 		# Translators: The label for a button in general settings to copy 		# current user settings to system settings (to allow current 		# settings to be used in secure screens such as User Account 	) 	label=_( 	self,         # -*- coding: UTF-8 -*-         ```     * No debería haber bom Unicode al principio del archivo, ya que esto desafortunadamente rompe una de las herramientas de traducción que usamos (`xgettext`). En su lugar, incluye esto como primera línea del archivo (sólo si el archivo contiene caracteres no ASCII):     * Deberás incluir esta línea si las cadenas del código (incluso si estas no son traducibles) contienen secuencias de escape que producen caracteres no Ascii, tales como `"\xff"`. Esto es particularmente importante para controladores de pantallas braille. El responsable del fallo es `Gettext`, como se puede ver en https://github.com/nvaccess/nvda/issues/2592#issuecomment-155299911.    # Añadir un origen remoto con el repositorio de NV Access.    # Descargar las ramas de NV Access.    # configurar la rama master local para que utilice por defecto la rama master de NV Access.    # Cambiar a la rama master local.    # Actualizar la rama master local.    - Si es posible para tu solicitud de cambios, plantéate crear un conjunto de pruebas unitarias para evaluar tus cambios.    - Ejecuta `rununittests` (`rununittests.bat`) antes de abrir tu solicitud de cambios, y comprueba que se superan todas las pruebas unitarias.    - La comprobación de estilo garantiza que tu código cumple con nuestras expectativas de estilo del código. Usa `runlint nvaccess/master` (`runlint.bat`)    Después de que se fusione una solicitud de cambios, estáte atento a los comentarios de los usuarios y evaluadores Alpha.    Todo el código debería basarse en el commit más reciente de la rama master oficial que hay en el momento en que empiezas a trabajar, a no ser que el código oficial sufra cambios drásticos que afecten a tu trabajo o dependa del código de otra incidencia.    Ser proactivo acelerará notablemente el proceso de revisión del código.    Sin embargo, esta rama no se actualizará cuando lo haga la rama master oficial.    Si vas a añadir algo de lo que el usuario se vaya a dar cuenta, deberías actualizar la guía de usuario convenientemente para reflejar tu cambio.    Si has clonado tu bifurcación de GitHub, puedes hacerlo desde la línea de órdenes del siguiente modo:    Rellena la plantilla de solicitud de cambios, incluyendo las consideraciones de la lista de comprobación.    Participa en este proceso, responde a las preguntas y debate sobre los cambios.    La lista de comprobación te pide que confirmes que has pensado en todos los elementos. Si falta alguno de ellos, viene bien explicar en algún lugar de la solicitud por qué se ha descartado.    Este proceso requiere que los desarrolladores principales de NVDA entiendan el propósito del cambio, lean los cambios en el código, hagan preguntas o sugieran modificaciones.    Para asegurarte de que tu trabajo siempre se basa en el último commit de la rama master oficial, se recomienda que vincules la copia de tu rama a la oficial en vez de la que hay en tu cuenta.    Cuando se apruebe la solicitud de cambio se fusionará, y dicho cambio estará activo en la siguiente compilación Alpha.    Cuando bifurques el repositorio, GitHub creará una copia de la rama master.    Cuando creas que una contribución está lista, o quieras recibir comentarios, abre un borrador de solicitud de cambios.    Cuando quieras una revisión, marca la solicitud como "ready for review".    Puedes tener que continuar para solucionar fallos o tener en cuenta casos de uso imprevistos.    ```    git branch -u nvaccess/master    git checkout master    git fetch nvaccess    git pull    git remote add nvaccess https://github.com/nvaccess/nvda.git     * `Action`: lleva el prefijo `pre_` o `post_` para especificar que se notifica a los manejadores antes o después de que la acción tenga lugar.     * `Decider`: lleva el prefijo `should_` para mostrarlo como una pregunta. Por ejemplo, `should_doSomething`     * `Filter`: por determinar. lo ideal es que siga el mismo estilo que los otros, y comunicar si el filtro ocurre antes o después de la acción. Sería estupendo tener también un esquema de nombres que lo diferencie de los otros.     - Sé consciente de que esto necesita un salto de línea después de abrir un paréntesis, corchete o llave si pretendes dividir la instrucción en varias líneas.   - Plantéate iniciar un debate por las listas de correo (por ejemplo NVDA Developers) para ver si hay interés.   - Por ejemplo, una corrección de un error obvio de codificación o escritura o un controlador simple de síntesis o pantalla Braille     - En la lista de parámetros de la definición de funciones, da un margen doble para diferenciar los parámetros del cuerpo de la función.   - Ten en cuenta que NV Access no aceptará cambios que no se hayan discutido previamente.   - Eso permitirá a los desarrolladores discutir los aspectos y consecuencias derivadas del cambio, y potencialmente evitará gastar tiempo inútilmente.   - Esto debería ser raro.     - nombra las constantes para evitar "números mágicos" y da una pista sobre la intención u origen del valor. Pregúntate ¿qué representa?     - deberían intentar usar la forma positiva del idioma (para evitar dobles negativos como `shouldNotDoSomething = False`)     - comienza con una "palabra de pregunta" para dar una pista sobre su naturaleza booleana. Ejemplos: `shouldX`, `isX`, `hasX` # Cómo contribuir con NVDA # Translators: The name of a category of NVDA commands. ## Estilo del código ## Contribuciones de código / documentos ## Clasificación en investigación de incidencias: ## Nota: actualmente sólo se aceptan solicitudes de cambio de mantenimiento o corrección de fallos mientras se procesa la cola existente. ## Pruebas ### Codificación ### Proceso de GitHub: ### Pautas: ### Nombres de identificadores ### Indentado ### Cadenas traducibles #### 1. "Bifurca" el repositorio de NVDA en GitHub #### 2. Usa una rama "temática" separada para cada contribución #### 3. Ejecuta las pruebas unitarias y de estilo #### 4. Crea una solicitud de cambios (PR o Pull Request) #### 5. Participa en el proceso de revisión del código #### 6. Comentarios de los usuarios Alpha ) * Todas las cadenas que se puedan mostrar al usuario deberían marcarse como traducibles usando la función `_()`. Por ejemplo, en vez de poner `"text review"` pondríamos en su lugar `_("text review")`. Todas las cadenas traducibles deberían estar precedidas por un comentario en inglés para traductores que describa claramente su propósito. Por ejemplo: * Funciones booleanas o variables * El caso anterior también se aplica para las clases, pero en vez de empezar en minúscula lo hacen en mayúscula; por ejemplo, `BrailleHandler`. * Las constantes siempre deben estar en mayúscula, separando las palabras con guiones bajos. Por ejemplo, `LANGS_WITH_CONJUNCT_CHARS`. * Los manejadores de eventos tienen el prefijo "event_", y tienen la forma "event_ACTION" o "event_OBJECT_ACTION", donde OBJECT hace referencia al tipo de clase a la que se refiere la acción. * Puntos de extensión: * Las funciones, propiedades, variables, etc. deberían usar mayúsculas para separar palabras, pero empezar con una letra minúscula; por ejemplo, `speakText`. * La indentación se debe hacer con tabuladores (uno por nivel) y no con espacios. * Se pueden dividir las cadenas traducibles largas en múltiples líneas, aprovechando la ventaja que ofrece la unión implícita de líneas entre paréntesis de Python. Los comentarios para traductores pueden ocupar varias líneas también. Por ejemplo: * La mayoría de los archivos deben contener saltos de línea en formato `crlf` de Windows. Este es un proyecto hecho exclusivamente para Windows, y no se puede usar en sistemas operativos derivados de Unix. * Usa nombres descriptivos * Al dividir una instrucción en varias líneas, indéntala con uno o más niveles. No uses alineación vertical del tipo “alinear con el corchete de la línea superior”. * Cuando los archivos Python contengan caracteres que no sean Ascii, deberán estar codificados en UTF-8. - Un cambio menor / trivial que no requiera definitivamente debates sobre diseño, experiencia de usuario o implementación puede ir directamente en una solicitud de cambio sin crear una incidencia antes. - Probando NVDA - Contribuciones de documentación o código - Para cualquier cosa distinta a la reparación de problemas pequeños, por favor comenta en una incidencia existente o crea una incidencia nueva exponiendo los detalles del cambio que propones. - Ante cualquier duda, usa una incidencia primero. Utilízala para debatir sobre las alternativas planteadas respecto a la implementación, el diseño y la experiencia de usuario. Después, da tiempo a la gente para que ofrezca retroalimentación. - Incluye información sobre casos de uso, diseño, experiencia de usuario, etc. - Clasificación e investigación de incidencias - Es recomendable esperar la aceptación de tu propuesta antes de que empieces a codificar. - Pruebas enfocadas a cambios recientes: siguiendo los cambios que se han hecho en NVDA y probándolos a propósito con casos extremos. - Prueba de regresiones: se prueban funciones antiguas y su comportamiento para buscar regresiones no intencionadas cuyo comportamiento no parezca relacionado con los cambios recientes. - Uso no enfocado: simplemente utiliza NVDA como lo harías normalmente, e intenta completar tareas cotidianas. - Los cambios no relacionados se deben gestionar en incidencias separadas. - [label:Abandoned ](https://github.com/nvaccess/nvda/issues?q=label%3AAbandoned) - [label:closed/needs-new-author ](https://github.com/nvaccess/nvda/issues?q=label%3Aclosed%2Fneeds-new-author) - [label:goodForNewDev ](https://github.com/nvaccess/nvda/issues?q=label%3AgoodForNewDev) - [label:goodfirstissue](https://github.com/nvaccess/nvda/issues?q=label%3Agoodfirstissue+) El estilo del código está reforzado por el comprobador de conformidad Flake8, visita [`tests/lint/readme.md`](https://github.com/nvaccess/nvda/tree/master/tests/lint) para más información. Para más información, consulta: https://github.com/nvaccess/nvda/issues/11006 Formar un grupo puede ayudar a obtener una buena cobertura, ideas sobre lo que se debe probar, y quizá aprender nuevas formas de usar NVDA. Si eres nuevo en el proyecto o buscas una forma de ayudar, echa un vistazo a: SCRCAT_TEXTREVIEW = _("Text review") Hacer pruebas sobre las Alfa / beta / candidatas a liberación garantiza la calidad de NVDA. Hay varios enfoques que se pueden tomar para ellas: Hay diversas maneras de colaborar con el proyecto NVDA: Las pruebas de los usuarios y de la comunidad en general son particularmente importantes con idiomas distintos al inglés. También puedes hacer contribuciones que no sean de código, ayudando a procesar las incidencias entrantes en GitHub. Para más información, consulta los documentos relacionados con la clasificación de incidencias en nuestra web. ``` self.copySettingsButton = wx.Button( 