# https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(s):
            return all(s[i] == s[~i] for i in range(len(s)//2))
        
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return isPalindrome(s[i:j]) or isPalindrome(s[i+1:j+1])
            i += 1
            j -= 1
        return True
