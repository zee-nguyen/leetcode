# https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        table = collections.Counter(p)
        counter = len(table)
        size = len(p)
        
        begin = end = 0
        ans = []
        
        if (len(s) < len(p)) or len(s) == 0:
            return ans
        
        while end < len(s):
            end_char = s[end]
            if end_char in table:
                table[end_char] -= 1
                if table[end_char] == 0:
                    counter -= 1
            end += 1
            
            while counter == 0:
                if end-begin == size:
                    ans.append(begin)
                
                begin_char = s[begin]
                if begin_char in table:
                    table[begin_char] += 1
                    if table[begin_char] > 0:
                        counter += 1
                begin += 1
        return ans
