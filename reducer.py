#!/usr/bin/env python3
import sys 
import json

dic={}
new={}
old_key="testetsttesttesttest"
for line in sys.stdin:
    key, value= line.split(",")
    key=key.strip("\n")
    value=value.strip("\n")
    key=key.strip(" ")
    value=float(value)
    #print("tester",key,old_key,"aaa")
    if(key!=old_key):

        if(old_key!="testetsttesttesttest"):
            #print(old_key,round((dic[old_key]/count),3))
            new["name"]=old_key
            new["strike_rate"]=round((dic[old_key]/count),3)
            print(json.dumps(new))
            dic.clear()


        count=1
        old_key=key
        dic[key]=value
    else:
        count=count+1
        dic[key]=dic[key]+value
#print(old_key,round((dic[old_key]/count),3))
new["name"]=old_key
new["strike_rate"]=round((dic[old_key]/count),3)
print(json.dumps(new))
dic.clear()
    

