# https://leetcode.com/problems/search-in-a-binary-search-tree/
# Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's 
# value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return root
        elif root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return None