# Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

from typing import List

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i, list in enumerate(A):
            # flip horizontally
            for i, item in enumerate(list):
                j = len(list) - i - 1
                if (i >= j):
                    break
                temp = list[i]
                list[i] = list[j]
                list[j] = temp       
            # replace 0 by 1 and 1 by 0
            for i, item in enumerate(list):
                if (list[i] == 1):
                    list[i] = 0
                else:
                    list[i] = 1
        return A
            


# Test
obj = Solution()
A = [[1,1,0],[1,0,1],[0,0,0]]
# [[1,0,0],[0,1,0],[1,1,1]]
# obj.flipAndInvertImage(A)

B = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

obj.flipAndInvertImage(B)