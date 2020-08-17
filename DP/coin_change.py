# https://leetcode.com/problems/coin-change/
# You are given coins of different denominations and a total amount of money amount. 
# Write a function to compute the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        if amount < min(coins) or amount < 0:
            return -1
        
        c = [-1 for i in range(amount+1)]
        # s = [0 for i in range(amount+1)]
        
        c[0] = 0

        for a in range(1,amount+1):
            minimum = float("inf")
            for j in range(len(coins)):
                if coins[j] <= a:
                    # TODO: case coins = 2 and amount = 3
                    # if c[a - coins[j]] == -1:
                    #     c[a] = -1
                    if 1 + c[a - coins[j]] < minimum:
                        minimum = 1 + c[a - coins[j]]
            c[a] = minimum
            # s[a] = coins[j]
        return c[amount]
                
test = Solution()
coins = [2]
amount = 3
# coins = [186,419,83,408]
# amount = 6249
print(test.coinChange(coins, amount))
