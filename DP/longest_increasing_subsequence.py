# https://leetcode.com/problems/longest-increasing-subsequence/
# Given an unsorted array of integers, find the length of longest increasing subsequence.

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # Initialize the table
        C = [1 for i in range(n)]

        for i in range(1,n):
            for k in range(0, i):
                if nums[i] > nums[k] and C[k] + 1 > C[i]:
                    C[i] = C[k] + 1
           
        return max(C) if C else 0

test = Solution()
# n = []
n = [1,2,3]
# n = [10,9,2,5,3,7,101,18]
# n = [50, 3, 10, 7, 40, 80]
# n = [3, 10, 2, 1, 20]
print(test.lengthOfLIS(n))