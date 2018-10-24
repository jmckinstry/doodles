An implementation for the following request:
Given an integer n and an array of numbers k, return the nth smallest number in k.

This can apparently be done in O(2k), which boggles my mind enough that I made a _testing version just to see it in action.

First implementation attempt was to keep an array of size n and just discard things too big for it, but that wasn't working out. A bit of advice ("No need to sort") put me on divide and conquer.

It's O(2k) because we initially scan the full list to sort it, then discard on average half of the array to do it again.
n + n/2 + n/4 + n/8 + n/16... = 2n
