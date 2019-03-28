# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:15:38 2019

@author: JustinM
"""

# How fast can I do stock fizzbuzz? Let's find out!
# Written in 4:59.57

for x in range(1, 101):
    s_out = ""
    
    fizz = x % 3 == 0
    buzz = x % 5 == 0
    
    if (fizz or buzz):
        if (fizz):
            s_out += "Fizz"
        if (buzz):
            s_out += "Buzz"
    else:
        s_out = str(x)
    
    print (s_out)
