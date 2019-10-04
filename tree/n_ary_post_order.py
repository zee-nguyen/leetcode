# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # Iterative
        # The idea is to have rioot - right - left using a stack, then reverse the list
        if not root:
            return []
        
        stack, ret = [root], []
        
        while stack:
            top = stack.pop()
            if top:
                ret.append(top.val)
            for c in top.children:
                stack.append(c)
        
        return ret[::-1]