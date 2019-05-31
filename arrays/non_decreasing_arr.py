# https://leetcode.com/problems/non-decreasing-array/

# Given an array with n integers, your task is to check if it could become
# non-decreasing by modifying at most 1 element.
# We define an array is non-decreasing if array[i] <= array[i + 1] 
# holds for every i (1 <= i < n). The n belongs to [1, 10,000].

from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        inverted_count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                nums[i] = nums[i+1]
                inverted_count += 1
        for i in range(len(nums) - 1):
            # if there still exists inverted pairs or inverted_count > 1
            if nums[i] > nums[i+1] or inverted_count > 1:
                return False
        return True

# A = [4, 2, 3]
# A = [3, 4, 2, 3]
# A = [1,5,4,6,7,10,8,9]
# A = [1, 2, 3, 1, 3]
A = [2,3,3,2,4]
2,3,2,2,4
test = Solution()
print(test.checkPossibility(A))