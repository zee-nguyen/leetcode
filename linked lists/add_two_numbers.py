# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1, n2 = "", ""
        while l1:
            n1 += str(l1.val)
            l1 = l1.next
        while l2:
            n2 += str(l2.val)
            l2 = l2.next
        n1 = n1[::-1]
        n2 = n2[::-1]
        val = str(int(n1) + int(n2))
        new_head = ListNode(val[-1])
        tmp = new_head
        for i in range(len(val)-2, -1, -1):
            tmp.next = ListNode(val[i])
            tmp = tmp.next
        return new_head
            