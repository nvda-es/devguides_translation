# -*- coding: utf-8 -*-
""" This script converts the hold documentation (saved in markdown files) in a python file with a list of strings to translate it using gettext."""
import sys
import os
def prepare_documentation_in_file(fileSource, fileDest):
	""" This takes documentation written in a markdown file and put all the contents in a python file, to create a translatable  documentation.
	 @fileSource str: A markdown(.md) file.
	 @fileDest str: A file where this will put the new strings"""

	f1 = open(fileSource, "r")
	f2 = open(fileDest.replace(" ", "_"), "w")
	lns = f1.readlines()
	f2.write("# -*- coding: utf-8 -*-\n")
	f2.write("documentation = [\n")
	for i in lns:
		if "\n" == i:
			newvar = "\"\","
		elif "\n" == i[-1]:
			newvar = "_(u\"\"\"%s\"\"\"),\n" % (i[:-1])
		else:
			newvar = "_(u\"\"\"%s\"\"\"),\n" % (i)
		newvar=newvar.replace("|\"\"\"", "| \"\"\"").replace("\"\"\"\"", "\" \"\"\"").replace("u\" \"\"\"", "u\"\"\" \"").replace("u\"\"\"|", "u\"\"\" |")
		f2.write(newvar)
	f1.close()
	f2.write("]")
	f2.close()

if len(sys.argv)<2:
	print ("You must specify at least a source markdown file")
elif len(sys.argv)==2:
	prepare_documentation_in_file(sys.argv[1], os.path.join("..", "python_docs", os.path.splitext(os.path.basename(sys.argv[1]))[0]+".py"))
else:
	prepare_documentation_in_file(sys.argv[1], sys.argv[2])