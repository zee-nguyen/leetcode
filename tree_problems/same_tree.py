# https://leetcode.com/problems/same-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # null trees are the same
        if not p and not q:
            return True
        # one of the two is null -> not the same
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
            
# Test
# 1 is null, 2 is not and reversed
# both null
# the two are mirrored