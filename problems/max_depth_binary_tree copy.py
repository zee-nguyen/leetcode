# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Recursive
        # base case - root empty
        # if not root:
        #     return 0

        # # get max depth left and max depth right + 1
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        # Iterative
        if not root:
            return 0
        
        s = []
        s.append((root, 1))
        max_depth = 1
        
        while s:
            node, depth = s.pop()
            max_depth = max(max_depth, depth)
            
            if node.left:
                s.append((node.left, depth+1))
            if node.right:
                s.append((node.right, depth+1))
                
        return max_depth