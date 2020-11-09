# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        Transpose then reverse
        """
        n = len(matrix)
        
        def transpose(matrix, n):
            for i in range(n):
                for j in range(i, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        transpose(matrix, n)
        
        for r in range(n):
            matrix[r] = matrix[r][::-1]
