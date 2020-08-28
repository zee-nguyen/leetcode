# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        def height(root):
            if not root:
                return 0
            left_h = height(root.left)
            right_h = height(root.right)
            # the longest path between two nodes (diameter) always goes through some root, but keeping track of the longest path because it could occur on either side of a tree 
            self.ans = max(left_h + right_h, self.ans)
            return max(left_h, right_h) + 1
        
        height(root)
        return self.ans
