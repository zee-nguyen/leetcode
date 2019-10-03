# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
         # recursive
        def build_path(node, path, ret):
            if not node:
                return
            
            if not node.left and not node.right: #at leaf, add and append to ret
                path += str(node.val)
                ret.append(path)
            else:
                path += str(node.val) + "->"
                
                if node.left:
                    build_path(node.left, path, ret)
                if node.right:
                    build_path(node.right, path, ret)
            
        ret = []
        path = ""
        build_path(root, path, ret)
        
        return ret