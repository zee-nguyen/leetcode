# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Solution below was because I didn't fully understand the question
        # I forgot that the head is keeping track of the least-significant digit
        # ie that's where we can start adding
        # n1, n2 = "", ""
        # while l1:
        #     n1 += str(l1.val)
        #     l1 = l1.next
        # while l2:
        #     n2 += str(l2.val)
        #     l2 = l2.next
        # n1 = n1[::-1]
        # n2 = n2[::-1]
        # val = str(int(n1) + int(n2))
        # new_head = ListNode(val[-1])
        # tmp = new_head
        # for i in range(len(val)-2, -1, -1):
        #     tmp.next = ListNode(val[i])
        #     tmp = tmp.next
        # return new_head

        # better solution
        
        dummy = ListNode(-1) # dummy head
        tmp1, tmp2, carry = l1, l2, 0
        curr = dummy
        while tmp1 or tmp2:
            p = tmp1.val if tmp1 is not None else 0
            q = tmp2.val if tmp2 is not None else 0
            total = p + q + carry
            carry = total / 10
            curr.next = ListNode(total % 10)
            tmp1 = tmp1.next
            tmp2 = tmp2.next
            curr = curr.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummy.next
            