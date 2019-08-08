# https://leetcode.com/problems/unique-paths/

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. 
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?
# Note: m and n will be at most 100.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        C = [[0 for row in range(m)] for col in range(n)]
        for r in range(n):
            for c in range(m):
                if r == c == 0:
                    C[r][c] = 1
                elif r-1 < 0:
                    C[r][c] = C[r][c-1]
                elif c-1 < 0:
                    C[r][c] = C[r-1][c]
                else:
                    C[r][c] = C[r-1][c] + C[r][c-1]
                
        return C[n-1][m-1]

test = Solution()
m = 7
n = 3
print(test.uniquePaths(m, n))