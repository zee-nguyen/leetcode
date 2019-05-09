# https://leetcode.com/problems/transpose-matrix/
# Given a matrix A, return the transpose of A.
# The transpose of a matrix is the matrix flipped over it's main diagonal, 
# switching the row and column indices of the matrix.

from typing import List

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        numRow = len(A[0]) # number of rows 
        result = [[] for i in range(numRow)]

        for i in range(numRow):
            for j in range(len(A)):
                result[i].append(A[j][i])
        
        return result
        
        # i = 0
        # result = []
        # numRow = len(A[0])
        # while (i < numRow):
        #     mat = []
        #     for lst in A:
        #         mat.append(lst[i])
        #     result.append(mat)
        #     i += 1
        # return result

test = Solution()
# A = [[1,2,3],[4,5,6]]
A = [[1,2,3],[4,5,6],[7,8,9]]
print(test.transpose(A))