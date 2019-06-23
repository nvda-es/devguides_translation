��    G      T  a   �             >     �   R  �  �  ~   �  .  8	     g
  "   y
     �
     �
     �
     �
     �
     �
          &     <     T     l     �     �     �  �   �  9  �  U   �  H   !  a   j  K   �  C     �   \  5   �  D   %  Z   j  ,  �  �   �  �   �     f  �   g    $  �   7  �   �  �   \  �   �  u   �  3   e  V   �  
  �  �   �  �   �  g   o  w   �  +  O  �   {  0   ;  x   l  N   �  �   4   �  �   �  "  �   $  �  �$  N   �&  e  �&  1   J(  (   |(  �   �(  {   ;)  �   �)  c  g*  n   �+  �  :,     �-  T   �-  �   ".  �   �.  �   Z/  q  �/  (   l1     �1     �1     �1     �1      �1     2      '2     H2     e2     |2     �2  /   �2     �2  !   3  '   #3  �   K3  �  24  k   �5  t   26  n   �6  e   7  J   |7  �   �7  7   �8  W   �8  �   9  _  �9  �    ;  1  �;    =  �   #>  '  �>  �   @  �   �@  �   IA  2  �A  �   0C  ;   �C  i   D  =  pD  �   �E    tF  f   �G  �   �G  U  rH  �   �I  .   �J  w   �J  M   cK  �   �K  �  kL  �  $N  #  �O  
  Q  f   "S  }  �S  e   U  T   mU  �   �U  �   pV  �   W  �  �W  �   wY     3   )   B   F   %         &   ?       D   A       6   /   .   5      C                             !       (   8                 '         ,   +                          G   $   *   
   -   2                 #       9          E   4       @          >      "                                ;   7       :   	       1   0   <         =                              * The bug is trivial enough to be fixed by a collaborator.     * The pull request was submitted by an active collaborator and it is inevitable that they will follow through with a suitable pull request to address the issues.  * Anyone currently on master snapshots will be upgraded to the first available tagged beta for the current release. Beta builds, as the name implies, are beta quality and have had some testing by users. Note that as new betas are made available you will keep automatically upgrading, and then also upgrade to the final stable release. To get back to beta testing for the next release you will need to manually download a new beta for that release.  * The snapshots page at https://www.nvaccess.org/files/nvda/snapshots/ now lists both alpha snapshots and all beta releases.   * Up until recently incubation was the only way we could guarantee some kind of code quality. Now we have a growing number of unit tests, system testing is well under way, and Github's management of pull requests (including mandatory code reviews) ensure a minimum code quality we did not have before. # Release Process ## Changes to the existing process ## For Developers ## For Testers ## For Translators ## Release Workflow ### Beta phase ### Changes for developers ### Changes for testers ### Development Phase ### Goals and reasoning ### Maintenance Release ### Release Candidate ### Representation on GitHub ### Scheduled Releases ### Translatable String Freeze *  Builds of  master (known as alpha snapshots) will be made available to the public for very early testing. This is bleeding-edge code and should never be run in production environments. * 3 weeks before the release is due, the beta branch will enter a translatable string freeze for 2 weeks. That is, no changes to text strings that affect translations are allowed. Minor spelling or grammatical fixes may be made to documentation files, but gettext strings in the code should not be changed at all. * A maintenance release may only include fixes for crashes and major security issues. * A topic branch should be submitted for inclusion using a pull request. * After the translatable string freeze, the "rc" branch will be created based on the beta branch. * After this, only critical bug fixes should be committed to the rc branch. * All Pull requests must follow the Pull Request template provided. * All pull requests submitted must have their "Allow edits from maintainers" checkbox ticked. This is usually the case for all new pull requests.  * All translation should be based on the beta branch. * Any relevant documentation should be included in the topic branch. * For most items, an issue will be filed and discussed before a pull request is submitted. * From 7 weeks before the release, merges from master to beta will no longer occur. New pull requests may be now considered for squash merging straight to beta, if and only if they are addressing a bug introduced in the current release cycle or a critical Operating System change out of our control.  * Generally, final releases will be due around 22 February, 22 May, 22 August and 22 November. The exact date for each release will be determined by the lead developers. * GitHub issues should be created for most issues and discussed first before submitting a pull request. However, some trivial changes might not require an issue first. See [[Contributing]] for details. * If a merged pull request has been identified as causing a regression, new bug, or does not work as originally reported, the pull request may be reverted at the discretion of the lead developers. Reasons in favor of not reverting the pull request may be:  * If a merged pull request results in a regression, new bug or does not work as advertised, the lead developers will be a little more strict on reverting the pull request than in the past. * If a merged pull request that reached beta has been identified as causing a regression, new bug, or does not work as originally reported, the pull request may be reverted at the discretion of the lead developers. Reasons in favor of not reverting the pull request may be:  * If a pull request is reverted from beta, it is more than likely any new pull request replacing it will not get into the current release. * If any changes are made to beta, such as the merging of critical pull requests or translation merges, beta will be periodically merged back to master.  * If priority should be given to an issue for inclusion in a specific release, its milestone should be set to the appropriate release milestone (e.g. 2014.4). * If the merging of a pull request to master causes any build checks on master to fail, the pull request is reverted without question. This is however unlikely to be an issue as build checks on the pull request itself must have already passed. * Issues/pull requests for bug fixes for an rc should have their milestone set to the relevant release (e.g. 2013.2). * Maintenance releases are made from the rc branch. * New commands, drivers, settings, dialogs, etc. must be documented in the User Guide. * Once a pull request has been reviewed and approved by at least one NVDA Collaborator and all build checks have passed, a lead developer will make a final commit to the pull request which updates changes.t2t, and then will squash merge the pull request into master. * Once a pull request is approved by reviewers and all build checks pass, the pull request will be merged straight to master. There is no longer incubation on next. * Once a pull request is squash merged to the master branch, the milestone for the issue (if any) and pull request should be set to the next release milestone (e.g. 2013.2) and it should be closed as fixed. * Only critical bug fixes and translation updates should be committed to the beta branch at this stage. * Pull requests must be based on NVDA's master branch unless explicitly instructed to do otherwise by a lead developer. * Starting from 5 weeks before final release, tagged beta releases will be published periodically, allowing the wider community to try out the betas. At this stage code originally introduced through master will have been tested for at least 2 weeks, thus the beta builds can be seen as beta quality. * Submitted pull requests should not contain edits to changes.t2t. Instead, change log entries should be placed in the pull request description, under the appropriate section in the template. * Subsequent release candidates may be released. * The final release can only be made if there have been no commits and at least 1 week since the last release candidate. * The first release candidate will immediately be released from the rc branch. * The master branch is bleeding edge. It includes code that is being tested for possible inclusion in upcoming releases, but it may not yet be tested much (if at all) and there may be major bugs. * The next branch and next snapshots will no longer exist. Anyone currently on a next snapshot will be automatically updated to new "alpha" snapshots. Alpha snapshots are created directly from Master each time it changes (I.e. when a pull request is merged).  As the name suggests, these snapshots are alpha quality. And although automated tests pass, these builds have had no user testing. * The next branch required manual merging of pull requests. This did not fit in well with Github's infrastructure in that these incubation merges were not tracked very well, reverts were messy and sometimes required next to be totally re-created, pull requests on next would frequently become conflicted with other pull requests, which meant manually fixing conflicts in both next and master. * Topic branches should be submitted as pull requests against master, unless a lead developer has specifically requested  the pull request be made against beta or rc in the case of addressing bugs introduced in the current release cycle.  * Translators should ensure their translation is up to date a day before the translatable string freeze ends in order for it to be included in the upcoming final release. The lead developers will announce the deadline when the freeze begins, but it will generally be close to UTC 00:00 on 14 February, 14 May, 14 August and 14 November. Work submitted after this time will not be included in the upcoming release. * Under rare circumstances, a maintenance release (e.g. 2013.1.1) may be made. * Up until 7 weeks before a release, a last known good commit of master (I.e. one that passes build checks) will be periodically merged into a "beta" branch, making that code available for early translation. The beta branch at this stage should still be considered bleeding-edge, and is not recommended for people than other to check early translation work. * Work should be done in a separate topic branch. * Work should be done in topic branches. * beta releases are beta quality. They include code that will be in the next release and has been tested without reported issues for at least a week. The main goal of these changes is to remove the need for a "next" branch and pull request incubation. Reasons for this are: The process outlined later in this document has only been implemented very recently. Therefore this first section talks specifically about the changes from the older process.  This document provides rough guidelines for the process of developing NVDA releases. All current and potential developers and translators should read and follow this document. These guidelines may be broken under special circumstances. Any concerns should be discussed with the lead developers: Mick Curran (@michaelDCurran) and Reef Turner (@feerrenrut). This is the general release workflow. Information for specific community groups is provided in later sections. Project-Id-Version: 
POT-Creation-Date: 2018-08-28 22:09+Hora de verano romance
PO-Revision-Date: 2019-06-23 12:01+0200
Last-Translator: José Manuel Delicado <jmdaweb@hotmail.com>
Language-Team: 
Language: es
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Generated-By: pygettext.py 1.5
X-Generator: Poedit 2.2.3
Plural-Forms: nplurals=2; plural=(n != 1);
       * El fallo es suficientemente trivial como para que un colaborador lo solucione.     * La solicitud de cambios fue enviada por un colaborador activo y se sabe con certeza que volverá con otra solicitud de cambios para solucionar los problemas.  * Se actualizará a cualquiera que utilice versiones master a la primera versión beta etiquetada para la liberación actual que esté disponible.  * La página de versiones de desarrollo en https://www.nvaccess.org/files/nvda/snapshots/ ahora lista tanto todas las versiones alfa como las versiones beta.   * Hasta hace poco, la incubación era la única forma de garantizar algún tipo de calidad en el código. Ahora hay un número creciente de pruebas unitarias, las pruebas del sistema van por buen camino, y la gestión de solicitudes de cambio de Github (incluidas las revisiones obligatorias del código) aseguran una calidad mínima del código que antes no existía. # El proceso de liberación de versiones ## Cambios al proceso existente ## Para desarrolladores ## Para evaluadores ## Para traductores ## Flujo de trabajo de versiones ### La fase beta ### Cambios para desarrolladores ### Cambios para evaluadores ### Fase de desarrollo ### Objetivos y razones ### Versiones de mantenimiento ### Candidata a liberación (release candidate) ### Representación en GitHub ### Programación de liberaciones ### Congelación de cadenas traducibles * Versiones de desarrollo compiladas de master (conocidas como instantáneas alfa)  quedarán a disposición del público para pruebas tempranas. Su código es muy inestable y nunca deberían utilizarse en entornos de producción. * Tres semanas antes de que se libere la versión definitiva, la rama beta entrará en modo congelación de cadenas traducibles durante dos semanas. Esto significa que no se permitirán los cambios que afecten al texto de las traducciones. Los errores de ortografía y gramática que estén en la documentación pueden arreglarse, pero no hay que cambiar las cadenas traducibles con Gettext del código. * Una versión de mantenimiento sólo puede incluir solución a fallos muy graves o problemas de seguridad. * Una rama de un tema concreto debería ser enviada para incluirla mediante una solicitud de cambios (pull request). * Después de la congelación de cadenas traducibles, se actualizará la rama "rc" basándose en la rama beta. * Después de esto, sólo se pueden enviar commits a la rama rc para solucionar problemas muy graves. * Todas las solicitudes de cambio deben seguir la plantilla proporcionada. * Todas las solicitudes de cambio enviadas deben tener la casilla de verificación "Allow edits from maintainers" marcada. Generalmente, este es el caso para todas las nuevas solicitudes de cambio.  * Todas las traducciones deben basarse en la rama beta. * Se debe incluir cualquier documentación relevante en la rama temática en cuestión. * Para la mayoría de elementos, se abrirá una incidencia y se discutirán los cambios antes de enviar una solicitud de cambios. * Siete semanas antes de la liberación, dejarán de hacerse mezclas de master a beta. Se deberían plantear las nuevas solicitudes de cambios para mezclarse directamente en beta, sy y sólo si solucionan un fallo introducido en el ciclo actual de liberación o hay un cambio crítico en el sistema operativo fuera del control de los desarrolladores.  * Generalmente, las versiones finales saldrán alrededor del 22 de febrero, 22 de mayo, 22 de agosto y 22 de noviembre. La fecha exacta para cada versión será determinada por los desarrolladores principales. * En la mayoría de los casos, se debe crear una incidencia en GitHub para cada problema existente y discutirla antes de enviar una solicitud de cambios. Sin embargo, aquellos cambios que sean triviales no necesitan una incidencia. Mira el artículo sobre cómo contribuir con NVDA para más información. * Si una solicitud de cambios mezclada se ha identificado como causante de un fallo nuevo, una regresión, o no funciona como se informó originalmente, los desarrolladores principales pueden revertir la solicitud. Las razones a favor de no revertir la solicitud de cambios pueden ser:  * Si una solicitud de cambios mezclada incluye una regresión, un fallo nuevo o no funciona como se indica, los desarrolladores principales serán un poco más estrictos que antes al revertirla. * Si una solicitud de cambios que llega a beta se identifica como causante de una regresión, un nuevo fallo o no funciona como se había indicado originalmente, los desarrolladores principales pueden revertir la solicitud. Las razones a favor de no revertir la solicitud de cambios pueden ser:  * Si se revierte una solicitud de cambios en beta, es más que probable que las solicitudes de cambio que la sustituyan no entren en la versión actual. * Si se realiza algún cambio a beta, como la fusión de pull requests o la integración de traducciones, se fusionará beta de vuelta a master periódicamente.  * Si se debería dar prioridad a una incidencia para que se incluya en una versión específica, su hito (milestone) debe establecerse a la versión deseada (por ejemplo, 2014.4). * Si la mezcla de una solicitud de cambios en master causa que falle cualquier comprobación de compilación en master, la solicitud se revierte sin preguntar. Sin embargo, esto probablemente no será un problema, ya que las comprobaciones de compilación en la solicitud en sí deberían haberse superado. * Las incidencias y solicitudes de cambio para arreglar fallos en una versión candidata deberían tener el hito de dicha versión (por ejemplo, 2013.2). * Las versiones de mantenimiento se crean desde la rama rc. * Las nuevas órdenes, controladores, ajustes, diálogos, etc. deben documentarse en la guía de usuario. * Una vez que una solicitud de cambio ha sido revisada y aprobada por al menos un colaborador de NVDA y todas las comprobaciones de compilación se han superado, un desarrollador principal hará un commit final a la solicitud de cambio que actualice changes.t2t, y después mezclará la solicitud de cambio en master. * Una vez que los revisores aprueben una solicitud de cambios y se superen todas las comprobaciones de compilación, la solicitud se mezclará directamente en master. Ya no hay incubación en next. * Una vez se mezcle una solicitud de cambios en la rama master, el hito para la incidencia (si lo hay) y el de la solicitud de cambios deberían establecerse en el hito de la siguiente versión (por ejemplo, 2013.2) y el problema debería cerrarse y marcarse como resuelto. * Sólo se deben enviar a la rama beta actualizaciones de traducciones y solucionar pequeños errores. * Las solicitudes de cambio deben basarse en la rama master de NVDA a menos que un desarrollador principal especifique lo contrario. * Empezando cinco semanas antes de la liberación final, se publicarán periódicamente versiones etiquetadas como beta, permitiendo que la mayor parte de la comunidad las pruebe. En este punto, el código introducido mediante master habrá sido probado durante al menos dos semanas, por lo que las compilaciones beta tienen calidad de beta. * Las solicitudes de cambios enviadas no deberían contener cambios en changes.t2t. En su lugar, las entradas del registro de cambios deberían situarse en la descripción de la solicitud de cambios, bajo la sección apropiada de la plantilla. * Pueden publicarse más versiones candidatas. * La versión final sólo puede crearse si no ha habido commits durante una semana desde la última versión candidata. * Se liberará la primera versión candidata inmediatamente desde la rama rc. * La rama master tiene código que se está probando para ver si se incluye en próximas versiones. Este código podría no haberse probado mucho, y podría contener fallos importantes. * La rama next y las versiones instantáneas de desarrollo next dejarán de existir. Se actualizarán automáticamente a las nuevas versiones "alfa" todas las next. Las versiones alfa se crean a partir de master cada vez que ésta cambia (p.ej. cuando se mezcla una solicitud de cambio). Como su nombre sugiere, estas versiones son de calidad alfa. Y aunque pasen las pruebas automáticas, estas versiones no han tenido evaluadores humanos. * En la rama next era necesario mezclar manualmente las solicitudes de cambio. Esto no encajaba bien en la infraestructura de Github, y por tanto las mezclas incubadas no se rastreaban muy bien, las reversiones estaban desordenadas y en ocasiones era necesario recrear la rama next, las solicitudes de cambios generalmente hacían conflictos en next con otras solicitudes, lo que significaba que había que solucionar los conflictos tanto en next como en master. * Las ramas temáticas deberían enviarse como solicitudes de cambio hacia master, a menos que un desarrollador principal haya solicitado específicamente que la solicitud de cambios se haga hacia beta o rc en caso de que se solucionen fallos introducidos en el ciclo de la versión actual.  * Los traductores deben asegurarse de que su traducción esté lista un día antes de que finalice la congelación de cadenas de traducción para que sus cambios sean incluidos en la versión final. Los desarrolladores principales anunciarán la fecha límite cuando la congelación comience, pero generalmente estará cerca de las 00:00 UTC el 14 de febrero, 14 de mayo, 14 de agosto y 14 de noviembre. Cualquier trabajo que se envíe tras estas fechas no se incluirá en la próxima versión, quedará para la siguiente. * Bajo extrañas circunstancias, se puede crear una versión de mantenimiento (por ejemplo, 2013.1.1). * Hasta siete semanas antes de una liberación, se mezclará en una rama "beta" un commit reciente que se sepa que funciona bien de master (es decir, que supera las pruebas de compilación), dejando el código disponible para su traducción. La rama beta en ese momento debería seguir considerándose inestable, y no se recomienda para gente que no vaya a probar las traducciones. * El trabajo debería hacerse en una rama separada y relacionada con el tema sobre el que se trabaja. * El trabajo debería hacerse en ramas independientes según el tema del que traten. * Las liberaciones beta están en estado beta. Incluyen código que irá en la próxima versión, y que se ha evaluado sin informar de problemas durante al menos una semana. El objetivo principal de estos cambios es suprimir la necesidad de una rama "next" e incubación de solicitudes de cambio. Las principales razones son: El proceso descrito más adelante en este documento ha sido implementado hace muy poco. Por lo tanto, esta primera sección habla de los cambios específicos del proceso antiguo.  Este documento ofrece pautas generales para el desarrollo de versiones de NVDA. Todos los desarrolladores y traductores, tanto actuales como aquellos que potencialmente puedan serlo, deberían leer y seguir este documento. Estas pautas pueden romperse en circunstancias especiales. Cualquier detalle relacionado con este documento debe discutirse con los desarrolladores principales: Mick Curran (@MichaelDCurran) y Reef Turner (@feerrenrut). Este es el flujo de trabajo general de publicación de versiones. En las siguientes secciones se ofrece información para grupos específicos de la comunidad. 