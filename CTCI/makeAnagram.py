#!/bin/python

import math
import os
import random
import re
import sys

def isAnagram(a,b):
    counter = [0]*26
    offset = ord('a')
    delCounter = 0
    for i in a:
        counter[ord(i) - offset]+=1
    for j in b:
        counter[ord(j) - offset]-=1
    for i in counter:
        delCounter += abs(i)
    print (delCounter)

if __name__ == '__main__':
    a = raw_input()

    b = raw_input()
    isAnagram(a,b)


