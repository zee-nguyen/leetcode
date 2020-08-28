# https://leetcode.com/problems/maximum-subarray/
# Given an integer array nums, find the contiguous subarray (containing at least 
# one number) which has the largest sum and return its sum.

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if the array in empty, max sum is 0
        if not nums:
            return 0

        C = [0 for i in nums]
        C[0] = nums[0]
        for i in range(1, len(nums)):
            C[i] = max(C[i-1] + nums[i], nums[i])
        return max(C)

test = Solution()
input = [-2,1,-3,4,-1,2,1,-5,4]
print(test.maxSubArray(input))