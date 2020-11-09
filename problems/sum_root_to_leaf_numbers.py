# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.ans = 0
        
        def dfs(path):
            node = path[-1]
            if not node.left and not node.right: #leaf
                # convert list of nodes to list of node vals
                tmp = [n.val for n in path]
                tmp_val = sum(d * 10**i for i, d in enumerate(tmp[::-1]))
                self.ans += tmp_val
                return
            for child in (node.left, node.right):
                if child:
                    path.append(child)
                    dfs(path)
                    path.pop()
        if root:
            dfs([root])
        return self.ans
