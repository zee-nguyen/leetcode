# https://leetcode.com/problems/most-common-word/

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        normalized = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        words = normalized.split()
        count = collections.defaultdict(int)
        banned_words = set(banned)
        
        for word in words:
            if word not in banned_words:
                count[word] += 1
        return max(count, key=count.get)
