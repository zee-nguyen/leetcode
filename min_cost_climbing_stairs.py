# https://leetcode.com/problems/min-cost-climbing-stairs
# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

# Once you pay the cost, you can either climb one or two steps. You need to find 
# minimum cost to reach the top of the floor, and you can either start from the 
# step with index 0, or the step with index 1.

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # tracking cost
        S = [0] * len(cost)
        #base cases
        S[0] = cost[0]
        S[1] = cost[1]
        for i in range(2, len(cost)):
            S[i] = min(S[i-1] + cost[i], S[i-2] + cost[i])
        # since we can go from n-2 or n-1 to n, take min of the 2
        return min(S[len(cost)-1], S[len(cost)-2])

# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
cost = [0, 1, 0, 1, 0, 1, 0]
# cost = [10, 15, 20]
test = Solution()
print(test.minCostClimbingStairs(cost))