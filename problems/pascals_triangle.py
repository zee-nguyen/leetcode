# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1 for j in range(i+1)] for i in range(numRows)]
        for i in range(2, numRows):
            prev = ans[i-1] #prev row
            j = 1
            while j < len(ans[i])-1:
                ans[i][j] = prev[j-1] + prev[j]
                j += 1
        return ans
        