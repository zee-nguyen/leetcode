# https://leetcode.com/problems/merge-two-binary-trees/

# Given two binary trees and imagine that when you put one of them to cover 
# the other, some nodes of the two trees are overlapped while the others are not.

# You need to merge them into a new binary tree. The merge rule is that if two 
# nodes overlap, then sum node values up as the new value of the merged node. 
# Otherwise, the NOT null node will be used as the node of new tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            t3 = TreeNode(t1.val + t2.val)
            t3.left = self.mergeTrees(t1.left, t2.left)
            t3.right = self.mergeTrees(t1.right, t2.right)
        else: 
            return t1 or t2

        return t3

        # if t1 == None and t2 == None:
        #     return None
        # elif t1 == None:
        #     t3 = TreeNode(t2.val)
            
        # elif t2 == None:
        #     t3 = TreeNode(t1.val)
        # else:
        #     t3 = TreeNode(t1.val + t2.val)

        # if t1 == None:
        #     t3 = t2
        # elif t2 == None:
        #     t3 = t1
        # else:
        #     t3.left = self.mergeTrees(t1.left, t2.left)
        #     t3.right = self.mergeTrees(t1.right, t2.right)

        # return t3
