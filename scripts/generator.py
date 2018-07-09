# -*- coding: utf-8 -*-
import markdown
import os
from codecs import open as _open
import languageHandler
languageHandler.setLanguage("en")
import sys
import imp

# supported languages
languages = ["es"]

def generate_document(language, sourceModule):
 #import the source module, we will call it strings
 moduleName=os.path.splitext(os.path.basename(sourceModule))[0]
 searchpath=[os.path.dirname(os.path.abspath(sourceModule))]
 translation_file = moduleName
 reload(languageHandler)
 languageHandler.setLanguage(language, translation_file)
 f, p, d=imp.find_module(moduleName, searchpath)
 strings=imp.load_module(moduleName, f, p, d)
 f.close()
 markdown_file = markdown.markdown("\n".join(strings.documentation[1:]), extensions=["markdown.extensions.toc", "markdown.extensions.wikilinks", "markdown.extensions.tables", "markdown.extensions.fenced_code"])
 title = strings.documentation[0]
 filename = moduleName+".html"
 first_html_block = """<!doctype html>
 <html lang="%s">
 <head>
  <title>%s</title>
  <meta charset="utf-8">
  </head>
  <body>
  <header><h1>%s</h1></header>
  """ %  (language, title, title)
 first_html_block = first_html_block+ markdown_file
 first_html_block = first_html_block + "\n</body>\n</html>"
 if not os.path.exists(os.path.join("..", "translated_docs", language)):
  os.mkdir(os.path.join("..", "translated_docs", language))
 mdfile = _open("%s/%s" % ("../translated_docs/"+language, filename), "w", encoding="utf-8")
 mdfile.write(first_html_block)
 mdfile.close()

def create_documentation(sourceModule):
 print("Creating documentation in the supported languages...\n")
 for i in languages:
  print("Creating documentation for: %s" % (i,))
  generate_document(i, sourceModule)
 print("Done")

if len(sys.argv)<2:
	print ("Please, provide the Python filename which contains translatable strings")
else:
	create_documentation(sys.argv[1])