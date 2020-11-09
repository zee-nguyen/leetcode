# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # Iterative with stack
        if not root or (not root.left and not root.right):
            return True
        else:
            s = []
            s.append(root.left)
            s.append(root.right)
            while s:
                top = s.pop()
                second = s.pop()

                if not top and not second:
                    continue
                if not top or not second or top.val != second.val:
                    return False
                
                s.append(top.left)
                s.append(second.right)

                s.append(top.right)
                s.append(second.left)
                    
        return True