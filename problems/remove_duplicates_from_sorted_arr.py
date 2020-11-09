# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        nxt = 1
        while nxt < len(nums):
            if nums[start] != nums[nxt]:
                nums[start + 1], nums[nxt] = nums[nxt], nums[start + 1]
                start += 1
            nxt += 1
        return start + 1