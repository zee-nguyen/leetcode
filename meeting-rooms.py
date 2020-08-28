# https://leetcode.com/problems/meeting-rooms/
from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        ans = True
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if intervals[i][0] <= intervals[j][0] < intervals[i][1]:
                    ans = False
        return ans

test = Solution()
time = [[7,10],[2,4]]
# time = [[0,30],[5,10],[15,20]]
print(test.canAttendMeetings(time))
