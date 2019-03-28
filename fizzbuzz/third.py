# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:55:14 2019

@author: Asier
"""

# Third pass: Fastest execution, smallest memory footprint

# Finished in 23:33.71

s_fastest_precomputed_string = """1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz"""

def fizzbuzz_fastest():
    """
    First thing I look for is if precomputation is acceptable.
    The space of this problem is surprisingly small (A max of sum_of_word_lengths * output_line_count),
    which seems to be a good candidate for precomputation.
    I'll use a module-specific top-level variable to keep python from evaluating the string each time (I'm actually not certain it will, and I'd do more research in the normal programming day)
    """
    
    print (s_fastest_precomputed_string)

def fizzbuzz_smallest():
    """
    Since we're counting, we MUST have a counter
    Since we MUST have the strings, we'll pre-allocate those (otherwise they're sitting in program memory instead of execution memory and we're copying them anyways)
    -    (as an aside, I realize that 'fizz' and 'buzz' have common suffixes and could be reduced together using 'fi', 'bu', and 'zz' to save two bytes, but I think
    -    the code to stitch the words back together will take more than two bytes of execution space so it's not worth it in this case)
    Since we MUST have the divisors, we'll store those via program execution space
    
    FizzBuzz is better than brain-dead because of the possiblity of multiple divisors applying to the counter, so do I use a single test for *any* divisors and then branch,
    or do I use multiple bools (ie: C-style masking) so I don't duplicate work?
    Research says: Python doesn't have masks, and single bools are likely to be smaller than any comparison check, so I'll do tests for all divisors and then act accordingly.
    Each test takes a bool to process, but it tosses it away afterwards, so checks should be smallest
    """
    x = 1
    
    while x <= 100:
        #switch(x): # Python doesn't have switch, research says to use a dictionary for single values, we're multiple values here, do it by hand
        if x % 3 and x % 5:
            print (x)
        elif (x % 3 == 0) and (x % 5 == 0):
            print ("FizzBuzz")
        elif x % 3 == 0:
            print ("Fizz")
        else:
            print ("Buzz")
            
        x += 1

print ("fizzbuzz_fastest(): ")
fizzbuzz_fastest()

print ("")

print ("fizzbuzz_smallest(): ")
fizzbuzz_smallest()