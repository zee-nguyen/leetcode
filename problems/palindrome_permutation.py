# https://leetcode.com/problems/palindrome-permutation/

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        c = collections.Counter(s)
        return sum(v % 2 for v in c.values()) <= 1
