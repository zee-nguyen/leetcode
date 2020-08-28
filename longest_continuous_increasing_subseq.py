# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

""" 
O(n) time
O(1) space
 """
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_len = 1
        len_so_far = 1
        
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                len_so_far += 1
            else:
                len_so_far = 1
            max_len = max(max_len, len_so_far)
            
        return max_len