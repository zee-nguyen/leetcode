# https://leetcode.com/problems/k-closest-points-to-origin/

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        max_heap = []
        
        for (x,y) in points:
            # python only has min heap, so we insert negtaive of distance to sort in reversed distance order
            # replicate max heap
            
            dist = -(x*x + y*y)
            heapq.heappush(max_heap, (dist, x,y))

            # when heap length exceeds K, pop the min element (i.e. max distance)
            if len(max_heap) == K+1:
                heapq.heappop(max_heap)
            
        return [(x,y) for (dist, x,y) in max_heap]