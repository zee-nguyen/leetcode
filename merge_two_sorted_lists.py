# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        tmp = head
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
        tmp.next = l1 or l2
        return head.next
        # if l1 is None:
        #     return l2
        # elif l2 is None:
        #     return l1
        # else:
        #     if l1.val <= l2.val:
        #         head = l1
        #         head.next = self.mergeTwoLists(l1.next, l2)
        #     else:
        #         head = l2
        #         head.next = self.mergeTwoLists(l1, l2.next)
        # return head
        


