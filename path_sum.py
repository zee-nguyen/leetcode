# https://leetcode.com/problems/path-sum/
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
# such that adding up all the values along the path equals the given sum.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        

test = Solution()
node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(11)
node5 = TreeNode(13)
node6 = TreeNode(4)
node7 = TreeNode(7)
node8 = TreeNode(2)
node9 = TreeNode(1)

node1.left = node2
node1.right = node3
node2.left = node4
node4.left = node7
node4.right = node8
node3.left = node5
node3.right = node6
node6.right = node9

# tree = [5,4,8,11,None,13,4,7,2,None,None,None,1]
sm = 22 #TRUE
# [10, 8, 2, 3, 5,2,null]
# [11,2,5,4,null,9,7,7,8,6,null,null,4,10,null,1,null,null,5]
print(test.hasPathSum(node1, sm))