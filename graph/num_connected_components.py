# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

'''
Main idea:

- Track unvisited nodes
- For each unvisited nodes, run dfs on that node and increment number of connected components

- Speed up the checking edges process by building an adjacency list

'''

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        ans = 0
        
        adj_list = {i: [] for i in range(n)}
        for start, end in edges:
            adj_list[start].append(end)
            adj_list[end].append(start)
            
        for i in range(n):
            if visited[i]:
                continue
            
            ans += 1
            dfs = [i]
            visited[i] = True
            
            while dfs:
                node = dfs.pop()
                for neighbor in adj_list[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        dfs.append(neighbor)
                        
        return ans
            