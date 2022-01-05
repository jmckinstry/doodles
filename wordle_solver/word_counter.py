#!/usr/bin/python3

# This script counts the letters in a given file and, if they are alphabetical/numerical, writes out their count
import sys
from collections import Counter

all_letters = "abcdefghijklmnopqrstuvwxyz"

arg1 = sys.argv[1] if len(sys.argv) > 1 else "dictionary_top_5000"
f = open(arg1)
c = Counter("")
for l in f:
	c += Counter(l)
f.close()

for c1 in c.keys():
	if all_letters.find(c1) >= 0:
		print(c1 + " " + str(c[c1]))