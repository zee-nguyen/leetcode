# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        res = 0
        counter_s = collections.Counter(s)
        counter_t = collections.Counter(t)
        for ch in counter_s:
            if counter_t[ch] < counter_s[ch]:
                continue
            else:
                res += (counter_s[ch] - counter_t[ch])
        return res
