# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

import unittest

# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # Recursively
        def helper(root, res):
            if not root:
                return
            res.append(root.val)
            for c in root.children:
                helper(c, res)
        res = []
        helper(root, res)
        return res
    
        # Iteratively
        if not root:
            return [] 
        
        stack = []
        res = []
        stack.append(root)
        while stack:
            top = stack.pop()
            i = len(top.children)-1
            res.append(top.val)
            while i >= 0 and top.children:
                stack.append(top.children[i])
                i -= 1
        return res
