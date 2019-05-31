# https://leetcode.com/problems/monotonic-array/
# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  
# An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
# Return true if and only if the given array A is monotonic.

from typing import List

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        n = len(A)
        if n == 1 or n == 2:
            return True 
        return (all(A[i] >= A[i+1] for i in range(n-1)) or \
            all(A[i] <= A[i+1] for i in range(n-1)))
        # return all(i >= i+1 for i in A) or all(i <= i+1 for i in A) --> why doesn't this work?

A = [1,2,2,3]
# A = [6, 5, 4, 4]
# A = [1, 3, 2]
# A = [3, 3, 2, 1, 1, 1, -1, -1, 2, 3, 4, 4]
# A = [3,2,1,-1,2,3]
# A = [5, 3, 2, 4, 1]
test = Solution()
print(test.isMonotonic(A))
