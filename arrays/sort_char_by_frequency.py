
# https://leetcode.com/problems/sort-characters-by-frequency/

from collections import Counter
import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return s
        
        # convert string to list of char and get their counts
        chars = list(s)
        count = Counter(chars)
        
        # make a heap out of it
        # since we'll want to use max heap, use -v
        heap = [(-v, k) for (k, v) in count.items()]
        
        heapq.heapify(heap)
        ret = []
        
        while heap:
            top = heapq.heappop(heap)
            ret.append(top[1] * -top[0]) #append however many times
        
        return "".join(ret)
        