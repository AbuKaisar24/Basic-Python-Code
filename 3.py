# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 11:51:05 2019

@author: Masum
"""
import re
s="I love Avengers"
print(re.sub(r"Avengers","Justic League",s))
print(re.sub(r"[a-z]","0",s))
print(re.sub(r"[A-Z]","0",s))

