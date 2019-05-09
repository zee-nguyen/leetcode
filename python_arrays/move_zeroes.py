# https://leetcode.com/problems/move-zeroes/
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, j = 0, 1
        while (i < len(nums) and j < len(nums)):
            if (nums[i] != 0):
                i += 1
                j += 1
            elif (nums[j] != 0):
                nums[i], nums[j] = nums[j], nums[i]    
                i += 1
                j += 1
            else:
                j += 1      

# A = [0, 1, 0, 3, 12]
A = [0, 12, 0, 4, 5, 0, 0, 6, 0, 11]
test = Solution()
print(test.moveZeroes(A))    