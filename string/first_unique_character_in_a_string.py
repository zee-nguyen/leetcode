# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for i, let in enumerate(s):
            if count[let] == 1:
                return i
        return -1
