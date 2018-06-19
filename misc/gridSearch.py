## https://www.hackerrank.com/challenges/the-grid-search/problem
#!/bin/python3

import math
import os
import random
import re
import sys

def gridSearchUtil(G,P,rStart,cStart):
    for x in range(len(P)):
        for y in range(len(P[0])):
            if G[x+rStart][y+cStart] == P[x][y]:
                continue
            else: return False
    return True
# Complete the gridSearch function below.
def gridSearch(G, P):
    rg = len(G)
    cg = len(G[0])
    rp = len(P)
    cp = len(P[0])
    rDiff = rg-rp
    cDiff = cg-cp
    flag = False
    for i in range(rDiff+1):
        for j in range(cDiff+1):
            if G[i][j] == P[0][0]:
                flag = gridSearchUtil(G,P,i,j)
                if flag:
                    return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
