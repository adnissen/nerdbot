#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from flask import Markup
import re
import urllib2
import sys

progname = 'ts'

def main(args):
	if len(args) == 0:
		print "You need to enter a search term."
		return
	s = ""
	for arg in args:
		s+=arg
	s = s.replace(" ", "+")
	s = s.replace("'", r"")
	response = urllib2.urlopen("https://twitter.com/search?q=" + s + "&src=typd")
	page_source = response.read()
	soup = BeautifulSoup(page_source)
	links = soup.find_all("a", "details with-icn js-details")
	username = soup.find_all("span", "username js-action-profile-name")
	tweets = soup.find_all("p", "js-tweet-text")
	if len(tweets) == 0:
		print "No results."
		return
	tweet = Markup(tweets[0]).striptags()
	username = Markup(username[0]).striptags()
	link = links[0].get('href')
	link = "https://twitter.com" + link
	print username.encode("ascii", "ignore") + ": " + tweet.encode("ascii", "ignore") + " (" + link.encode("ascii", "ignore") + ")";

if __name__ == '__main__':
	main(sys.argv[1:])