# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        from collections import deque
        
        q = deque([(root, 1)])
        max_depth = 1
        
        while q:
            nodes = list(q)
            q.clear()
            
            for node, depth in nodes:
                max_depth = max(max_depth, depth)
                for child in node.children:
                    q.append((child, depth+1))
                    
        return max_depth