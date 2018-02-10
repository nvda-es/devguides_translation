# Repositorio de traducción de documentación para desarrolladores de NVDA

Note: this readme file is in spanish. If you don't know our language, consider using a translation tool or learning it. It's one of the most spoken languages in the world, apart from English.

## Introducción

El objetivo de este repositorio es alojar y mantener la traducción al español de la documentación de desarrollo de NVDA. En el momento de la creación de este repositorio ya se han traducido casi completamente dos wikis de NVAccess y se han alojado como páginas en nuestra web oficial, pero existe un grupo de documentos que cambian a un ritmo más elevado que los demás. Estos son:

* La guía para desarrolladores de NVDA
* La wiki de desarrollo de complementos
* El archivo léame del repositorio de código fuente.

Hay que monitorizar los cambios en estos documentos de una manera sencilla, y traducirlos rápidamente para garantizar su disponibilidad.

## Funcionamiento y estructura del repositorio

Nuestro objetivo es que los traductores conozcan en todo momento su progreso y cometan el mínimo número de errores posible. Para ello, no hay mejor forma de trabajo que con el programa Poedit, incluso para la documentación. Se ha partido del método que usa Manuel Cortez en TWBlue para traducir documentos, y se ha extendido para soportar casi cualquier archivo. El repositorio consta de las siguientes carpetas:

* original_docs: aquí se descargarán documentos en inglés periódicamente, preferiblemente en formato markdown.
* python_docs: esta carpeta contiene los documentos anteriores, convertidos a scripts Python.
* potfiles: en esta carpeta hay plantillas de traducción, una por cada documento.
* translations: en esta carpeta se encuentran los archivos que deben abrir los traductores con Poedit.
* translations/xx/LC_MESSAGES: xx, en este caso, es un código de idioma, de momento es.
* translated_docs: esta carpeta contiene el resultado final de las traducciones en html.
* scripts: pequeños programas encargados de convertir ficheros.

Nota: si alguna de estas carpetas no existe, créala antes de empezar.

## Para comenzar

Si eres traductor, únicamente necesitas Poedit. Puedes descargarlo desde http://poedit.net
Si quieres participar en el proceso de conversión de documentos, necesitas lo siguiente:

* Python, versión 2.7.14 o posterior para Windows. Se pueden usar las versiones de 32 o 64 bits.
* Los paquetes markdown y html2markdown, que puedes instalar desde pip
* Agrega la ruta a tu carpeta de instalación de Python modificando la variable path en las variables de entorno de tu sistema. El instalador lo hará por ti si marcas la opción correspondiente.

## Conversión de ejemplo

Vamos a convertir el documento home.md, que corresponde a una sencilla página de bienvenida con una sola línea. Para ello hay que abrir un símbolo del sistema y navegar a la carpeta scripts dentro del repositorio. Es muy importante permanecer en esta carpeta mientras se ejecutan comandos. Allí hacemos lo siguiente:

1. Ejecuta el siguiente comando: python documentation_importer.py ../original_docs/home.md
2. Verás un archivo llamado home.py en python_docs
3. Ejecuta el siguiente comando: genpot
4. En potfiles verás una plantilla de traducción.
5. Abre poedit. Crea un nuevo catálogo a partir de esta plantilla, e indica que está en español.
6. Traduce el documento.
7. Guarda el resultado en translations/es/LC_MESSAGES/home.po, y asegúrate de que el archivo .mo se compila al guardar.
8. Desde la consola, ejecuta: python generator.py ../python_docs/home.py
9. El documento aparecerá en translated_docs/xx, donde xx es el código de idioma.

## Conversión de html a markdown

En ocasiones hay documentos que están en formato t2t. Este formato no es ideal para trabajar. Afortunadamente estos documentos se convierten a html, como la guía del desarrollador. Para convertirlos a markdown y procesarlos como en el apartado anterior, necesitamos un programa como pandoc. Se puede descargar de http://pandoc.org. Una vez instalado, hacemos lo siguiente:

1. Descargamos el documento a nuestro disco duro usando la opción guardar como del navegador. Por ejemplo vamos a guardar este en la carpeta raíz del repositorio, con el nombre devguide.html: https://www.nvaccess.org/files/nvda/documentation/developerGuide.html
2. Ejecutamos el siguiente comando desde la raíz del repositorio: pandoc devguide.html -f html -t markdown -s -o original_docs/devguide.md
3. El documento convertido aparecerá en original_docs. Borra el html de origen, no sirve para nada y ocupará un preciado espacio en el repositorio si no lo haces.
