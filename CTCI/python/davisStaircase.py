#!/bin/python3


import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def stepPerms(n):
    ## explanation here: https://math.stackexchange.com/questions/2376182/recursion-davis-staircase
    # if n <0:
    #     return 0
    # if n==1 or n==0:
    #     return 1
    # return stepPerms(n-1)+stepPerms(n-2)+stepPerms(n-3)
    
    ## following taken from discussions
    arr = [1,2,4]
    if n < 4: return arr[n - 1];
    m=n+1
    for i in range(5,m):
        arr[(i + 1) % 3] = arr[0] + arr[1] + arr[2];
    return arr[0] + arr[1] + arr[2];
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
