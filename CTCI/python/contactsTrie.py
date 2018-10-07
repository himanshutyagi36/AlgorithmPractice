#!/bin/python3

import math
import os
import random
import re
import sys

class Node:
    def __init__(self):
        self.count = 1
        self.children = {}
        
trie = Node()

def add(node, name):
    for letter in name:
        sub = node.children.get(letter)  # 1
        if sub:
            sub.count += 1
        else:
            sub = node.children[letter] = Node()  # 2
        node = sub  # 3
# 1. looping on each letter of the passed contact name, if the children dictionary in this level contains the relative letter, I access that node and increase its counter.
# 2. Otherwise I create a new node in the dictionary using as key the current letter.
# 3. Then I follow the recursive trie structure passing to the node in the level below.

def find(node, name):
    for letter in name:
        sub = node.children.get(letter)
        if not sub:
            return 0
        node = sub
    return node.count
            
    

if __name__ == '__main__':
    n = int(input())

    for n_itr in range(n):
        opContact = input().split()

        op = opContact[0]

        contact = opContact[1]
        if op == "add":
            add(trie, contact)
        elif op == "find":
            count = find(trie, contact)
            print (count)

