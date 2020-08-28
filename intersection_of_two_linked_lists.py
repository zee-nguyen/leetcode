# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getLength(self, head):
        length = 0
        if head is None:
            return length
        tmp = head
        while tmp is not None:
            length += 1
            tmp = tmp.next
        return length

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
            
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        
        # A is always the shorter list, so swap if we need to
        if lenA > lenB:
            headA, headB = headB, headA
        
        dif = abs(lenB - lenA)

        tmpA = headA
        tmpB = headB

        for i in range(dif):
            tmpB = tmpB.next

        # now both lists are at the same pos
        while tmpA is not None and tmpB is not None:
            if tmpA is tmpB:
                return tmpA
            tmpA = tmpA.next
            tmpB = tmpB.next
        
        # if the code gets here, intersection doesn't exist
        return None
