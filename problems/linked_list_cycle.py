# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # # O(n) space
        # seen = {}
        # cur = head
        # while cur:
        #     if cur not in seen:
        #         seen[cur] = 1
        #     else: # saw already, cycle
        #         return True
        #     cur = cur.next
        # return False
        
        # O(1) space
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next 
        
        while True:
            if slow == fast:
                return True
            if not fast.next or not fast.next.next:
                return False
            slow = slow.next
            fast = fast.next.next 
        return False
