# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ret = []
        
        if not root:
            return ret
        
        from collections import deque
        
        q = deque([root])
        
        while q:
            nodes = list(q)
            q.clear()
            
            level = []
            
            for node in nodes:
                level.append(node.val)
                q.extend(node.children)
                
            ret.append(level)
            
        return ret