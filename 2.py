# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 11:35:11 2019

@author: Masum
"""
import re 
s= "1996 was the year when I was born"
a=re.match(r"[a-zA-Z]+",s)
print(a)
b=re.search(r"[a-zA-Z]+",s)
print(b)
if re.match(r"^1996",s):
    print("match")
else:
    print("not match")
if re.search(r"born$",s):
    print("match")
else:
    print("not match")
