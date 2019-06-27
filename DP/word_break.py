# https://leetcode.com/problems/word-break/
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note:

# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # brute force - look at all prefixes and suffixes
        # if n == 0:
        #     return True
        # else:
        #     for i in range(0, n):
        #         if s[0:i+1] in wordDict and self.wordBreak(s[i+1:n], wordDict):
        #             return True
        # return False
        
        C = [[False for i in range(n)] for i in range(n)]

        for i in range(n):
            C[i][i] = True if s[i] in wordDict else False

        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                if s[i:j+1] in wordDict:
                    C[i][j] = True
                else:
                    for k in range(j):
                        flag = False
                        if (C[i][k] and C[k+1][j]):
                            flag = True
                            C[i][j] = flag
        return C[0][n-1]

test = Solution()
wordDict = ["leet", "code"]
s = "leetcode"
# wordDict = ["apple", "pen"]
# s = "applepenapple"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# s = "catsandog"
# wordDict = ["i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"]
# s = "isam"
# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(test.wordBreak(s, wordDict))