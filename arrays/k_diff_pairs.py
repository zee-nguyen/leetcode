# https://leetcode.com/problems/k-diff-pairs-in-an-array/

# Given an array of integers and an integer k, you need to find the number of 
# unique k-diff pairs in the array. Here a k-diff pair is defined as an integer 
# pair (i, j), where i and j are both numbers in the array and their absolute 
# difference is k.

# The pairs (i, j) and (j, i) count as the same pair.
# The length of the array won't exceed 10,000.
# All the integers in the given input belong to the range: [-1e7, 1e7].

from typing import List
from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        pairs = []
        myDict = Counter(nums)
        # can't get a pair from list of len 0 or 1
        if len(nums) == 0 or len(nums) == 1:
            return 0
        else:
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if abs(nums[i] - nums[j]) == k:
                        single_pair = {nums[i], nums[j]}
                        if single_pair not in pairs:
                            pairs.append(single_pair)
        return len(pairs)


# A = [3, 1, 4, 1, 5]
# k = 2
# A = [1, 2, 3, 4, 5]
# k = 1
# A = [1, 3, 1, 5, 4]
# k = 0
# A = [1,1]
# k = 0
test = Solution()
print(test.findPairs(A, k))