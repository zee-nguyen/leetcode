# https://leetcode.com/problems/find-largest-value-in-each-tree-row/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        res = []
        q = deque([root])
        while q:
            tmp = list(q)
            q.clear()
            res.append(max(node.val for node in tmp))
            for node in tmp:
                for child in (node.left, node.right):
                    if child:
                        q.append(child)
        return res
