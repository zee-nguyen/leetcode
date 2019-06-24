# https://leetcode.com/problems/longest-palindromic-subsequence/

# Given a string s, find the longest palindromic subsequence's length in s. 
# You may assume that the maximum length of s is 1000.
from typing import List

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
            find and calculate the length of the longest palindrome subsequence
        '''
        n = len(s)
        c = [[0 for i in range(n)] for i in range(n)]
        t = [["" for i in range(n)] for i in range(n)]

        for i in range(n):
            c[i][i] = 1
            t[i][i] = s[i]
        
        for l in range(2, n + 1):
            for i in range(0, n-l+1):
                j = i + l - 1
                if s[i] == s[j]:
                    c[i][j] = 2 + c[i+1][j-1]
                    t[i][j] = s[i] + t[i+1][j-1] + s[j]
                else:
                    if c[i][j-1] > c[i+1][j]:
                        c[i][j] = c[i][j-1]
                        t[i][j] = t[i][j-1]
                    else:
                        c[i][j] = c[i+1][j]
                        t[i][j] = t[i+1][j]
        return c[0][n-1], t

    def print_sol(self, t: List, s: str) -> str:
        '''
            print the longest palindromic subsequence
        '''
        return t[0][len(s)-1]



test = Solution()
s = "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew" #6
# s = "a"
# s = "baab"

length, t = test.longestPalindromeSubseq(s)
print(len(test.print_sol(t, s)))