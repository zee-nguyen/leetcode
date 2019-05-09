# Given an array A of non-negative integers, return an array consisting of all the 
# even elements of A, followed by all the odd elements of A.

# You may return any answer array that satisfies this condition.
from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if (len(A) == 1):
            return A
        else:
            i = 0
            j = len(A) - 1
            while (i < j):
                if (A[i] % 2 == 0):
                    i += 1
                elif (A[j] % 2 == 0):
                    #swap
                    temp = A[j]
                    A[j] = A[i]
                    A[i] = temp
                    i += 1
                    j += 1
                else:
                    j -= 1    
            return A

# Test
obj = Solution()
A = [5, 2, 7, 6, 5, 8, 10, 1, 4, 3]
print(obj.sortArrayByParity(A))