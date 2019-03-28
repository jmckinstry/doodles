# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 12:25:51 2019

@author: Asier
"""

# Fourth: Production-style FizzBuzz. The horror.
# While I won't be adding __init__.py to this doodles folder, pretend it's there so this would be importable

# Finished in 30:24.49

"""
fizzbuzz takes a starting and stopping integer and optional list of divisors and words.
It can return a string, write to a callback, or print to console.

For each integer between start and end inclusive, if that integer is evenly divisible by a divisor,
write that word. If multiple divisors apply, write out every word that would apply in the order supplied to the words list.
If no divisor applies, write out the counter instead.

If print_output is True, write the output to the console instead of returning a value.

If callback is specified, callback is called for each counter value instead of returning a value.
This is especially useful if you're calling fizzbuzz with a very large counter range.
"""

def fizzbuzz(        
        start = 1,
        stop  = 100,
        words = [               # A list of 2-value tuples in the form (<divisor>, <word_to_print>)
                    (3, 'Fizz'),
                    (5, 'Buzz')
                ],
        print_output = True,
        callback = None
        ):
    
    store_output = (print_output is False and callback is None)
    output = "" # This will hold the entire string to return if print_output is false and no callback is specified
    
    x = start
    
    while x <= stop:
        s_out = _check(x, words)
        
        if print_output:
            print (s_out)
        if callback:
            callback(s_out)
            
        if store_output:
            output += s_out + "\n"
        
        x += 1
    
    if store_output:
        return output

"""
_check is an internal function that figures out which words or values to output for fizzbuzz to use. It is supplied with the
current value and the words to check against.

Always returns a string.

JM: Splitting up like this also makes the output generation easier to test
"""
def _check(counter, words):
    s_out = ""
    
    for (div, word) in words:
        if counter % div == 0:
            s_out += word
    
    if len(s_out):
        return s_out
    else:
        return str(counter)


"""
Normally this section would be calling / testing code, but it's here for convenience
"""
fizzbuzz(1, 16)

out_len = len(fizzbuzz(1, 20, print_output = False))
print ("Output length of fizzbuzz(1, 20, False) is: ", str(out_len))

fizzbuzz(1, 30, print_output = False, callback = lambda val: print ("Lambda call: " + val))

fizzbuzz(-30, -10)

# Globals are gross, but I'll need to research lambda functions in python to do better quickly (and would do so in the normal day-to-day)
fizz_count = 0
def g_fcount(val): 
    global fizz_count
    if val.find('Fizz') is not -1:
        fizz_count += 1
        
fizzbuzz(1, 100, print_output = False, callback = g_fcount)
print ("Fizz count for 1-100 is: " + str(fizz_count))