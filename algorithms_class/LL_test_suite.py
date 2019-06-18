# Name: Phuong Nguyen (Zee)
# Homework 1 - CS5800 
# Problem 1 - Test Suite

from linked_list_intersection import Node
from linked_list_intersection import Solution
import unittest

class MyTest(unittest.TestCase):
    def test1(self):
        # ll1: 2 -> 12 -> 22 -> 32 -> 42
        node1 = Node(42)
        node2 = Node(32, node1)
        node3 = Node(22, node2)
        node4 = Node(12, node3)
        node5 = Node(2, node4)

        # ll2: 200 -> 101 -> 99 -> 12 -> 22 -> 32 -> 42
        node6 = Node(99, node4)
        node7 = Node(101, node6)
        node8 = Node(200, node7)

        test = Solution()
        self.assertEqual(test.ll_intersection(node5, node6), 12)

    def test2(self):
        # ll1: 42
        node1 = Node(42)

        # ll2: 123 -> 42
        node2 = Node(123, node1)

        test = Solution()
        self.assertEqual(test.ll_intersection(node1, node2), 42)

if __name__ == '__main__':
    unittest.main()