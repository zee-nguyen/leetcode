# https://leetcode.com/problems/rotate-array/
# Given an array, rotate the array to the right by k steps, where k is non-negative.

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # result = []
        # for i in range(len(nums) - k, len(nums)):
        #     result.append(nums[i])
        # for j in range(0, len(nums) - k):
        #     result.append(nums[j])
        # return result

        # In place - exceeds time limit
        # for i in range(k % len(nums)):
        #     key = nums[len(nums) - 1]    
        #     j = len(nums) - 2
        #     while (j >= 0):
        #         nums[j+1] = nums[j]
        #         j -= 1
        #     nums[j+1] = key
        # return nums

        # k = 0, nothing changes
        if k == 0: 
            return nums
        
        n = len(nums)
        i = 0
        j = n - k
        while j < n:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        self.rotate(nums[n - k - 1:], k % (n - k))
            

A = [1, 2, 3, 4, 5, 6, 7]
k = 3
# A = [-1,-100,3,99]
# k = 2
# A = [1, 2]
# k = 3
test = Solution()
print(test.rotate(A, k))