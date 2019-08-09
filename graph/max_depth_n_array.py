# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
# Given a n-ary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root 
# node down to the farthest leaf node.
# Note:
# The depth of the tree is at most 1000.
# The total number of nodes is at most 5000.


# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        maxDepth = 0
        for c in root.children:
            maxDepth = max(maxDepth, self.maxDepth(c))
        return maxDepth + 1

