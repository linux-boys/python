#!/usr/bin/env python 
#-*- coding: utf-8 -*-


# list comprehension
l1 = ['b','c','d','b','c','a','a']  
l2 = []  
[l2.append(i) for i in l1 if not i in l2] 
print l2


# list all item
count = 0
l1=["123","afa","asf"]

while count < len(l1):
	print l1[count]
	count += 1
while l1:
	print l1[0]
	l1.pop(0)


# about class of list method
l3 = ["a","c",2,3,5,6,7]
l4 = [12,34,56]
l3.append(2)
print l3
del l3[0]
print l3
l3.sort()
print l3
l3.reverse()
print l3
l3.extend(l4) #<=> l3 = l3 + l4
print l3,l4
print len(l3)


# section 
print l3[1:]
print l3[1:-1]
