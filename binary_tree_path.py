# https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # Iterative
        if not root:
            return []
        
        ret = []
        nodes = []
        paths = []
        
        nodes.append(root)
        paths.append(str(root.val))
        
        while nodes:
            top = nodes.pop()
            cur = paths.pop()
            
            if not top.left and not top.right: #leaf
                ret.append(cur)
            else:
                if top.right:
                    nodes.append(top.right)
                    paths.append(cur + "->" + str(top.right.val))
                if top.left:
                    nodes.append(top.left)
                    paths.append(cur + "->" + str(top.left.val))
        
        return ret
                