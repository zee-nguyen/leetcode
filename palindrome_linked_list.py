# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # O(n) time, O(n) space
        # lst = []
        # while head:
        #     lst.append(head.val)
        #     head = head.next
        # return all(lst[i] == lst[~i] for i in range(len(lst)//2))

        # O(n) time O(1) space
        # travel to mid of list, reverse the second half then compare the two halves
        def reverseLL(node):
            prev, cur = None, node
            while cur:
                tmp = cur.next 
                cur.next = prev 
                prev = cur
                cur = tmp
            return prev
        
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next 
        
        first_half, second_half = head, reverseLL(slow)
        while first_half and second_half:
            if first_half.val != second_half.val:
                return False
            first_half, second_half = first_half.next, second_half.next 
        return True
