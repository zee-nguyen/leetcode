# https://leetcode.com/problems/find-the-town-judge/
# In a town, there are N people labelled from 1 to N.  
# There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given trust, an array of pairs trust[i] = [a, b] 
# representing that the person labelled a trusts the person labelled b.

# If the town judge exists and can be identified, 
# return the label of the town judge.  Otherwise, return -1.

from typing import List

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        outdeg = [0 for i in range(N)]
        indeg = [0 for i in range(N)]
        for i in trust:
            outdeg[i[0]-1] += 1
            indeg[i[1]-1] += 1
        judge = -1
        for j in range(len(outdeg)):
            if outdeg[j] == 0 and indeg[j] == N-1:
                judge = j+1
        return judge

test = Solution()
N = 4
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
print(test.findJudge(N, trust))
