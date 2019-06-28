# https://leetcode.com/problems/partition-equal-subset-sum/

# Given a non-empty array containing only positive integers, find if the array 
# can be partitioned into two subsets such that the sum of elements in both subsets is equal.

# Note:

# Each of the array element will not exceed 100.
# The array size will not exceed 200.

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        
        # can't partition if total sum is odd
        if totalSum % 2 != 0 or len(nums) == 1:
            return False
        
        # Similar to 0-1 Knapsack, but our knapsack capacity is half of the total sum
        T = int(totalSum/2)

        # Initialize the DP table - col is each possible value of the sum (knapsack) and row is each item in the array
        C = [[False for i in range(T+1)] for i in range(len(nums))]

        for i in range(len(nums)):
            # If sum is 0, empty subset satisfies
            C[i][0] = True
            for j in range(T+1):
                if nums[i] == j:
                    # if sum is also the value of this item, we can make that sum
                    C[i][j] = True
                else:
                    # else, whether we can make this sum with current items or not depends on result of 2 cases:
                    # either we include the current item and the sub-pb becomes j - current item using the rest of the items
                    # or we don't include the current item and the sub-pb becomes - same amount j but using the rest of the items
                    C[i][j] = C[i-1][j] or C[i-1][j - nums[i]]


        return C[len(nums)-1][T]

a = [1,2,3]

test = Solution()
print(test.canPartition(a))