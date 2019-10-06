class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_so_far = float("inf"), 0
        
        for price in prices:
            min_price = min(min_price, price) #min price so far
            profit = price - min_price
            max_so_far = max(profit, max_so_far)
        
        return max_so_far
        