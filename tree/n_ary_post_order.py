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
        # The idea is to have root - right - left using a stack, then reverse the list
        if not root:
            return []
        
        stack, ret = [root], []
        
        while stack:
            top = stack.pop()
            if top:
                ret.append(top.val)
            stack.extend(top.children)
        
        return ret[::-1]