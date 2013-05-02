#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import sys

progname = 'youtube'

def main(args):
    s = ""
    for arg in args:
        s+=arg
    s = s.replace(" ", "+")
    s = s.replace("'", r"")
    r = requests.get('https://gdata.youtube.com/feeds/api/videos?q=' + s + '&alt=json')
    ret = json.loads(r.text)
    if 'entry' in ret['feed']:
        print ret['feed']['entry'][0]['title']['$t']
        print ret['feed']['entry'][0]['link'][0]['href']
    else:
        print "No results found!"

if __name__ == '__main__':
    main(sys.argv[1:])