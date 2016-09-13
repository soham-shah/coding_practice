#!/bin/python

import sys


S = raw_input().strip()
test = zip(S, 'SOS'*100)
fails = 0
for x,y in test:
    if (x!=y):
        fails += 1
print(fails)