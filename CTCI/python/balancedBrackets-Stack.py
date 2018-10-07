#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        expression = input()
        stack = []
        for c in expression:
            # print(c)
            if (c == '(' or c == '{' or c == '['):
                stack.append(c)
            else:
                if(len(stack) > 0):
                    if c == ')' and stack[len(stack)-1] == '(':
                        stack.pop()
                    elif c == '}' and stack[len(stack)-1] == '{':
                        stack.pop()
                    elif c == ']' and stack[len(stack)-1] == '[':
                        stack.pop()
                else:
                    stack.append(c)
                        
        if len(stack) == 0:
            print("YES")
        else: print("NO")

