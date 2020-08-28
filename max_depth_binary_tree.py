# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the 
# root node down to the farthest leaf node.
# Note: A leaf is a node with no children.

from collections import dequeue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        max_left = self.maxDepth(root.left)
        max_right = self.maxDepth(root.right)
        
        max_depth = max(max_left, max_right) + 1
        
        return max_depth

