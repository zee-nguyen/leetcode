# Name: Phuong Nguyen (Zee)
# Homework 1 - CS5800 
# Problem 1

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def get_next(self):
        return self.next

class Solution:
    def size_ll(self, head: Node) -> int:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.get_next()
        return count

    def ll_intersection(self, headA: Node, headB: Node) -> Node:
        '''
        Function: ll_intersection
        Params: headA, headB are the head node of two linked lists
        return: the first node that list A and list B intersects
        '''
        lenA = self.size_ll(headA)
        lenB = self.size_ll(headB)

        # assuming len A > len B
        # curA is always the longer list
        curA, curB = headA, headB
        shorterLen = lenB

        if lenA < lenB:
            curA, curB = headB, headA
            shorterLen = lenA
        for i in range(abs(lenA-lenB)):
            curA = curA.get_next()

        for j in range(shorterLen):
            if (curA == curB):
                return curA.data
            curA = curA.get_next()
            curB = curB.get_next()