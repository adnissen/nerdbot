#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import sys
from flask import Markup
from bs4 import BeautifulSoup


def main(args):
	response = urllib2.urlopen("http://adnissen.com/insults/")
	page_source = response.read()
	soup = BeautifulSoup(page_source)
	insult = soup.find("center")
	insult = Markup(insult).striptags()
	print insult

if __name__ == '__main__':
    main(sys.argv[1:])