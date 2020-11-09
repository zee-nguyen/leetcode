# https://leetcode.com/problems/3sum/
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# Note: The solution set must not contain duplicate triplets.

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) < 3: 
            return result
        if len(nums) == 3 and sum(nums) != 0:
            return result
        
        sorted_arr = sorted(nums)

        for i in range(len(sorted_arr) - 1):
            j = i + 1
            k = len(sorted_arr) - 1

            while (j < k):
                if (sorted_arr[i] + sorted_arr[j] + sorted_arr[k]) == 0:
                    tup = [sorted_arr[i], sorted_arr[j], sorted_arr[k]]
                    if not tup in result:
                        result.append(tup)
                    j += 1
                elif (sorted_arr[i] + sorted_arr[j] + sorted_arr[k]) < 0: # need bigger number
                    j += 1
                else: # need smaller number
                    k -= 1
        
        return result

test = Solution()
A = [1,2,3]
# A = [-1, 0, 1, 2, -1, -4]
print(test.threeSum(A))