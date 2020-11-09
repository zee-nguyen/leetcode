# https://leetcode.com/problems/two-sum-less-than-k/
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        max_so_far = -1
        i, j = 0, len(A)-1
        
        while i < j:
            if A[i] + A[j] >= K: #too big
                j -= 1
            else:
                max_so_far = max(max_so_far, A[i] + A[j])
                i += 1
        return max_so_far
