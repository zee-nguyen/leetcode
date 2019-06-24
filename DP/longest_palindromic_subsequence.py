# https://leetcode.com/problems/longest-palindromic-subsequence/

# Given a string s, find the longest palindromic subsequence's length in s. 
# You may assume that the maximum length of s is 1000.

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        c = [[0 for i in range(n)] for i in range(n)]

        for i in range(n):
            c[i][i] = 1
        
        for l in range(2, n + 1):
            for i in range(0, n-l+1):
                j = i + l - 1
                if s[i] == s[j]:
                    c[i][j] = 2 + c[i+1][j-1]
                else:
                    c[i][j] = max(c[i][j-1], c[i+1][j])
        return c[0][n-1]

test = Solution()
s = "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew" #6
# s = "a"
# s = "baab"

print(test.longestPalindromeSubseq(s))