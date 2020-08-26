# https://leetcode.com/problems/reorder-data-in-log-files/

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digs = []
        lets = []
        for log in logs:
            arr = log.split(" ")
            if arr[1].isdigit(): #digit logs in original order
                digs.append(log)
            else:
                lets.append(log)
        # for letter-logs, sort by everything after identifier. If tie, sort by identifier
        lets.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return lets + digs
