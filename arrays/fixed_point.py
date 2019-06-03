# https://leetcode.com/problems/fixed-point/

# Given an array A of distinct integers sorted in ascending order, return the smallest index i that satisfies A[i] == i.  Return -1 if no such i exists.

from typing import List

class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        for i in range(len(A)):
            if i == A[i]:
                return i
        return -1

A = [0]
test = Solution()
print(test.fixedPoint(A))