import html2markdown
import sys
import os
if len(sys.argv)<2:
 print ("Please, provide the path to the html file.")
else:
 f1=open(sys.argv[1], "r")
 content=f1.read()
 f1.close()
 f2=open(os.path.join("..", "original_docs", os.path.basename(os.path.splitext(sys.argv[1])[0]+".md")), "w")
 f2.write(html2markdown.convert(content))
 f2.close()
