# https://leetcode.com/problems/find-pivot-index/
# if a is pivot item, total sum - a = 2 * leftsum

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftsum = 0
        for i, num in enumerate(nums):
            if leftsum == total - leftsum - num:
                return i
            leftsum += num
        return -1
