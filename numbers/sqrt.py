# https://leetcode.com/problems/sqrtx/

# This runs too slow: 2792 ms

class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0

        while i <= x and i * i <= x:
            i += 1

        return i-1