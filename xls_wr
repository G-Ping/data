#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlwt;
import xlrd;
import xlutils;
from xlutils.copy import copy;

def write(row,col,value,file):
    oldWb = xlrd.open_workbook(file)
    newWb = copy(oldWb)
    newWs = newWb.get_sheet(0)
    newWs.write(row,col,value)
    newWb.save(file)

def read(row,col,file):
    data = xlrd.open_workbook(file)
    table = data.sheets()[0]
    return table.row_values(row)[col]
    
if __name__ ==  '__main__':
    write(0,0,11,'1.xls')
    write(0,1,12,'1.xls')
    write(0,2,13,'1.xls')
    write(1,0,21,'1.xls')
    write(1,1,22,'1.xls')
    write(1,2,23,'1.xls')

    data = xlrd.open_workbook('1.xls')
    table = data.sheets()[0]
    for i in range(table.nrows):
        for j in range(len(table.row_values(i))):
            print table.row_values(i)[j]

    for i in range(table.ncols):
        for j in range(len(table.col_values(i))):
            print table.col_values(i)[j]
            
    print read(0,0,'1.xls')
