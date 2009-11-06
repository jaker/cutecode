#!/bin/python

#
# Script to add language brushes from http://alexgorbatchev.com/wiki/SyntaxHighlighter:Brushes
# Initially written by Jeff Dlouhy
#

import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'cutesite.settings'
sys.path.append('..')

from cutesite.apps.poster.models import Language

BRUSHES = [{ "name" : "ActionScript3",
  "highlightname" : "as3",
  "highlightscript": "shBrushAS3.js"},
{ "name" : "Bash/shell",
  "highlightname" : "bash",
  "highlightscript" : "shBrushBash.js"},
{ "name" : "C#",
  "highlightname" : "csharp",
  "highlightscript" : "shBrushCSharp.js"},
{ "name" : "C++",
  "highlightname" : "cpp",
  "highlightscript" : "shBrushCpp.js"},
{ "name" : "CSS",
  "highlightname" : "css",
  "highlightscript" : "shBrushCss.js"},
{ "name" : "Delphi",
  "highlightname" : "pascal"
  , "highlightscript" : "shBrushDelphi.js"},
{ "name" : "Diff",
  "highlightname" : "diff",
  "highlightscript" : "shBrushDiff.js"},
{ "name" : "Groovy",
  "highlightname" : "groovy"
  , "highlightscript" : "shBrushGroovy.js"},
{ "name" : "JavaScript",
  "highlightname" : "jscript",
  "highlightscript" : "shBrushJScript.js"},
{ "name" : "Java",
  "highlightname" : "java",
  "highlightscript" : "shBrushJava.js"},
{ "name" : "JavaFX",
  "highlightname" : "javafx"
  , "highlightscript" : "shBrushJavaFX.js"},
{ "name" : "Perl",
  "highlightname" : "perl",
  "highlightscript" : "shBrushPerl.js"},
{ "name" : "PHP",
  "highlightname" : "php",
  "highlightscript" : "shBrushPhp.js"},
{ "name" : "Plain Text",
  "highlightname" : "plain",
  "highlightscript" : "shBrushPlain.js"},
{ "name" : "PowerShell",
  "highlightname" : "powershell",
  "highlightscript" : "shBrushPowerShell.js"},
{ "name" : "Python",
  "highlightname" : "python",
  "highlightscript" : "shBrushPython.js"},
{ "name" : "Ruby",
  "highlightname" : "ruby",
  "highlightscript" : "shBrushRuby.js"},
{ "name" : "Scala",
  "highlightname" : "scala",
  "highlightscript" : "shBrushScala.js"},
{ "name" : "SQL",
  "highlightname" : "sql",
  "highlightscript" : "shBrushSql.js"},
{ "name" : "Visual Basic",
  "highlightname" : "vbnet"
  , "highlightscript" : "shBrushVb.js"},
{ "name" : "XML",
  "highlightname" : "xml",
  "highlightscript" : "shBrushXml.js"}]


# TODO: Fix it to update the language if it already exists
def addLanguge(langDict):
    newLang = Language(name = langDict["name"],
                       highlight_name = langDict["highlightname"],
                       highlight_script = langDict["highlightscript"],
                       mime_type = "text/plain")
    newLang.save()


def createBrushes():
    for brush in BRUSHES:
        print "Importing " + brush["name"]
        addLanguge(brush)
    print "Done!\n"

if __name__ == '__main__':
    createBrushes()
