# Setup
import sys

ary_input = sys.argv
ary_input.pop(0)
list_input = list(' '.join(ary_input))

print("Input:\t\t" + str(''.join(list_input)))

# Solution
length = len(list_input)

def reverse_elements(a, first=0, last=-1):
        if last < 0:
                last = len(a) - 1

        if first >= last \
                or first < 0:
                return

        for x in range((last - first + 1) / 2): # Add 1 to include the last char
                holder = a[first + x]
                a[first + x] = a[last - x]
                a[last - x] = holder


val = list_input
index = 0
reverse_elements(val)
for x in range(len(val)):
        if val[x] == ' ':
                reverse_elements(val, index, x - 1)
                index = x + 1
reverse_elements(val, index)

print("Solution 1:\t" + str(''.join(val)))
