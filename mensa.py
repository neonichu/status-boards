#!/usr/bin/env python

##
## Extracts the table for meals in Mensa 1 of the TU Braunschweig.
##

from BeautifulSoup import BeautifulSoup as soup

import urllib2

BASE_URL = 'http://www.stw-on.de/braunschweig/essen/menus/mensa-1#heute'

if __name__ == '__main__':
	page = soup(urllib2.urlopen(BASE_URL))
	for anchor in page('a', {'name': 'heute'}):
		p = anchor.parent.nextSibling.nextSibling
		for table in p('table'):
			print table
