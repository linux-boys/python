#!/usr/bin/env python 
#-*- coding: utf-8 -*-

import os 
Dir = ["/opt/a","/opt/n"]
for i in Dir:
	if not os.path.exists(i):
		print "a"
	else:
		print "b"
