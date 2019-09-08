# https://leetcode.com/problems/valid-palindrome/

# Observation:
# Since we're only looking at alphanumeric characters, we need to process the input string to get rid of what doesn't qualify
# Then, we can run 2 pointers to check if the pre-processed string is a palindrome
# while left < right: 
# if two pointers are the same, increment left and decrement right 
# if they're different, return False since this is not a palindrome
# at the end, if two pointers cross and the program doesn't return false, then this is a valid palinrome

# Afterthought:
# Some part can be enhanced as below

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j-=1
            else:
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i+=1
                    j-=1
        return True
