# Given a 2d grid map of '1's (land) and '0's (water), count the number of 
# islands. An island is surrounded by water and is formed by connecting adjacent 
# lands horizontally or vertically. You may assume all four edges of the grid 
# are all surrounded by water.

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def isSafe(grid, visited, r, c):
            '''
            Determine whether a given ceil is safe to include in dfs.
            A ceil is safe when it is within bound, a '1', and not visited.
            '''
            return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0]) and \
                grid[r][c] and not visited[r][c]

        def dfs(visited, r, c):
            '''
            Recursive DFS procedure.
            '''
            visited[r][c] = True
            neighborRow = [-1, -1, -1, 0, 0, 1, 1, 1]
            neighborCol = [-1, 0, 1, -1, 1, -1, 0, 1]

            for k in range(8):
                if isSafe(grid, visited, r+neighborRow[k], c+neighborCol[k]):
                    dfs(visited, r+neighborRow[k], c+neighborCol[k])

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0
        # track visited nodes
        visited = [[False for i in range(cols)] for j in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if not visited[r][c] and grid[r][c]:
                    dfs(visited, r, c)
                    count += 1
        
        return count


test = Solution()
# grid = [[1,1,1,1,0], [1,1,0,1,0], [1,1,0,0,0], [0,0,0,0,0]]
grid = [[1, 1, 0, 0, 0], 
        [0, 1, 0, 0, 1], 
        [1, 0, 0, 1, 1], 
        [0, 0, 0, 0, 0], 
        [1, 0, 1, 0, 1]]
print(test.numIslands(grid))