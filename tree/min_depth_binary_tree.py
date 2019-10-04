# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        from collections import deque
        
        q = deque([(root, 1)])
        min_depth = float("inf")
        
        while q:
            nodes = list(q)
            q.clear()
            
            for node, depth in nodes:
                # only consider if this is leaf node
                if not node.left and not node.right:
                    min_depth = min(min_depth, depth)
                
                if node.left:
                    q.append((node.left, depth+1))
                if node.right:
                    q.append((node.right, depth+1))
        return min_depth