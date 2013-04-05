#!/usr/bin/env python
# matt@nycresistor.com - guesses gender count on openstack contributors

import gender
import json

from pprint import pprint

json_data=open('grizzly.json')
devs = json.load(json_data)
json_data.close()

malecount = 0
femalecount = 0
unknowncount = 0

for developers in devs['developers'] :
    #pprint(developers)
    fname = devs['developers'][developers][0]
    for key, value in fname.iteritems():
        checkname = value.encode('ascii','ignore')
        checkname = checkname.upper()
        # print "checking %s : " % ( checkname )
        try:
            # print gender.gender[checkname]
            gendev = gender.gender[checkname]
            if gendev == 'male' :
                malecount += 1
            else :
                femalecount += 1 
        except:
            unknowncount += 1

print "females : %s" % femalecount
print "males : %s" % malecount
print "unknowncount : %s" %unknowncount 

