# https://leetcode.com/problems/toeplitz-matrix/
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
# Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        numRow = len(matrix)
        numCol = len(matrix[0])
        for i in range(numRow):
          for j in range(numCol):
            if (i + 1 < numRow and j + 1 < numCol):
              if (matrix[i][j] != matrix[i+1][j+1]):
                return False
            else:
              continue
        return True

matrix = [
  [1,2],
  [2,2]
]
# matrix = [
#   [1,2,3,4],
#   [5,1,2,3],
#   [9,5,1,2]
# ]
test = Solution()
print(test.isToeplitzMatrix(matrix))