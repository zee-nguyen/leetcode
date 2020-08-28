# https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. 
# Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
# Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            # insert left
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        
        return root
    
        '''
            Iterative

            tmp = root
            while tmp:
                if val < tmp.val:
                    # Insert left
                    if not tmp.left:
                        tmp.left = TreeNode(val)
                        return root
                    else:
                        tmp = tmp.left
                else:
                    if not tmp.right:
                        tmp.right = TreeNode(val)
                        return root
                    else:
                        tmp = tmp.right
            # Code gets here if root doesn't exist
            return TreeNode(val)
        '''
