# https://leetcode.com/problems/cousins-in-binary-tree/

""" 
RT: O(n) where n is total number of nodes in the tree
Space: O(h) where h is height of the tree. Worst case O(n), balanced tree O(logn)
 """
 
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = deque([(root, None, 0)])
        first = None
        second = None
        while q:
            item, parent, level = q.popleft()
            
            if first and second:
                break
            
            if item.val == x:
                first = (item, parent, level)
                continue
            
            if item.val == y:
                second = (item, parent, level)
                continue
            
            if item.left:
                q.append((item.left, item, level + 1))
            if item.right:
                q.append((item.right, item, level + 1))
        
        return first and second and first[1].val != second[1].val and first[2] == second[2]