# Given an array of integers A sorted in non-decreasing order, return an array of 
# the squares of each number, also in sorted non-decreasing order.
# Example:
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # return [x*x for x in A]
        return sorted(x*x for x in A)
        # sq = []
        # for num in A:
        #     sq.append(num * num)
        # sq.sort()
        # print(sq)
    
    
# Test
obj = Solution()
print(obj.sortedSquares([-4,-1,0,3,10]))