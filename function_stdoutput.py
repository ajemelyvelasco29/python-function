#!/usr/bin/env python
#Author: April Jemely Velasco
#Date: March 7, 2016
#Purpose: Python Script for displaying ouput in three ways

def MyFunc(name, age):
          print "Hi! My name is ", name + "and my age is", age
          print "Hi! My name is %s and my age is %d" %(name, age)
          print "Hi! My name is {} and my age is {}".format(name,age)

print MyFunc("April Jemely Velasco", 19)
