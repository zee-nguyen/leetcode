# https://leetcode.com/problems/find-common-characters/
# Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

# You may return the answer in any order.

# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] is a lowercase letter

# ========== DONE
from typing import List

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        count_dict = {}
        result = []

        for word in enumerate(A):
            # total occurances for each letter in this word
            letter_dict = {}

            for l in word[1]:
                if not l in letter_dict:
                    letter_dict[l] = 1
                else:
                    letter_dict[l] += 1    
            
            # final dict has letter as key and an array of total time it
            # appears in a word
            for k, v in letter_dict.items():
                if not k in count_dict:
                    count_dict[k] = [v]
                else:  
                    count_dict[k].append(v)

        for k, v in count_dict.items():
            # if a letter appears in each word, its length will be >= list len
            if (len(v) >= len(A)):
                for i in range(min(v)):
                    result.append(k)

        return result        

        

A = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
# A = ["bellaaaaa", "label", "roller"]
obj = Solution()
# obj.commonChars(A)
print(obj.commonChars(A))
# print(result)