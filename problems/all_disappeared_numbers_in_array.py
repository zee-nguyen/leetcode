# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for val in nums:
            if nums[abs(val)-1] > 0:
                nums[abs(val)-1] = -nums[abs(val)-1] #mark as seen
        return [i+1 for i in range(len(nums)) if nums[i] > 0]
            