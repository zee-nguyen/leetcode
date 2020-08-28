# https://leetcode.com/problems/range-sum-of-bst/
# Given the root node of a binary search tree, return the sum of values of 
# all nodes with value between L and R (inclusive).
# The binary search tree is guaranteed to have unique values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        total = 0
        if root == None:
            return total
        else:
            if L <= root.val <= R:
                total += root.val
            if L < root.val:
                total += self.rangeSumBST(root.left, L, R)
            if R > root.val:
                total += self.rangeSumBST(root.right, L, R)
            return total
