# https://leetcode.com/problems/word-ladder/

from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def is_convertable(s, t):
            ''' Returns true if s can be transformed into t by changing one character '''
            diff = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1
            
        if beginWord not in wordList or not beginWord or not wordList:
            return 0
        
        graph = {wordList[i]:[] for i in range(len(wordList))}
        graph[beginWord] = []
        
        for i in range(len(wordList)):
            if is_convertable(wordList[i], beginWord):
                graph[beginWord].append(wordList[i])
                graph[wordList[i]].append(beginWord)
                
            for j in range(i+1, len(wordList)):

                if is_convertable(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
                    
        q = deque([(beginWord, 1)])
        visited = {beginWord: True}
        
        while q:        
            front, pos = q.popleft()
            
            if front == endWord:
                return pos

            for neighbor in graph[front]:
                if neighbor not in visited:
                    q.append((neighbor, pos+1))
                    visited[neighbor] = True
                    
        return 0 # no sequence found