# https://leetcode.com/problems/remove-linked-list-elements/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # use dummy to check for the case where head.val == val
        dummy = ListNode(-1)
        dummy.next = head
        
        cur = dummy
        while cur.next: # we want to check if next node == val, need to check if it's a valid node
            if cur.next.val == val:
                cur.next = cur.next.next # skip this node
                # but don't move current yet because we need to check if the new node we just move
                # cur.next to is equal to val or not
            else:
                cur = cur.next 
        return dummy.next
