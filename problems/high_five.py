# https://leetcode.com/problems/high-five/

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        import heapq
        # init a dict with default value for each item is a list
        d = collections.defaultdict(list)
        ans = []
        
        for idx, val in items:
            # because d is a defaultdict, d[idx] won't raise KeyError
            heapq.heappush(d[idx], val)
            
            # only keep top 5
            if len(d[idx]) > 5:
                heapq.heappop(d[idx])
            
        return [[idx, sum(d[idx]) // 5] for idx in sorted(d)]

# from typing import List
# from collections import defaultdict
# class Solution:
#     def highFive(self, items: List[List[int]]) -> List[List[int]]:
#         d = defaultdict(list)
#         for item in items:
#             d[item[0]].append(item[1])
#         res = []
#         for k, v in d.items():
#             total = 0
#             d[k] = sorted(v, reverse=True)
#             for i in range(5):
#                 total += d[k][i]
#             avg = total//5
#             res.append([k, avg])
#         return res

# g = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
# test = Solution()
# test.highFive(g)
