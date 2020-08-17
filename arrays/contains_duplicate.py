# https://leetcode.com/problems/contains-duplicate/
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the 
# array, and it should return false if every element is distinct.

# ========== DONE
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # for i in range(0, len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if (nums[j] == nums[i]):
        #             return True
        # return False
        s = set(nums)
        return len(s) != len(nums)


A = [1, 2, 2, 1]
# A = [1,1,1,3,3,4,3,2,4,2]
# A = [1, 2, 3, 4]
test = Solution()
print(test.containsDuplicate(A))   
