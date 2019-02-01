# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 10:37:12 2019

@author: Masum
"""
import re
s="I was born in the year 1995"
s="abbb"
a=re.sub(r"\d","",s)
print(a)
b=re.match(r".*",s)
print(b)
c=re.match(r".+",s)
print(c)
d=re.match(r"[a-zA-Z]+",s)
print(d)
e=re.match(r"ab?",s)
print(e)