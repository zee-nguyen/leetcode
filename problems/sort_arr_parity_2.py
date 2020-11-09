# https://leetcode.com/problems/sort-array-by-parity-ii/

# Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
# You may return any answer array that satisfies this condition.

from typing import List

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        # if length is less than 2, return
        if (len(A) < 2):
            return
        else:
            i = 0
            j = i + 1
            while ((i < len(A)) and (j < len(A))):
                # case i even
                if (A[i] % 2 == 0):
                    i += 2
                # case j odd    
                elif (A[j] % 2 != 0):
                    j += 2    
                # case i odd and j even    
                else:
                    A[i], A[j] = A[j], A[i]
                    i += 2
                    j += 2
            return A
        
obj = Solution()
A = [4, 2, 5, 7, 9, 6]
print(obj.sortArrayByParityII(A))