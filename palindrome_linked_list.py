# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # O(n) time, O(n) space
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return all(lst[i] == lst[~i] for i in range(len(lst)//2))
