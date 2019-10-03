# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        from collections import deque
        
        q = deque([root])
        ret = []
        
        while q:
            # get all nodes in current level
            nodes = list(q)
            q.clear()
            
            # only take the right 
            ret.append(nodes[-1].val)
            
            for node in nodes:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
        return ret