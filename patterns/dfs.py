# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        def dfs(path):
            node = path[-1]
            if not node.left and not node.right: #leaf
                tmp = [str(n.val) for n in path]
                tmp = '->'.join(tmp)
                paths.append(tmp)
                return
            for child in (node.left, node.right):
                if child:
                    path.append(child)
                    dfs(path)
                    path.pop()
        if root:
            dfs([root])
        return paths
