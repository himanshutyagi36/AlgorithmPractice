""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
INT_MAX = 4294967296
INT_MIN = -4294967296
def checkBST(root):
    return (checkBSTUtil(root, INT_MIN, INT_MAX))
    
def checkBSTUtil(root, min, max):
    # if tree is empty
    if root is None:
        return True
    # if it fails the value constraints
    if root.data < min or root.data > max:
        return False
    # recursively check the left and right subtrees
    return (checkBSTUtil(root.left, min, root.data-1) and checkBSTUtil(root.right, root.data+1, max))
    
        
