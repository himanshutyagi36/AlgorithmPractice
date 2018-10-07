#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    if len(note) > len(magazine):
        print("No")
        return
    
    counts = dict()
    flag = True
    for word in magazine:
        counts[word] = counts.get(word,0) + 1
        
    for word in note:  
        if word in counts:
            # checkCaseEquality(word, counts[word])
            counts[word] = counts.get(word) - 1
            if counts[word] < 0:
                print("No")
                return
        else:
            flag = False
            break
    if (flag):
        print("Yes")
    return
                
        

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
