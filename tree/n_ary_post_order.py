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
        if not root:
            return []
        ret = []
        
        for child in root.children:
            ret.extend(self.postorder(child))
        
        ret.append(root.val)
        return ret