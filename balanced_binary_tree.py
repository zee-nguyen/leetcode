# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

""" Analysis:
In the worse case, for each node, we check the height of its left subtree and right subtree, i.e. we traverse down the tree and
check each path, so we look at N nodes.
We do the same thing for N nodes, so total time is O(N^2)

Space is at most O(H) where H is the height of the tree. This is the space for the recursive call stack. Worst case, when the tree is 
skewed, it's O(N). Best case, the tree is balanced and it's O(logN)
 """

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def depth(node):
            if not node:
                return 0
            return max(depth(node.left), depth(node.right)) + 1
        
        l_depth = depth(root.left)
        r_depth = depth(root.right)
        
        return abs(l_depth - r_depth) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    