#!/usr/bin/env python3
# -*- coding: utf-8 -*

import urllib
#python3 urllib2 merged with urllib
from bs4 import BeautifulSoup
import re
import subprocess
import os
import sys
from collections import namedtuple

## FILES ##
definitions = os.path.abspath("Documents/Terminal/wordOfTerminal/definitions.txt")
dictFile = os.path.abspath("Documents/Terminal/wordOfTerminal/dicts.txt")
## FILES  ##


## Resource EP determined from language abvreviation (langAbrv) in Bash input ##
class getLanguage:

	def __init__(self, lang, langAbrev, defTrans):
		self.lang = lang
		self.langAbrev = langAbrev
		self.defTrans = defTrans

	def __repr__(self):
		return repr((self.lang, self.langAbrev, self.defTrans))

def loadLanguages():
	languages = []
	with open(dictFile) as df:
		for line in df:
			lang, langAbrev, defTrans = line.split()	
			languages.append(getLanguage(lang, langAbrev, defTrans))
	return languages

def matchLanguage(languages):
	for language in languages:
		if language.langAbrev == sys.argv[1]:
			return language

languages = loadLanguages()
language = matchLanguage(languages)

## Resource EP and language for prompt (language.defTrans & Language.Lang) ##		
### Retrive searchterm from translate command if present 
### User input - no searchterm present give prompt >> continue to give prompt
try:
	searchTermBash =  sys.argv[2]
except IndexError:
	searchTermBash = ""
	pass
searchFinished = False
searchTerm = ""

while not (searchFinished):

	if ((searchTermBash == "" and searchTerm == "") or searchTerm != "" ):
		searchTerm = input("word in " + language.lang + ":")
	else:
		searchTerm = searchTermBash
## User input ##
	
## Retrieve Definition
	resourceEP = "https://www.wordreference.com/" + language.defTrans + "/%s" % searchTerm
	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
	headers ={'User-Agent':user_agent,}
	request = urllib.request.Request(resourceEP,None,headers)
	response = urllib.request.urlopen(request)
	soup = BeautifulSoup(response, 'html.parser')

## Printound to definitions log and to terminal ##
	try:
		result = soup.ol.get_text()
	
	except:
		result = "no translation found"
		pass
	
	print(result)
		
	if(result != "no translation found"):
		with open(definitions, "a") as wordLog:
	       		definition = ' '.join(result.split())
	       		wordLog.write((u'{} {}: {}'.format(language.lang, searchTerm, definition)))
	       		wordLog.write("\n")
## While loop continues	
			
		
		

	


