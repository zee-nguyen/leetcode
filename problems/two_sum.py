# https://leetcode.com/problems/two-sum
class Solution(object):
    def twoSum(self, nums, target):
        if not nums:
            return []
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        for j in range(len(nums)):
            comp = target - nums[j]
            if comp in d and d[comp] != j:
                return [j, d[comp]]
