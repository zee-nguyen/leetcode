# https://leetcode.com/problems/single-number/
# Your algorithm should have a linear runtime complexity. 
# Could you implement it without using extra memory?

from typing import List
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a
        # count = Counter(nums)
        # for k, v in count.items():
        #     if v == 1:
        #         return k

test = Solution()
arr = [4,2,1,2,1]
print(test.singleNumber(arr))
