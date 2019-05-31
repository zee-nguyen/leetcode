# https://leetcode.com/problems/majority-element/

# Given an array of size n, find the majority element. 
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element 
# always exist in the array.

from typing import List
# from collections import defaultdict
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]
        # count = defaultdict(lambda: 0)
        # for i in range(len(nums)):
        #     count[nums[i]] += 1
        # return max(count, key=count.get)

test = Solution()
# nums = [1, 1, 1, 2, 2, 2, 2, 2, 2]
# nums = [3, 2, 3]
nums = [1, 2, 3, 4, 5, 5, 3, 4, 2, 7, 6, 1, 1, 2, 2, 2, 3]
print(test.majorityElement(nums))
