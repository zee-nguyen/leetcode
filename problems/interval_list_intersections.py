# https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = []

        while i < len(A) and j < len(B):
            a1, a2 = A[i]
            b1, b2 = B[j]

            lo = max(a1, b1)
            hi = min(a2, b2)

            if lo <= hi: #intersect
                res.append([lo, hi])
            
            # move on from the interval with smallest end time
            if a2 < b2:
                i += 1
            else:
                j += 1
        return res
