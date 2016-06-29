#!/usr/bin/python
# -*- coding: gb2312 -*-
import json

def json_str(dict1):
    return json.dumps(dict1, ensure_ascii = False,encoding = 'gb2312',sort_keys=True,indent=4,skipkeys=True)


def json_w(dict1,outputJsonFile):
    fout = open(outputJsonFile, 'w')
    outStr = json.dumps(dict1, ensure_ascii = False)  
    fout.write(outStr.strip() + '\n')                                                    
    fout.close() 

if __name__ == '__main__':
    
    data = {
    '手动' : '手动',
    'shares' : 100,
    'price' : {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
    }
    }

    json_w(data,'2.json')
    
    fin = open('2.json', 'r')
    for eachLine in fin:
        line = eachLine.strip().decode('gb2312')
        line = line.strip(',')
        print json_str(json.loads(line))
