# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use min heap
        # all the code below can be written as: return heapq.nlargest(k, nums)[-1]
        
        heap = []
        
        for num in nums:
            if len(heap) == k:
                smallest = heapq.heappop(heap)
                if num < smallest:
                    heapq.heappush(heap, smallest)
                else:
                    heapq.heappush(heap, num)
            else:
                heapq.heappush(heap, num)
        
        return heapq.heappop(heap)