# https://leetcode.com/problems/fixed-point/

# Given an array A of distinct integers sorted in ascending order, return the smallest index i that satisfies A[i] == i.  Return -1 if no such i exists.

from typing import List

class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        # for i in range(len(A)):
        #     if i == A[i]:
        #         return i
        # return -1
        n = len(A)
        s = 0
        e = n-1
        while (s < e):
            m = s+e//2
            if A[s] == s: return s
            elif A[m] > m: #left
                e = m
            else:
                s = m + 1
        return -1
        

A = [-10,-5,0,3,7] #3
test = Solution()
print(test.fixedPoint(A))