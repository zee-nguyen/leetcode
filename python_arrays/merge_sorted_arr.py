# https://leetcode.com/problems/merge-sorted-array/
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to 
# m + n) to hold additional elements from nums2.

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 or not nums2:
            return
        i = m - 1
        j = n - 1
        k = len(nums1) - 1
        while (k >= 0):
            if (i < 0): # list 1 is exhausted
                nums1[k] = nums2[j]
                j -= 1
            elif (nums1[i] >= nums2[j]) or (j < 0):
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

# A = [0, 0, 1, 2, 2, 3, 6, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0]
# B = [2, 5, 6, 7, 8, 8, 9, 10]
# A = [0, 2, 5, 6, 0, 0]
# B = [0, 1]
# A = [1]
# B = []
A = [1, 2, 0]
B = [6]
test = Solution()
# print(test.merge(A, 9, B, 8))
test.merge(A, 2, B, 1)
print(A)