# https://leetcode.com/problems/reorganize-string/

class Solution:
    def reorganizeString(self, S: str) -> str:
        '''
        Intuition: Always try to use the char with most count if possible. 
        - Use a max heap to keep track of order
        '''
        if not S or len(S) == 1:
            return S

        dct = collections.Counter(S)
        h = []
        ans = []
        cur = ''
        
        # load all letters to heap
        for k, v in dct.items():
            heapq.heappush(h, (-v, k))
        
        while h:
            nxt_count, nxt = heapq.heappop(h)
            # if no item is left and count > 1 -- not possible
            if len(h) == 0 and abs(nxt_count) > 1: 
                return ''
            
            if nxt == cur: #can't reuse the same as current letter
                tmp_count, tmp = nxt_count, nxt
                nxt_count, nxt = heapq.heappop(h) #get next letter
                heapq.heappush(h, (tmp_count, tmp))
            
            ans.append(nxt)
            cur = nxt
            if abs(nxt_count) > 1: #only put back to heap if count != 0
                heapq.heappush(h, (nxt_count + 1, nxt))
        return ''.join(ans)
        