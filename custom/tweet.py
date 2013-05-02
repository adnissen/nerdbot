#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import sys
from flask import Markup
from bs4 import BeautifulSoup


def main(args):
	response = urllib2.urlopen("http://adnissen.com/tweets/")
	page_source = response.read()
	soup = BeautifulSoup(page_source)
	tweet = soup.find("center")
	tweet = Markup(tweet).striptags()
	print tweet

if __name__ == '__main__':
    main(sys.argv[1:])