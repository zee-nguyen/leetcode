# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ch_count = collections.Counter(chars)
        res = 0
        for word in words:
            w_count = collections.Counter(word)
            if w_count & ch_count == w_count:
                res += len(word)
        return res
