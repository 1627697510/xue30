#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
try:
    fh = open("D:/testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print "Error: 没有找到文件或读取文件失败"
else:
    print "内容写入文件成功"
    fh.close()

try:
    fh = open("D:/testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
finally:
    print "Error: 没有找到文件或读取文件失败"
try:
    fh = open("D:/testfile", "w")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print "close this file"
        fh.close()
except IOError:
    print "Error: 没有找到文件或读取文件失败"
'''
def functionName( level ):
    if level < 1:
        raise Exception("Invalid level!", level)
    print "OK"
try:
    functionName(0)
except "Invalid level!":
    print "user defined exception"
else:
    print "else......"
finally:
    print "finally always run....."
