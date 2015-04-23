#!/usr/bin/env python 
#-*- coding: utf-8 -*-
l1 = ['b','c','d','b','c','a','a']  
l2 = []  
[l2.append(i) for i in l1 if not i in l2] 
print l2

count = 0
l1=["123","afa","asf"]

while count < len(l1):
	print l1[count]
	count += 1
while l1:
	print l1[0]
	l1.pop(0)
