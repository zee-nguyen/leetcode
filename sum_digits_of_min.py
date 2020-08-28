# https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/
# Given an array A of positive integers, let S be the sum of the digits of the minimal element of A.
# Return 0 if S is odd, otherwise return 1.

from typing import List

class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        smallest = min(A)
        sumDigits = 0

        while(smallest):
            sumDigits += smallest % 10
            smallest //= 10
        return 0 if sumDigits % 2 != 0 else 1

# A = [34,23,1,24,75,33,54,8]
A = [99,77,33,66,55]
test = Solution()
print(test.sumOfDigits(A))