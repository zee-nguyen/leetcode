# https://www.geeksforgeeks.org/count-number-of-ways-to-cover-a-distance/
# Count number of ways to cover a distance
# Given a distance ‘dist, count total number of ways to cover the distance with 1, 2 and 3 steps.

class Solution:
    def count_total_ways(self, n):
        c = [0 for i in range(n+1)]
        c[0] = 1
        c[1] = 1
        c[2] = 2
        for i in range(n+1):
            if (i > 2):
                c[i] = c[i-1] + c[i-2] + c[i-3]
        return c[n]

test = Solution()
print(test.count_total_ways(4))