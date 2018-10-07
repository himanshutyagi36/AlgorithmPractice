#!/bin/python3
## https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem
from collections import defaultdict


import math
import os
import random
import re
import sys

# Complete the maxRegion function below.
def maxRegion(grid):
    max = 0
    r = len(grid)
    c = len(grid[0])
    max = 0
    for i in range(r):
        for j in range(c):
            count = countCells(grid, i, j)
            if count > max:
                max = count
    return max

def countCells(grid, i,j):
    if (i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0):
        return 0
    else:
        count = 1
        grid[i][j] = 0
        count += countCells(grid, i+1,j)
        count += countCells(grid, i-1,j)
        count += countCells(grid, i,j+1)
        count += countCells(grid, i,j-1)
        count += countCells(grid, i+1,j-1)
        count += countCells(grid, i-1,j-1)
        count += countCells(grid, i+1,j+1)
        count += countCells(grid, i-1,j+1)
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))
    
    
    res = maxRegion(grid)
    print(res)
    # fptr.write(str(res) + '\n')

    # fptr.close()

