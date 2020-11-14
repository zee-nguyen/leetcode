# https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        steps = 0
        for log in logs:
            if log == './': # stay the same
                continue
            elif log == '../': # backup 1
                steps -= 1 if steps != 0 else 0
            else: # move to another folder
                steps += 1
        return steps
                