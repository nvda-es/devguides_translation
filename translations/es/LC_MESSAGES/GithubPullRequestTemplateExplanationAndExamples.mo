��    E      D  a   l      �     �     �  2   �     2  
   A  #   L     p     �     �     �  +   �  9   �  #   *     N     h  +   y     �     �     �     �               +  	   7     A  	   P     Z  T   i  D   �  E   	  2   I	  0   |	  +   �	  ,   �	  ,   
  K   3
  ;   
  [   �
  K     '   c  C   �  \   �  L   ,  =   y  <   �     �  +   �  $   "     G     ]     o     �  !   �     �  @   �  7     I   M  0   �  `   �     )     2  4   @  X   u  4   �  Z     :   ^  8   �     �  j  �     A     C  7   O     �     �  8   �  2   �       %     &   B  ?   i  K   �  3   �  $   )     N  =   c     �     �     �  <   �     /     E     c  	   y     �  	   �     �  P   �  Q     Y   d  E   �  D     /   I  0   y  9   �  Q   �  L   6  y   �  i   �  )   g  ]   �  �   �  d   r  :   �  c        v  :   x  5   �     �          !     5  $   H  (   m  U   �  4   �  i   !  R   �  t   �     S     \  8   i  V   �  ?   �  j   9  :   �  8   �               "          =       .   ?      
       1                    E       >       	   !                           #      6         0   ,   9      B          4   (   C      D   %      @                  7       )   A   ;             2       3   <                     &      :   $           8                          -   5   *           /      '       +            - Braille   - Different web browsers (Firefox, Chrome, Edge)   - Low Vision   - Speech # Creating PR's on the NVDA project ## Code Review Checklist ## The template ### Change log entry ### Change log entry: ### Context sensitive help for GUI changes. ### Description of how this pull request fixes the issue: ### Known issues with pull request: ### Link to issue number: ### Manual tests ### Pull Request description is up to date. ### Summary of the issue: ### System tests ### Testing strategy: ### UX of all users considered ### Unit tests ### User Documentation * Bug fixes * Changes * New features *Changes* *New features* - As a reviewer, please use this description to replicate the testing (if possible). - Be clear on steps another user can take to replicate your testing. - Clearly describing this helps alpha testers, and future developers. - Describe the coverage of automated system tests? - Describe the coverage of automated unit tests? - Discuss under "testing strategy" heading. - Discuss under "testing strategy" heading.  - Does the user documentation need updating? - Even if changes to the approach are described in the comments for the PR. - Future developers need a concise explanation of a change. - Have you considered possible regressions (related features or behaviours that may break)? - Have you ensured testing coverage across all supported operating systems? - How did you manually test the change? - How have you tested to ensure that your change works as intended? - If many NVDA settings are required, consider attaching a sample `nvda.ini` file to the PR. - Is the changed code already, or can it be covered by automated unit tests? - Is the described manual testing appropriate for the change? - New GUI options require context sensitive help assignment. > >   - "speak typed characters" is unchecked >   - "speak typed words" is checked > - Keyboard category > 1. Open notepad > 2. Type "hello" > 3. Press space > Expect "hello" to be announced. > In NVDA settings ensure that: A lead developer will update file when merging the pull request. A quick summary of the problem you are trying to solve. After each modification, check that the PR description is still accurate. Authors must keep the PR description up to date. Code must be reviewed (via a Pull Request on GitHub) before it can be accepted into the project. Example: For instance: Hopefully it helps to prevent items being forgotten. If the reviewer reaches the same conclusion as the author, no further work is necessary. More broadly, try to answer the following questions: These descriptions should be in the format: `"{Description of change}. (#{issue number})"` `Added a command to announce useful thing. (#WXYZ, #ABCD)` `Old command, now also uses new useful command. (#WXYZ)` ``` Project-Id-Version: 
Report-Msgid-Bugs-To: 
PO-Revision-Date: 2021-09-04 17:32+0200
Last-Translator: José Manuel Delicado <jmdaweb@hotmail.com>
Language-Team: 
Language: es
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Generated-By: pygettext.py 1.5
X-Generator: Poedit 3.0
Plural-Forms: nplurals=2; plural=(n != 1);
     - Braille   - Diferentes exploradores web (Firefox, Chrome, Edge)   - Baja visión   - Voz # Creación de solicitudes de cambio en el proyecto NVDA ## Lista de comprobación de revisión del código ## La plantilla ### Entrada en el registro de cambios ### Entrada en el registro de cambios: ### Ayuda sensible al contexto en cambios de interfaz gráfica. ### Descripción de cómo resuelve la incidencia esta solicitud de cambios: ### Problemas conocidos con la solicitud de cambio: ### Enlace al número de incidencia: ### Pruebas manuales ### La descripción de la solicitud de cambios está al día. ### Resumen de la incidencia: ### Pruebas del sistema ### Estrategia de pruebas: ### Experiencia de usuario planteada para todos los usuarios ### Pruebas unitarias ### Documentación de usuario * Fallos solucionados * Cambios * Nuevas características *Cambios* *Nuevas características* - Como revisor, usa esta descripción para replicar las pruebas (si es posible). - Sé claro en los pasos que otro usuario puede seguir para replicar tus pruebas. - Al describirlos claramente se ayuda a los evaluadores alfa y a futuros desarrolladores. - ¿Se describe la cobertura de las pruebas automatizadas de sistema? - ¿Se describe la cobertura de las pruebas unitarias automatizadas? - Debate bajo el encabezado "testing strategy". - Debate bajo el encabezado "testing strategy".  - ¿Es necesario actualizar la documentación de usuario? - Incluso si en los comentarios de la solicitud se describen cambios del enfoque. - Los desarrolladores futuros necesitan una explicación concisa del cambio. - ¿Te has planteado que pueda haber posibles regresiones (funciones o comportamientos relacionados que puedan romperse)? - ¿Te has asegurado de que hay una extensa cobertura de pruebas a través de varios sistemas operativos? - ¿Cómo probaste manualmente el cambio? - ¿Cómo has hecho las pruebas para asegurarte de que tus cambios funcionan como se esperan? - Si es necesario modificar muchos ajustes de NVDA, plantéate adjuntar un archivo `nvda.ini` de muestra a la solicitud de cambio. - ¿Se puede cubrir el código modificado (o ya está cubierto) con pruebas unitarias automatizadas? - ¿Es apropiada para el cambio la prueba manual descrita? - Las nuevas opciones de interfaz gráfica requieren una asignación de ayuda sensible al contexto. > >   - "Verbalizar caracteres al escribir" está desmarcada >   - "Verbalizar palabras al escribir" está marcada > - En la categoría teclado > 1. Abre el bloc de notas > 2. Escribe "hola" > 3. Pulsa espacio > Se espera que se verbalice "hola". > En las opciones de NVDA comprueba que: Un desarrollador principal actualizará el archivo al mezclar la solicitud de cambio. Un breve resumen del problema que intentas resolver. Después de cada modificación, comprueba bien que la descripción de la solicitud de cambios es precisa. Los autores deben mantener la descripción de la solicitud de cambios actualizada. El código debe revisarse (mediante una solicitud de cambios en GitHub) antes de que pueda aceptarse en el proyecto. Ejemplo: Por ejemplo: Con suerte, ayuda a que no se olviden algunos elementos. Si el revisor alcanza la misma conclusión que el autor, no es necesario más trabajo. Vayamos más allá, intenta responder las siguientes preguntas: Estas descripciones deberían seguir el formato: `"{Descripción del cambio}. (#{número de incidencia})"` `Added a command to announce useful thing. (#WXYZ, #ABCD)` `Old command, now also uses new useful command. (#WXYZ)` ``` 