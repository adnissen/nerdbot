#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

progname = 'imagesearch'

def main(args):
	s = ""
	for arg in args:
		s+=arg + "_"
	if s[-1:] == "_":
		s = s[:-1]
	print "http://mebe.co/" + s + ".jpg"

if __name__ == '__main__':
    main(sys.argv[1:])