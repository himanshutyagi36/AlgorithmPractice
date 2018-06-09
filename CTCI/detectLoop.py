"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    fastP = head
    slowP = head
    while (slowP and fastP.next and fastP.next):
        if fastP == slowP:
            return True
        fastP = fastP.next.next
        slowP = slowP.next
    return False
