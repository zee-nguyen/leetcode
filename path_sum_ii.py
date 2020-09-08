# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, total: int) -> List[List[int]]:
        paths = []
        def dfs(path):
            node = path[-1]
            if not node.left and not node.right: #leaf
                path_total = sum(n.val for n in path)
                if path_total == total:
                    paths.append([n.val for n in path])
                return
            for child in (node.left, node.right):
                if child:
                    path.append(child)
                    dfs(path)
                    path.pop()
                    
        if root:
            dfs([root])
        return paths
