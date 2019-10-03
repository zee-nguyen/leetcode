# https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Iterative solution. 
        # Stack to keep track of nodes
        # prev to compare if previous node is < current node
        stack = []
        prev = None 
        
        if root is None:
            return True
        
        while root is not None or stack:
            # go left if still possible
            while root is not None:
                stack.append(root)
                root = root.left
            
            # when we can't go left anymore, pop off the top of stack and try to go right from here
            root = stack[-1]
            stack.pop()
            # if prev >= current, not valid BST
            if prev is not None and prev.val >= root.val:
                return False
            prev = root
            root = root.right
        return True
