# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:42:25 2019

@author: Asier
"""

# Pass 2: Extended FizzBuzz. Start and stop with specified ints, allows for modifiable divisors and output words
# Finished in 9:07.92
def fizzbuzz(
        start = 1, 
        stop = 100, 
        words = [(3, 'Fizz'), (5, 'Buzz')]
        ):
    assert(start < stop)
    assert(len(words) > 0)
    
    x = start
    while (x <= stop):
        s_out = ""
        
        for div, word in words:
            if x % div == 0:
                s_out += word
        
        if len(s_out) > 0:
            print(s_out)
        else:
            print(str(x))
        
        x += 1

fizzbuzz(1, 16)

fizzbuzz(1, 10, [(2, 'Even'), (10, 'Tens')])