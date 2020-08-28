# https://leetcode.com/problems/friend-circles/

""" 
Intuition:

- Same idea as number of connected components
- The relationship is represented as adjacency matrix

RT: O(n^2) since we need to check each student (row), for each student we need to check other student (col)
Space: O(n) for list of visited

"""

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        ans = 0
        
        dfs = []
        visited = [False for i in range(len(M))]
        
        # for each student, if not visited, run friend circle
        for i in range(len(M)):
            if not visited[i]:
                dfs.append(i)
                ans += 1
            
            while dfs:
                top = dfs.pop()
                visited[top] = True
                
                for j in range(len(M)):
                    if not visited[j] and M[top][j] == 1:
                        dfs.append(j)
                        
        return ans