#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import yaml

def write(data,file1):
    f=open(file1,'w')
    yaml.dump(data,f)
    f.close()    

def write_one(key,value,file1):
    s = read(file1)
    f = open( file1, 'w' )
    s[key]=value
    yaml.dump( s, f )
    f.close( )

def read(file1):
    f = open(file1, 'r')
    return yaml.load(f)
    f.close()

def read_one(key,file):
    f = open(file, 'r')
    return yaml.load(f)[key]
    f.close()

def delete(key,file):
    s = read(file)
    f = open( file, 'w' )
    del s[key]
    yaml.dump( s, f )
    f.close( )

def new_yamlfile(dir1=''):
    timestamp = time.strftime( '%Y%m%d-%H%M%S' )
    file1 = dir1+timestamp + '.yaml'
    f = open( file1, 'w' )
    data = {}
    yaml.dump( data, f )
    f.close()
    return file1


if __name__ == "__main__":
    file1 = new_yamlfile()
    data={'host': {'ip00': '192.168.1.1', 'one': '192.168.1.2'}, 'soft': {'apache': 2.2, 'mysql': 5.2}} 
    write(data,file1)
    write_one('yd',2,file1)
    print read(file1)
    print read_one('yd',file1)
    delete('yd',file1)
    print read(file1)
