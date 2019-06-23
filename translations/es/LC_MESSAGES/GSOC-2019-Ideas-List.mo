��    Y      �     �      �     �  �   �     i  
  �     �	     �	     �	  \   �	  ^   
  ,   p
  &   �
  -   �
  $   �
  :     9   R  )   �  3   �  0   �          '     ;     L  @   ]  9   �  k   �  �   D  �     �   �  �   �  �   v  �     �   �    q  �   z    6  �   M  ~   /  �   �  (  r  �   �  �   E  d     L   x    �  M   �  K    �   f  �   =  �   �  �   �     x!  �  "  O   =%    �%  Q   �'  L   �'     >(  D   S(  �   �(  o   M)  f  �)  �  $+  H   -  �  d-  e  ^/  �  �0  t   i2    �2  H   �3  K  .4  �   z5  �   q6    �6  E  8  �   Q9  �  �9  �   j;  �   <  �   �<  �   i=  =  I>  �   �?  2  /@  �   bA  F  PB  /  �C  �   �D  m   ME  �  �E     LG  �   NG      *H  0  KH     |I     �I     �I  c   �I  x   J  8   �J  A   �J  (   K  +   -K  B   YK  D   �K  .   �K  ?   L  3   PL     �L     �L     �L     �L  @   �L  9   	M  �   CM  �   �M  �   �N    mO  �   �P  �   PQ  �   �Q  �   �R  /  �S  �   �T    �U    �V  �   �W  �   IX  1  2Y  �   d[  �   \  �   �\  ?   �]  �   �]  Y   �^  e  _  �   }`  �   ua  �   =b  �   c  -  �c    e  l   h  H  �h  h   �j  ]   =k     �k  M   �k  �   l  u   �l  �  <m    �n  T   �p  @  q  �  Ys    �t  a   
w    lw  M   xx  �  �x  :  nz  �   �{  =  2|  t  p}  �   �~  �  �  �   |�  �   1�  �   т  �   ��  �  ��  �   -�  h  (�    ��  V  ��  4  ��  �   .�  w   ��                 N                     <       U         3      J       E          +   )   D      V          -   '   ,      &             L                  M      !          ;   B   	           "   :      2       *          5   I   8           0   .       ?   T       
       H   W   9           4      =   Q   @                G           S      C                   O   X          1      /   #   Y      P           %   A   6   $   R   F      7   (         >      K                   Perhaps some kind of template language could be used to represent the order, along with a suitable UI that could allow the average user to be able to insert, remove and reorder properties.  Related issues: #7232  This UI would have to allow separate configuring for both speech and braille, and may go as far as separate configurations for both browse mode and focus mode (i.e. reporting controls embedded in a document such as a link, verses a stand-alone control in a dialog). ## Ideas ## Introduction ### 64 bit NVDA ### Customize order and inclusion of object and formatting information to speech and braille ### Improve performance of reading/navigating Microsoft excel by batching COM calls in process ### Improve stability of NVDA's audio output ### Improve the UX of the NVDA updater ### Integrate NVDA with the windows magnifier ### Lazy population of Elements list ### Move input / accessibility API event handlers into c++ ### Performance and stability in windows command consoles ### Performance measuring system for NVDA #### Accuracy of Speak typed characters in consoles #### Closing consoles with the mouse kills NVDA! #### Impact #### Implementation #### Performance #### The problem * Michael Curran <mick@nvaccess.org> (@michaeldcurran on Github) * Reef Turner <reef@nvaccess.org> (@feerrenrut on Github) - Administrative access is no longer required to update NVDA (we could use a service like Mozilla products) - Allow the user to configure all Magnifier settings directly from NVDA. This means they do not have to learn two different assistive programs, and their preferences can be saved in the same configuration. - Learn from the innovative ideas in the free [Glassbrick](https://www.glassbrick.org/) magnifier, and ensure that NVDA can offer the same if not better interaction and configurability. - NVDA is the gateway through which blind Windows users perceive the Operating System and its applications. If there is any performance cost for thread switching between architectures, users will notice, as it will affect anything they do. - NVDA receives a great deal more events from the system than other standard applications. Perhaps there is a cost involved with constant thread context switching between architectures. - Synchronize the Magnifier with NVDA's focus / object navigation. I.e. if the user specifically navigates with NVDA, the Magnifier should follow along. - Unpack NVDA in the background, so updating only takes as long as renaming a folder and registering some shortcuts etc. Rather than the user having to wait for all files to be copied. Although NVDA runs on both x86 and x64 variants of Windows, and there is some x64 c++ code for NVDA that runs in-process,  the main NVDA application is only itself x86. Although all the work to run NVDA's in-process code in Excel already exists, we would need to still write the actual COM calls, plus come up with an appropriate serialized format in which to represent all the information for a given cell, for sending back to NVDA. As a part of the Google Summer of Code application process, NV Access is required to provide a project ideas list, which will help students as they plan and write their project proposals. As x64 processors can run x86 instructions natively, it is the current belief of NV Access that no major performance benefit would be seen by moving the NVDA application to x64. However, we are not 100% sure of this, and only doing it would answer the question once and for all. At very least this data could be stored locally with the ability for the user to send it to NV Access manually. At best, this data would be sent directly to NV Access servers automatically, assuming the user has allowed this. Collection and submission of performance data should be opt-in, and should not in itself cause negative impact on performance. Currently if there is an update available for NVDA, a dialog comes to the foreground notifying the user. this can interrupt the user and or the user may miss it or even accidentally activate it.  Currently we try to differentiate typed characters from other characters by their proximity to the caret. However, we should consider looking at newer APIs which may not have existed when writing the initial support. E.g. detecting them with `WM_CHAR` messages (available in Windows 7 and above), or from the key presses themselves in NVDA's `keyboardHandler` module (in Windows 10 Fall Creators Update and above). On Windows 10 October 2018 and above we could also consider switching to using `UI Automation` rather than using the console APIs at all. Due to the way NVDA must connect to consoles in order to access their content, if the console is closed with the mouse, it will always kill off the NVDA process as well. However, depending on the size of the document, the Elements list can take a long time to become fully populated with content. While this is happening, the user is blocked from doing anything else in NVDA. However, further work can be done to extend this to fetching of text formatting which is still slow. However, this support has the following problems which need to be addressed: If NVDA is configured to speak characters as they are typed, many times in consoles if new chunks of text are being written to the console, many of those characters are mistaken for typed characters. This means that NVDA ends up spelling out much of the content. If NVDA is flooded with events, this can cause major performance degradation. Improving the audio in NVDA will improve both stability and performance of NVDA. NVDA will be able to be used efficiently on a wider range of audio hardware, which means NVDA can be used in more situations and possibly on lower-end devices, ensuring NVDA is helping the greatest amount of blind and vision impaired people possible. Information such as how often the core is woken up, how long a core cycle takes on average, number of accessibility API events are received, how long navigating to the next or previous line in a document takes etc. Many blind and vision impaired people use Excel either in their education or employment. Speeding up support for Microsoft Excel will allow NVDA users to be much more efficient at their work. NVDA allows the user to read the content of Windows command consoles (cmd, Bash etc) with NVDA review cursor commands. It Also reports new text as it is written to the console. NVDA outputs audio (including sounds and speech from most speech synthesizers) via the [Windows  Multimedia](https://docs.microsoft.com/en-gb/windows/desktop/Multimedia/waveform-functions) (winMM) API. NVDA provides broad support for reading and interacting with spreadsheets in Microsoft Excel. This support is implemented by using [Excel's COM object model](https://docs.microsoft.com/en-us/office/vba/api/overview/excel/object-model) in a cross-process fashion. NVDA receives a great deal of events from various accessibility APIs such as [Microsoft Active Accessibility](https://docs.microsoft.com/en-us/windows/desktop/winauto/microsoft-active-accessibility) (MSAA), [Microsoft UI Automation](https://docs.microsoft.com/en-us/windows/desktop/winauto/entry-uiauto-win32), and [keyboard and mouse input hooks](https://docs.microsoft.com/en-us/windows/desktop/winmsg/hooks). Currently some of this code is run on a separate thread, but is still written in Python. Although we do a great deal of filtering before these events reach NVDA's main core thread, Python's global interpreter lock is held by these event handlers while they process / filter the raw events. Note that much of this idea has already been implemented in NVDA, see pr #9257. Partly due to the amount of information NVDA must fetch, and partly due to recent slowdowns in the object model itself, NVDA's access for Microsoft Excel is becoming slower, and in some cases  totally impractical. Although NV Access is working closely with the Excel team at Microsoft to rectify the recent slowdowns, and has in some cases improved performance in the last few months, we should definitely consider further actions we can take in NVDA to limit or batch object model calls in order to provide the best performance. Perhaps included in this work could be also improving the update process so that: Please direct any questions about these ideas to the NV Access GSOC mentors: Related issue: #7197 Related issue: [#7348](https://github.com/nvaccess/nvda/issues/7348) Related issues: [#2257](https://github.com/nvaccess/nvda/issues/2257), [#7451](https://github.com/nvaccess/nvda/issues/7451), [#9174](https://github.com/nvaccess/nvda/issues/9174)  See the [nvWave](https://github.com/nvaccess/nvda/blob/master/source/nvwave.py) module in the NVDA source code. Similar to reporting controls, NVDA reports many text formatting attributes. Again, currently the order of this information is hard-coded and is pretty much the same in both speech and braille. Example formatting attributes are font name, font size, attributes such as bold, italic and underline, font and background color, paragraph alignment and much more. Similarly to our [in-process support for Microsoft Word](https://github.com/nvaccess/nvda/blob/master/nvdaHelper/remote/winword.cpp), work has already begun to batch cross-process COM calls. we should consider fetching all possible information needed for a given cell in one call, via NVDA's in-process code in c++. While these calls are being made, we should also consider instructing Excel to pause [screen updating](https://docs.microsoft.com/en-us/office/vba/api/excel.application.screenupdating).  Some theoretical arguments to why going x64 may improve performance are: Some users (especially those using USB audio hardware) report a short chunk of audio being cut off either at the beginning or the end of speech. This may be caused by the fact that NVDA opens and closes the audio device for every speech utterance. It is possible that some audio drivers take slightly longer to open the device and drop some initial blocks. Similarly, when closing the device, some audio hardware may throw away the final blocks, rather than ensuring they have been played before closing.  The [NVDA project](https://github.com/nvaccess/nvda/) currently has more than 2000 [open issues](https://github.com/nvaccess/nvda/issues/) on Github and will consider project proposals on any of them assuming the size and complexity is suitable for GSOC. However, the following list are just some of the higher priority issues students may wish to consider. The majority of the work to make an x64 variant of NVDA is to change the build process to incorporate and use an x64 build of Python. However, there may be a lot of small assumptions in NVDA's code base about the architecture. Right now there are some specialized situations where NVDA must use specific 64 bit structures when using some Windows APIs to access 64 bit apps. This logic would need to be possibly reversed. The order in which NVDA reports these properties is hard-coded, and is roughly the same for both speech and braille. There are a number of NVDA users who use NVDA in conjunction with the [Magnifier built into Windows](https://support.microsoft.com/en-au/help/11542/windows-use-magnifier). We should consider a tighter integration between NVDA and the Windows Magnifier. Examples: There are several locks in place currently, but this should be reviewed. There is a possibility that several system crashes reported by users may be due to NVDA opening and closing the audio device too aggressively. Similarly, some users on low-end hardware report general lag and bad responsiveness. This may possibly be due to the  audio driver taking time to open the device for all speech utterances. There would however be one definite benefit to going x64, which is that it would resolve #7724 where NVDA cannot currently interact with 64 bit Java applications because there is no x86 Java Access Bridge client dll packaged with the x64 Java VM. This support is implemented using the [console APIs from kernel32](https://docs.microsoft.com/en-us/windows/console/console-functions). To aide in locating information in large documents, NVDA provides an Elements List (a treevew of available elements in the document) which can be filtered by type or name. For instance, on a web page, the Elements List can be used to quickly search through a list of links. We also may have multiple code paths opening, writing to and closing the audio device at the same time. E.g. the tones module for beeps, may hold the audio device open all the time. It may be an idea to somehow integrate all this so that audio only goes through one final code path that serializes access to the audio device. We could also consider looking at using newer audio APIs available in Windows 7 and above, as this is now the minimum Windows version required by NVDA. We could consider keeping the audio device open for several seconds after speech finishes so that all audio is played, and so that the audio device does not have to be opened again if more speech is coming soon. We could also add a few milliseconds of silence to the start of the audio when first opening the device, to ensure that the device is truly ready when NVDA starts to speak. We should consider allowing the user to customize the order in which this information is presented, and allow it to be configured separately for speech and braille. We should consider allowing the user to customize the order of this information, and allow them to configure it separately for both speech and braille. We should consider either moving all of our console API code into a separate process which would be safe to kill off, or consider moving to `UI Automation` on Windows 10 October 2018 and above. We should consider finding a faster diffing algorithm or perhaps writing one ourselves in c++. Also we should try to limit the amount of text sent to be spoken, so as to not flood the NVDA's core or the speech synthesizer.  We should consider moving these handlers into C++, ensuring that they are run on separate threads from NVDA's main core thread. Each handler should place its filtered data into a queue and wake up the core with some kind of low-level win32 event. The core can then take from the queue and process as it normally does. We should consider providing a UX for updates similar to other software, that makes use of modern notification APIs such as toasts and the Windows 10 notification API. We should consider rewriting the Elements List so that it only loads as many elements as actually fit in the treeview visibly on screen, and then either fetch more in the background or on demand when the user causes the treeview to scroll with the mouse or by moving past the first or last visible element. We would like to gather information about the performance of NVDA's various subsystems within day to day usage, so that we can better understand the performance issues that some people are reporting, especially those on low-end hardware. When NVDA reports a particular control in speech or braille, it includes information such as the control's name, role (button, checkbox, slider etc), states (checked, pressed, collapsed etc), its value if it has one (100% for example), description, keyboard shortcut, position in group, and several other possible properties.  When large amounts of new text is written to the console, NVDA can greatly decrease in performance or completely freeze, not only making it impossible to read further content in the console, but sometimes impossible to read anything else on the system unless the console is closed or NVDA is restarted.  [Related issues](https://github.com/nvaccess/nvda/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+label%3A%22Windows+Command+Console%22) [Related issues](https://github.com/nvaccess/nvda/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+label%3Aaudio) Project-Id-Version: 
POT-Creation-Date: 2019-03-26 13:55+Hora estándar romance
PO-Revision-Date: 2019-06-23 12:00+0200
Last-Translator: José Manuel Delicado <jmdaweb@hotmail.com>
Language-Team: 
Language: es
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Generated-By: pygettext.py 1.5
X-Generator: Poedit 2.2.3
Plural-Forms: nplurals=2; plural=(n != 1);
    Quizás se podría usar algún tipo de lenguaje de plantilla para representar este orden, junto con una interfaz de usuario adecuada que permita al usuario medio ser capaz de insertar, eliminar y reordenar propiedades.  Incidencias relacionadas: #7232  Esta interfaz debería separar las configuraciones de voz y braille, y puede llegar incluso a separar la configuración para el modo foco y el modo exploración (por ejemplo, anunciar controles incrustados en un documento tales como enlaces, en comparación con un control independiente en un diálogo). ## Ideas ## Introducción ### NVDA para 64 bits ### Personalizar el orden y la inclusión de la información de objetos y formato con voz y braille ### Mejorar el rendimiento de la navegación / edición en Microsoft Excel haciendo llamadas COM por lotes en el proceso ### Mejorar la estabilidad de la salida de audio en NVDA ### Mejorar la experiencia de usuario con el actualizador de NVDA ### Integrar NVDA con la lupa de Windows ### Carga perezosa de la lista de elementos ### Mover los manejadores de entrada / apis de accesibilidad a C++ ### Rendimiento y estabilidad en las consolas de comandos de Windows ### Sistema de medida de rendimiento para NVDA #### Precisión al verbalizar caracteres escritos en la consola #### ¡Al cerrar consolas con el ratón NVDA muere! #### Impacto #### Implementación #### Rendimiento #### El problema * Michael Curran <mick@nvaccess.org> (@michaeldcurran en Github) * Reef Turner <reef@nvaccess.org> (@feerrenrut en Github) - Que ya no haga falta acceso como administrador para actualizar NVDA (se podría usar un servicio como el que tienen los productos de Mozilla) - Permitir al usuario configurar todos los ajustes de la lupa desde NVDA. Esto significa que no tendrían que aprender a usar dos programas de asistencia, y sus preferencias podrían guardarse en la misma configuración. - Aprender de las ideas innovadoras del ampliador gratuito [Glassbrick](https://www.glassbrick.org/), y asegurarse de que NVDA puede ofrecer la misma o mejor interacción y configuración. - NVDA es la puerta mediante la que los usuarios ciegos de Windows perciben el sistema operativo y sus aplicaciones. Si hay cualquier coste de rendimiento derivado del cambio de hilos entre arquitecturas, los usuarios lo notarán, ya que afectará a cualquier cosa que hagan. - NVDA recibe una cantidad de eventos del sistema mucho mayor que cualquier aplicación estándar. Tal vez esto implica un coste al tener que cambiar constantemente el contexto de hilos entre arquitecturas. - Sincronizar la lupa con la navegación de NVDA por objetos o foco. Por ejemplo: si el usuario navega exclusivamente con NVDA, la lupa debería seguirlo. - Extraer NVDA en segundo plano, de tal forma que la actualización dure sólo lo que se tarda en renombrar una carpeta, registrar algunos accesos directos, etc. en vez de que el usuario tenga que esperar a que se copien todos los archivos. Aunque NVDA funciona en las variantes X86 y X64 de Windows y dispone de cierto código que se inyecta en los procesos X64, la aplicación principal de NVDA tan sólo es X86. Aunque ya existe todo el código necesario para ejecutar llamadas internas de proceso en el propio Excel desde NVDA, se deberían escribir las llamadas COM reales, así como definir un formato de serialización apropiado en el que representar toda la información de una celda dada para enviarla a NVDA. Como parte del proceso de solicitud del Google Summer of Code, NV Access está obligada a proporcionar una lista de ideas de proyecto, que ayudará a los estudiantes mientras planean y redactan sus propuestas de proyecto. Ya que los procesadores X64 pueden ejecutar instrucciones X86 de forma nativa, NV Access piensa que no habría mejoras de rendimiento importantes al portar NVDA a X64. Sin embargo, al no estar seguros al 100%, hacerlo sería la forma de zanjar esta cuestión de una vez por todas. Como mínimo se podrían almacenar estos datos de forma local y dar la capacidad al usuario de enviarlos a NV Access manualmente. Lo mejor sería que los datos se enviaran a los servidores de NV Access automáticamente, siempre que el usuario lo haya permitido. La recopilación y envío de los datos de rendimiento debe ser opcional, y en sí misma no debería causar un impacto negativo en el rendimiento. Actualmente, si hay una actualización disponible para NVDA, se muestra un diálogo en primer plano para notificar al usuario. Esto puede interrumpir al usuario, que además podría pulsar de forma accidental alguno de los botones.  Actualmente, NVDA intenta diferencia los caracteres escritos del resto por su proximidad al cursor. Sin embargo, habría que plantearse el uso de apis que no existían cuando se desarrolló el soporte inicial. Por ejemplo, detectarlos con mensajes "WM_CHAR" (disponibles en Windows 7 y posterior), o desde las propias pulsaciones de teclado con el módulo `keyboardHandler` de NVDA (en la actualización Windows 10 Fall Creators y posterior). En Windows 10 de octubre 2018 y posterior se podría usar `UI Automation` en vez de usar las apis de consola del todo. Debido a la forma que tiene NVDA de conectarse a las consolas para acceder a su contenido, si la consola se cierra con el ratón, el proceso de NVDA se cierra con ella. Sin embargo, dependiendo del tamaño del documento, la lista de elementos puede tardar mucho tiempo en llenarse completamente de contenido. Mientras eso ocurre, el usuario se queda bloqueado y no puede hacer nada más con NVDA. Sin embargo, se puede hacer trabajo adicional para extenderla y que recupere rápidamente el formato del texto, ya que actualmente esto sigue yendo despacio. Sin embargo, este soporte tiene problemas que hay que resolver: Si NVDA está configurado para verbalizar caracteres mientras se escriben, algunos fragmentos de texto se pueden confundir con caracteres escritos cuando llegan a la consola. Esto hace que NVDA acabe deletreando gran parte del contenido. Si NVDA se inunda con eventos, se puede causar un importante degradado en el rendimiento. Mejorar el audio en NVDA mejorará la estabilidad y el rendimiento del lector. NVDA podrá usarse de forma eficiente en un rango más amplio de dispositivos de audio, lo que significa que podrá utilizarse en más situaciones y posiblemente en dispositivos de gama más baja, ayudando así al mayor número de personas ciegas y deficientes visuales posible. Información sobre cada cuánto tiempo despierta el núcleo, cuánto lleva de media un ciclo del núcleo, cuántos eventos se reciben de las apis de accesibilidad, cuánto tiempo lleva navegar a la línea anterior o siguiente en un documento, etc. Muchas personas ciegas y con baja visión usan Excel en sus estudios o su trabajo. Acelerar el soporte para Microsoft Excel permitiría a los usuarios de NVDA ser mucho más eficientes en sus tareas. NVDA permite al usuario leer el contenido de las consolas de comandos de Windows (cmd, bash, etc) con las órdenes del cursor de revisión. También anuncia el texto tecleado mientras lo escribimos en la consola. NVDA emite audio (incluyendo sonidos y voz de la mayoría de sintetizadores) mediante la API [Windows  Multimedia](https://docs.microsoft.com/en-gb/windows/desktop/Multimedia/waveform-functions) (winMM). NVDA proporciona un amplio apoyo para la lectura y la interacción con hojas de cálculo en Microsoft Excel. Este soporte se implementa utilizando [el modelo de objetos COM de Excel](https://docs.microsoft.com/en-us/office/vba/api/overview/excel/object-model) utilizando un enfoque de proceso cruzado. NVDA recibe una gran cantidad de eventos de diversas apis de accesibilidad como [Microsoft Active Accessibility](https://docs.microsoft.com/en-us/windows/desktop/winauto/microsoft-active-accessibility) (MSAA), [Microsoft UI Automation](https://docs.microsoft.com/en-us/windows/desktop/winauto/entry-uiauto-win32), y los [interceptores de teclado y ratón](https://docs.microsoft.com/en-us/windows/desktop/winmsg/hooks). Actualmente parte de este código se ejecuta en un hilo separado, pero todavía está escrito en Python. Aunque se hace una gran operación de filtrado antes de que estos eventos alcancen el hilo principal del núcleo de NVDA, el cerrojo global del intérprete Python está en uso por estos manejadores de eventos mientras procesan y filtran estos eventos en bruto. Ten en cuenta que gran parte de esta idea ya se ha implementado en NVDA. Mira la solicitud de cambios #9257. El acceso de NVDA a Microsoft Excel se está volviendo más lento, y en ocasiones impracticable, en parte por la cantidad de información que NVDA debe recuperar y en parte por la ralentización del propio modelo. Aunque NV Access trabaja mano a mano con el equipo de Excel en Microsoft para rectificar las últimas relentizaciones, y en algunos casos ha mejorado el rendimiento en los últimos meses, deberíamos definitivamente plantear acciones que se puedan aplicar a NVDA para limitar o procesar por lotes las llamadas al modelo de objetos para proporcionar el mejor rendimiento. Quizás en este trabajo se podrían incluir mejoras en el proceso de actualización como las siguientes: Por favor, dirige cualquier pregunta sobre estas ideas a los mentores para GSOC de NV Access: Incidencia relacionada: #7197 Incidencia relacionada: [#7348](https://github.com/nvaccess/nvda/issues/7348) Incidencias relacionadas: [#2257](https://github.com/nvaccess/nvda/issues/2257), [#7451](https://github.com/nvaccess/nvda/issues/7451), [#9174](https://github.com/nvaccess/nvda/issues/9174)  Mira el módulo [nvWave](https://github.com/nvaccess/nvda/blob/master/source/nvwave.py) en el código fuente de NVDA. De manera similar a cómo se anuncian controles, NVDA informa sobre muchos atributos de texto. De nuevo, esta información vuelve a ser rígida y es casi la misma tanto en voz como en braille. Algunos atributos de formato de ejemplo son el nombre de la fuente, tamaño de fuente, atributos como negrita, cursiva o subrayado, color de fuente y fondo, alineación de párrafo y muchos más. De manera similar al [soporte en proceso para Microsoft Word](https://github.com/nvaccess/nvda/blob/master/nvdaHelper/remote/winword.cpp), se debería plantear la posibilidad de recuperar toda la información posible necesaria para una celda dada en una sola llamada mediante el código en proceso de NVDA escrito en C++. Mientras se hacen estas llamadas, se debería pensar en pedirle a Excel que pause el [refresco de pantalla](https://docs.microsoft.com/en-us/office/vba/api/excel.application.screenupdating).  Algunos argumentos teóricos por los que el rendimiento mejoraría al moverse a X64: Algunos usuarios (especialmente los que utilizan hardware de audio USB) informan sobre un pequeño corte en el audio al comienzo o al final de cada mensaje de voz. Esto podría deberse al hecho de que NVDA abre y cierra el dispositivo de audio en cada emisión de voz. Es posible que algunos controladores de audio tarden ligeramente más en abrir el dispositivo y se deshagan de algunos bloques iniciales. De forma similar, al cerrar el dispositivo, algún hardware de audio puede deshacerse de los bloques finales, en vez de asegurarse de que se reproducen antes de cerrar.  El [proyecto NVDA](https://github.com/nvaccess/nvda/) tiene actualmente más de 2000 [incidencias abiertas](https://github.com/nvaccess/nvda/issues/) en Github y plantearán propuestas de proyecto para todas ellas asumiendo que su tamaño y complejidad son adecuados para GSOC. Sin embargo, la siguiente lista contiene algunas de las incidencias más prioritarias que los estudiantes podrían plantearse resolver. La mayoría de trabajo que hay que realizar para crear una variante X64 de NVDA es cambiar el proceso de construcción para incorporar y usar una compilación X64 de Python. Sin embargo, puede haber un montón de pequeños supuestos en el código fuente de NVDA sobre la arquitectura. Ahora mismo existen ciertas situaciones especializadas en las que NVDA debe usar estructuras específicas de 64 bits al utilizar algunas apis de Windows para acceder a aplicaciones de 64 bits. Posiblemente sería necesario revertir esta lógica. El orden en que NVDA anuncia estas propiedades es rígido, y es casi el mismo para voz y braille. Hay un buen número de usuarios que utilizan NVDA junto con la [lupa incorporada en Windows](https://support.microsoft.com/en-au/help/11542/windows-use-magnifier). Debería plantearse la posibilidad de mejorar la inegración entre NVDA y la lupa de Windows. Ejemplos: Actualmente hay en juego varios cerrojos, pero habría que revisar esa parte. Hay una posibilidad de que se hayan producido varios fallos de sistema informados por algunos usuarios al abrir y cerrar el dispositivo de forma demasiado agresiva. De forma similar, algunos usuarios con hardware de gama baja informan de retrasos generales y malos tiempos de respuesta. Posiblemente, esto puede ser debido a que el controlador de audio se toma su tiempo para abrir el dispositivo cada vez que se emite voz. Habría, sin embargo, un beneficio definido al ir a X64, y es que se resolvería la incidencia #7724, en la que se expone que NVDA actualmente no puede interactuar con aplicaciones Java de 64 bits porque no hay empaquetada una DLL del cliente de Java Access Bridge para X86 en la máquina virtual de Java para X64. Este soporte se implementa usando las [apis de consola de kernel32](https://docs.microsoft.com/en-us/windows/console/console-functions). Para ayudar a ubicar información en documentos grandes, NVDA proporciona una lista de elementos (una vista en árbol de elementos disponibles en el documento) que puede filtrarse por tipo o nombre. Por ejemplo, en una página web, se puede usar la lista de elementos para buscar rápidamente en una lista de enlaces. También se pueden tener varias partes del código que abren, cierran y escriben en el dispositivo de audio al mismo tiempo. Por ejemplo, el módulo tones que emite pitidos puede mantener abierto el dispositivo de audio todo el tiempo. Puede ser una buena idea trabajar en un único fragmento de código que integre todo esto y serialice el acceso al dispositivo de audio. Se podría también plantear la posibilidad de usar apis nuevas incluidas en Windows 7 y versiones posteriores, ya que esta es la versión mínima de Windows en la que funciona NVDA. Se podría considerar la posibilidad de mantener el dispositivo abierto durante algunos segundos después de que la voz termine para que se reproduzca todo el audio, de tal forma que no haga falta abrir el dispositivo de nuevo si se va a emitir más voz. También se podrían añadir unos milisegundos de silencio al principio del audio cuando se abre el dispositivo por primera vez, para asegurarse de que el dispositivo está realmente listo antes de que NVDA empiece a hablar. Debería plantearse la posibilidad de permitir que el usuario personalice el orden en el que se presenta esta información, y que se configure de forma separada para voz y braille. Debería plantearse la idea de permitir que el usuario personalice el orden de esta información, y permitir que lo configuren por separado para voz y braille. Debería plantearse la idea de mover todo el código de consola a un proceso independiente que pueda matarse con seguridad, o bien recurrir a `UI Automation` en la actualización de octubre de 2018 de Windows 10 y posterior. Deberíamos plantearnos buscar un algoritmo más rápido de diferenciación o escribir uno propio en C++. Además se debería intentar limitar el texto que se va a verbalizar de tal forma que no inunde el núcleo de NVDA o el sintetizador de voz.  Se debería plantear la posibilidad de mover estos manejadores a C++, asegurándose de que se ejecuten en hilos distintos al del núcleo principal de NVDA. Cada manejador debería dejar sus datos filtrados en una cola y despertar al núcleo con algún tipo de evento Win32 a bajo nivel. El núcleo entonces puede recoger de la cola y procesar la información como lo haría normalmente. Debería plantearse la posibilidad de proporcionar una experiencia de usuario similar a la de otros programas, que haga uso de las apis modernas de notificación, como por ejemplo la API de notificación de Windows 10 o las notificaciones emergentes. Debería plantearse la posibilidad de reescribir la lista de elementos de tal forma que cargue sólo tantos elementos como quepan visualmente en pantalla en la vista en árbol, y después cargue más en segundo plano o bajo demanda cuando el usuario haga desplazarse la vista en árbol con el ratón o se mueva más allá del primer o último elemento visible. A NV Access le gustaría recopilar información sobre el rendimiento de los distintos subsistemas de NVDA al usarlos día a día, y de esa forma entender mejor los problemas de rendimiento de los que informan los usuarios, especialmente aquellos con hardware de gama baja. Cuando NVDA anuncia un control determinado mediante voz o braille, incluye información como su nombre, su rol (botón, casilla de verificación, deslizador, etc), estados (marcado, pulsado, contraído, etc), su valor si lo tiene (100% por ejemplo), descripción, atajo de teclado, posición en el grupo, y otras posibles propiedades varias.  Cuando se escriben enormes cantidades de texto en la consola, NVDA reduce considerablemente su rendimiento o se cuelga completamente, no sólo haciendo imposible la lectura de nuevo contenido en la consola, sino en todo el sistema. Esto sólo se arregla cerrando la ventana de la consola o reiniciando NVDA.  [Incidencias relacionadas](https://github.com/nvaccess/nvda/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+label%3A%22Windows+Command+Console%22) [Incidencias relacionadas](https://github.com/nvaccess/nvda/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+label%3Aaudio) 