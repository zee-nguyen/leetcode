# https://leetcode.com/problems/middle-of-the-linked-list
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Fast-slow pointers
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next #move 2 nodes
            slow = slow.next #move 1 node
        return slow
            