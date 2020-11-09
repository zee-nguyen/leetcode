# https://leetcode.com/problems/third-maximum-number/

# Given a non-empty array of integers, return the third maximum number in this array. 
# If it does not exist, return the maximum number. The time complexity must be in O(n).

from typing import List
import math

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if not nums:
            return
        # max 3 doesn't exist if total distinct numbers < 3
        if len(set(nums)) < 3:
            return max(nums)
        else:
            m1 = m2 = m3 = -math.inf
            for i in range(len(nums)):
                if nums[i] > m1:
                    m2, m3 = m1, m2
                    m1 = nums[i]
                elif m2 < nums[i] < m1:
                    m3 = m2
                    m2 = nums[i]
                elif m3 < nums[i] < m2:
                    m3 = nums[i]
            return m3

# A = [2, 2, 3, 1]
# A = [5, 7, 54, 2, 3, 44, 45, 77, 2]
# A = [1]
# A = [2, 3]
# A = []
# A = [101, 202, 303, 444, 32, 12, 3203, 49381, 3231, 43, 5]
A = [1,2,-2147483648]

# A = [1, 1, 0, 2]
test = Solution()
print(test.thirdMax(A))