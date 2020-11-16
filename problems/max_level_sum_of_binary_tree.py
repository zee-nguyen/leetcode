# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        max_lev = 1
        max_sum = float("-inf")
        q = deque([(root, 1)])
        while q:
            tmp = list(q)
            q.clear()
            cur_lev = -1
            lev_sum = 0
            for node, lev in tmp:
                cur_lev = lev
                lev_sum += node.val
                for child in (node.left, node.right):
                    if child:
                        q.append((child, lev+1))
            
            if lev_sum > max_sum:
                max_sum = lev_sum
                max_lev = cur_lev
        return max_lev
