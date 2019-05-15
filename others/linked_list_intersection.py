# Two linked lists that intersect at some point
# Different length. Find the first intersection 

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def get_next(self):
        return self.next

class Solution:
    # size of LL
    def size_ll(self, head: Node) -> int:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.get_next()
        return count

    '''
        Function: ll_intersection
        Params: headA, headB are the head node of two linked lists
        return: the first node that list A and list B intersects
    '''
    def ll_intersection(self, headA: Node, headB: Node) -> Node:
        # find length of each list
        lenA = self.size_ll(headA)
        lenB = self.size_ll(headB)

        offset = abs(lenA - lenB)
        start = Node()
        shorterLen = 0
        curA = Node()
        curB = Node()

        if lenA == lenB:
            curA = headA
            curB = headB
            shorterLen = lenA
        elif lenA > lenB:
            shorterLen = lenB
            temp = headA
            for i in range(offset):
                start = temp.next
                temp = temp.next
            
            curA = start
            curB = headB
        else:
            shorterLen = lenA
            temp = headB
            for i in range(offset):
                start = temp.next
                temp = temp.next
            curB = start
            curA = headA
        
        for i in range(shorterLen):
            if (curA.data == curB.data):
                return curA.data
            curA = curA.next
            curB = curB.next

# ll1: 2 -> 12 -> 22 -> 32 -> 42
node1 = Node(42)
node2 = Node(32, node1)
node3 = Node(22, node2)
node4 = Node(12, node3)
node5 = Node(2, node4)

# ll1 = LinkedList(node4)

# ll2: 200 -> 101 -> 99 -> 22 -> 32 -> 42
node6 = Node(99, node4)
# node7 = Node(101, node6)
# node8 = Node(200, node7)

# ll2 = LinkedList(node6)

test = Solution()
print(test.ll_intersection(node5, node6))