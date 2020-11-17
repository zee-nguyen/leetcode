# https://leetcode.com/problems/maximum-number-of-balloons/


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_c = collections.Counter(text)
        bal_c = collections.Counter('balloon')
        
        return min(text_c[ch]//bal_c[ch] for ch in bal_c)
