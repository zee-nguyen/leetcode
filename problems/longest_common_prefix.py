# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        n = min(len(s) for s in strs)
        res = []
        for i in range(n):
            if not all(s[i]==strs[0][i] for s in strs):
                break
            else:
                res.append(strs[0][i])
        return ''.join(res)
