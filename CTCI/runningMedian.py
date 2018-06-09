#!/bin/python3

import math
import os
import random
import re
import sys

from heapq import heappush, heappop, heapify, _siftdown_max, _heappop_max

def _heappush_max(heap, item):
    heap.append(item)
    _siftdown_max(heap, 0, len(heap)-1)
    
def addItem(num, lowerHalf, higherHalf):
    if(len(lowerHalf) == 0 or num < lowerHalf[0]):
         _heappush_max(lowerHalf, num)
    else:
        heappush(higherHalf, num)
        
def rebalance(lowerHalf, higherHalf):
    if(abs(len(lowerHalf) - len(higherHalf)) >= 2):
        if(len(lowerHalf) < len(higherHalf)):
            _heappush_max(lowerHalf, heappop(higherHalf))
        else:
            heappush(higherHalf, _heappop_max(lowerHalf))
            
def getMedian(lowerHalf, higherHalf):
    if len(lowerHalf) == len(higherHalf):
        return (lowerHalf[0] + higherHalf[0]) / 2
    elif len(lowerHalf) > len(higherHalf):
        return lowerHalf[0]
    else:
        return higherHalf[0]

def findMedian(items):
    lowerHalf = []
    higherHalf = []
    medians = []
    for num in items:
        addItem(num, lowerHalf, higherHalf)
        rebalance(lowerHalf, higherHalf)
        medians.append(getMedian(lowerHalf, higherHalf))
    return medians

if __name__ == '__main__':
    n = int(input())

    a = []

    for _ in range(n):
        a_item = int(input())
        a.append(a_item)
        
    for each in findMedian(a):
        print('{0:.1f}'.format(each))

