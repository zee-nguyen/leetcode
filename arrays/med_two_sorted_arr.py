# https://leetcode.com/problems/median-of-two-sorted-arrays/

# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.
from typing import List

class Solution:
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    def findMedianSortedArrays(self, X: List[int], Y: List[int]) -> int:
        n = len(X)
        i = n//2
        medX = X[i]
        medY = Y[i]
        
        if n == 1:
            return min(X[0], Y[0])
        elif medX == medY:
            return medX
        elif medX > medY:
            # TODO: try different recursive call for different indices when n is even or odd
            return self.findMedianSortedArrays(X[:i+1], Y[i:])
        else:
            return self.findMedianSortedArrays(X[i:], Y[:i+1])

X = [1, 2, 4, 7, 8, 10, 13]
Y = [2, 5, 6, 8, 9, 12, 15]
test = Solution()
print(test.findMedianSortedArrays(X, Y))