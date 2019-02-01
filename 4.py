# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 12:30:03 2019

@author: Masum
"""
import re
s1="welcome home this is 2019"
s2="Just ~% +++----arrived at @dhaka.#fun$$$boys"
s3="i      love      my country"
m1=re.sub(r"\d","",s1)
print(m1)
m2=re.sub(r"[@$#%~+-\.\']"," ",s2)
print(m2)
m3=re.sub(r"\W"," ",s2)
print(m3)
m4=re.sub(r"\s+"," ",m3)
print(m4)
m5=re.sub(r"\s+"," ",s3)
print(m5)
m6=re.sub(r"\s[a-zA-Z]\s+"," ",m4)
print(m4)