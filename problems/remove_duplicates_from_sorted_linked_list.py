# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            # keep check next while it's equal current
            while cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next 
            cur = cur.next 
        return head
