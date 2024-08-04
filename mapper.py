#!/usr/bin/env python3
import sys
import json
for line in sys.stdin: 
	line=line.strip("[")
	line=line.strip("]")
	line=line.strip("\n")
	line=line.strip("\t")
	line=line.strip(",")
	rate=0
	if(len(line)!=0):
		line=json.loads(line)
		#print(line["name"])
		name=line["name"]
		if(line["balls"]==0):
			rate=0
		else:
			rate=round((line["runs"]/line["balls"]*100),3)
		print(line["name"],",",rate)
    
    
#    for word in words:
####        print(word.lower()+"\t1")
