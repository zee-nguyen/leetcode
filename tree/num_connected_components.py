# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

'''
Main idea:

- Track unvisited nodes
- For each unvisited nodes, run dfs on that node and increment number of connected components

- Speed up the checking edges process by building an adjacency list

'''

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False for i in range(n)]
        cc = 0 
        dfs = [] # stack
        
        # adj list
        adj_list = [[] for i in range(n)]
        for start, end in edges:
            adj_list[start].append(end)
            adj_list[end].append(start)
            
        for i in range(n):
            if not visited[i]:
                dfs.append(i)
                cc += 1
        
            while dfs:
                top = dfs.pop()
                visited[top] = True

                for neighbor in adj_list[top]:
                    if not visited[neighbor]:
                        dfs.append(neighbor)
        
        return cc
            