# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort() #increasing order
        result = [nums.pop()] # get biggest element
        while sum(result) <= sum(nums): #keep adding element when not valid yet
            result.append(nums.pop())
        return result
