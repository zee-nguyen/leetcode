# https://leetcode.com/problems/leaf-similar-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def getLeafSeq(root, seq):
            if not root:
                return
            if not root.left and not root.right:
                seq.append(root.val)
            getLeafSeq(root.left, seq)
            getLeafSeq(root.right, seq)
            return seq
        return getLeafSeq(root1, []) == getLeafSeq(root2, [])
