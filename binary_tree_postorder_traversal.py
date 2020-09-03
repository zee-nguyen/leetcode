# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # recursive
        # res = []
        # if root:
        #     if root.left:
        #         res.extend(self.postorderTraversal(root.left))
        #     if root.right:
        #         res.extend(self.postorderTraversal(root.right))
        #     res.append(root.val)
        # return res

        if not root:
            return []
        
        ret, s1, s2 = [], [root], []
        
        while s1:
            top = s1.pop()
            s2.append(top)
            if top.left:
                s1.append(top.left)
            if top.right:
                s1.append(top.right)
                
        while s2:
            ret.append(s2.pop().val)
            
        return ret
