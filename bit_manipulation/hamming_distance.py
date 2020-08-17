# https://leetcode.com/problems/hamming-distance/
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, calculate the Hamming distance.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        while x or y:
            ans += (x&1) ^ (y&1)
            x >>= 1
            y >>= 1
        return ans