# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        while num:
            if (num & 1) == 0: # even
                num >>= 1
            else:
                num -= 1
            count += 1
        return count
                