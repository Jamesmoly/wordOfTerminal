#!/usr/bin/env python3
# -*- coding: utf-8 -*

import urllib
#python3 urllib2 merged with urllib
from bs4 import BeautifulSoup
import re
import subprocess
import os
import sys

try:
	searchTermBash =  sys.argv[1]
except IndexError:
	searchTermBash = ""
	pass
searchFinished = False
searchTerm = ""

while not (searchFinished):
	if ((searchTermBash == "" and searchTerm == "") or searchTerm != "" ):
		searchTerm = input("paraula catala: ")
	else:
		searchTerm = searchTermBash
	resourceEP = "http://www.wordreference.com/definicio/%s" % searchTerm
	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
	headers ={'User-Agent':user_agent,}
	request = urllib.request.Request(resourceEP,None,headers)
	response = urllib.request.urlopen(request)
	soup = BeautifulSoup(response, 'html.parser')

	try:
		result = soup.ol.get_text()
		paraulasCatala = os.path.abspath("Documents/Terminal/wordOfTerminal/paraulasCatala.txt")
				
		with open(paraulasCatala, "a") as wordLog:
			
			definition = result.split(':')[0].split()
	
			if (len(definition)>15):
				definition = ' '.join(result.split()[:15])
			else:
				definition = ' '.join(result.split(':')[0].split())

			wordLog.write((u'{}: {}'.format(searchTerm,definition)))
			wordLog.write("\n")	
	except:
		result = "no translation found"
		pass
	print(result)
	
			
		
		

	


