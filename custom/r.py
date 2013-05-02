#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import sys

progname = "remember"

def main(args):
    appId = ''
    apiKey = ''
    args[0] = args[0].lower()
    if args[0] == "help":
        print "Usage: \n.r term \n .r term string \n .r del term \"thing to delete\" "
        return
    if len(args) == 1:
        headers = {'X-Parse-Application-Id': appId, 'X-Parse-REST-API-Key' : apiKey}
        r = requests.get('https://api.parse.com/1/classes/rObjs', headers = headers)
        results = json.loads(r.text)
        found = "false"
        for result in results['results']:
            if result['objWord'] == args[0]:
                found = "true"
                print result['objContent']
        if found == "false":
            print "I don't know anything about " + args[0]
    elif args[0] == "del":
        headers = {'X-Parse-Application-Id': appId, 'X-Parse-REST-API-Key' : apiKey}
        r = requests.get('https://api.parse.com/1/classes/rObjs', headers = headers)
        results = json.loads(r.text)
        for result in results['results']:
            if result['objWord'] == args[1] and result['objContent'] == args[2]:
                found = "true"
                delobj = result['objectId']
        if found == "true":
            requests.delete('https://api.parse.com/1/classes/rObjs/' + delobj, headers = headers)
            print "Forgotten"
        else:
            print "Not found"
    elif len(args) > 1:
        s = ""
        for arg in args[1:]:
            s+=arg + " "
        headers = {'X-Parse-Application-Id': appId, 'X-Parse-REST-API-Key' : apiKey}
        payload = {'objWord' : args[0], 'objContent' : s}
        r = requests.post('https://api.parse.com/1/classes/rObjs', data=json.dumps(payload), headers = headers)
        print "I\'ll remember that for " + args[0]



if __name__ == '__main__':
    main(sys.argv[1:])