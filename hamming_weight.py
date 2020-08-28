# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        # 1
        ans = 0
        while n:
            ans += 1
            n &= n-1
        return ans

        # 2
        ans = 0
        while n:
            ans += (n & 1)
            n >>= 1
        return ans
