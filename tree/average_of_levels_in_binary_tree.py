# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        if not root:
            return ans
        q = collections.deque([root])
        while q:
            tmp = list(q)
            q.clear()
            total = 0
            for t in tmp:
                total += t.val
                for node in [t.left, t.right]:
                    if node:
                        q.append(node)
            ans.append(total / len(tmp))
        return ans