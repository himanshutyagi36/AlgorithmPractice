## https://www.hackerrank.com/challenges/equal/problem

# Using this fact, we can calculate in O(1) time how many 
# operations it takes to remove n chocolates - see numOps()

# The optimal solution is usually to reduce everyone's # of chocolates
# down to the minimum # in the group, however it may also be the case that
# {min-1, min-2, min-3, min-4} are more optimal since we have the option of
# taking away up to 5 chocolates at a time.

# Using all this information, we can use a greedy approach where
# we iterate over every co-worker and reduce their chocolates down
# to the minimum.

import math
import os
import random
import re
import sys

 
def numOps(n):
    result = 0
    result += int(n/5)
    n %= 5
    result += int(n/2)
    n %= 2
    result += n
    return result

# Complete the equal function below.
def equal(arr):
    # Iterate over the list and try reducing everyone's candies
    # down to {min, min-1, min-2, min-3, min-4}. Take the minimum 
	# answer.
    answer = sys.maxsize
    for i in range(4):
        tempAnswer = 0
        for j in range(len(arr)):
            # minOps = sys.maxsize
            tempAnswer += numOps(arr[j] - smallestNum+i)
            print("tempAnser: "+str(tempAnswer))
        if tempAnswer < answer:
            answer = tempAnswer
    return answer

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))
        smallestNum = min(arr)
        
        result = equal(arr)
        print(result)
        
        # fptr.write(str(result) + '\n')

    # fptr.close()
