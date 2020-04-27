# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

# Given a sorted array nums, remove the duplicates in-place such that each element
# appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        i = 0
        j = i+1
        while j <= len(nums)-1:
            if nums[i] != nums[j]:
                nums[i+1], nums[j] = nums[j], nums[i+1]
                i = i + 1
            j = j + 1
        return i + 1
