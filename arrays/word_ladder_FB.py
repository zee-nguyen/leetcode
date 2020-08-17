""" 
Interview round 2 with FB

Giving a start word and end word and a list of words. Find path from word to end
- Each word can be differred by one char
- All words must exists in list

Ex:
start: "cat"
end: "bay"
list: ["cat", "bay", "bat", "faces", "cot", "cit"]
 """

class Solution:
    def isConvertable(self, s, t):
        if len(s) != len(t):
            return False
        
        diff = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                diff += 1
        
        return diff == 1


    def word_ladder(self, start, end, words):
        def dfs(word, path):
            if word not in visited:
                visited[word] = True
            
            if word == end:
                res.append(path)

            for neighbor in graph[word]:
                if neighbor not in visited:
                    dfs(neighbor, path + [neighbor])

        # build a graph
        graph = {words[i]: [] for i in range(len(words))}

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if self.isConvertable(words[i], words[j]): # they are neighbors
                    graph[words[i]].append(words[j])
                    graph[words[j]].append(words[i])
        
        # print(graph)
        visited = {}

        visited[start] = True
        res = []
        dfs(start, [start])

        return res


start = "cat"
end = "bay"
words = ["cat", "bay", "bat", "faces", "cot", "cit", "boy", "tat", "tay"]

obj = Solution()
print(obj.word_ladder(start, end, words))