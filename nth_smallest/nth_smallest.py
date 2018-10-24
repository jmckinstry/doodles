# Setup
import sys
import random

ary_input = sys.argv
program_name = ary_input.pop(0)

if len(ary_input) < 1:
        print("Usage: " + program_name + " <nth_smallest_number> [list of integers ...]")
        sys.exit(-1)

nth_smallest = int(ary_input.pop(0))
list_input = ary_input # neat

if nth_smallest <= 0:
        print("Nth smallest number must be a positive integer")
        sys.exit(-1)

if len(list_input) == 0:
        for x in range(1000000):
                list_input.append(random.randint(1, 100000000))

if len(list_input) < nth_smallest:
        print("Error: List too small to find value " + str(nth_smallest) + " (list only has " + str(len(list_input)) + " elements).")
        sys.exit(-2)


for x in range(len(list_input)):
        list_input[x] = int(list_input[x])

#print("Input:\t\tSize " + str(len(list_input)) + ", seeking smallest(" + str(nth_smallest) + ")")

# Solution 1

# This solution was scrapped: best case was too rare and worst case was essentially O(n^2) which is horrible
"""
list_smallest = []
size_smallest = 0
highest_in_smallest = sys.maxint

for x in range(len(list_input)):
        if list_input[x] > highest_in_smallest:
                list_input.pop(x)
                x -= 1
                continue

        if list_input[x] < highest_in_smallest:
                size_smallest += 1
"""

# Solution 2
# The start of this solution comes from an advisor's gentle nudging by insisting that sorting was too much work, but we can use what we've already touched anyways

def f_nth_smallest(a, n, pivot = -1):
        global cost

        list_left = []
        list_right = []

        # Check recursion "win" condition
        if len(a) == 1 and n == 1:
                return a[0]

        # No end yet, sort into left and right, then recurse
        pivot = a.pop(0)

        for x in range(len(a)):
                if a[x] < pivot:
                        list_left.append(a[x])
                else:
                        list_right.append(a[x])

        if len(list_left) == (n - 1): # Pivot won
                return pivot
        elif len(list_left) >= n: # winner is in left
                return f_nth_smallest(list_left, n)
        else: # Winner is in right
                return f_nth_smallest(list_right, n - (len(list_left) + 1)) # We reduce by 1 more because of the pivot

val = f_nth_smallest(list_input, nth_smallest)
print(str(val))
