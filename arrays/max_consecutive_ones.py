# https://leetcode.com/problems/max-consecutive-ones/
# Given a binary array, find the maximum number of consecutive 1s in this array.

from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # count = 0
        # mx = 0
        # for i in range(len(nums)):
        #     if nums[i] == 1:
        #         count += 1
        #     else:
        #         if count > mx:
        #             mx = count    
        #         count = 0 # reset
        # if count > mx:
        #     return count
        # return mx
        
        count = 0
        max_count = 0
        for num in nums:
            count = 0 if num == 0 else count + 1
            max_count = max(count, max_count)
        return max_count

a = [1, 1, 0, 1, 1, 1]
# a = [0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]
# a = [1, 0, 1, 1, 0, 1]
test = Solution()
print(test.findMaxConsecutiveOnes(a))
