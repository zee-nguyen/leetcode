# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # Iterative
        # The idea is to have root - right - left using a stack, then reverse the list
        # if not root:
        #     return []
        
        # stack, ret = [root], []
        
        # while stack:
        #     top = stack.pop()
        #     if top:
        #         ret.append(top.val)
        #     stack.extend(top.children)
        
        # return ret[::-1]

        if not root:
            return []
        
        ret, s1, s2 = [], [root], []
        
        while s1:
            top = s1.pop()
            s2.append(top)
            for c in top.children:
                s1.append(c)
        
        while s2:
            ret.append(s2.pop().val)
            
        return ret


        # Recursive
        # if not root:
        #     return []

        # ret = []
        # for c in root.children:
        #     ret.extend(self.postorder(c))
        # ret.append(root.val)
        # return ret