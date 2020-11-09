# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements that appear twice in this array.
# Could you do it without extra space and in O(n) runtime?

from typing import List
from collections import Counter

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        dup = {x: count[x] for x in count if count[x] >= 2}
        return list(dup.keys())

        # Still thinking of without extra space...

A = [4,3,2,7,8,2,3,1]
test = Solution()
print(test.findDuplicates(A))
        