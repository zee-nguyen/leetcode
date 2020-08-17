# https://leetcode.com/problems/non-decreasing-array/

# Given an array with n integers, your task is to check if it could become
# non-decreasing by modifying at most 1 element.
# We define an array is non-decreasing if array[i] <= array[i + 1] 
# holds for every i (1 <= i < n). The n belongs to [1, 10,000].

from typing import List

class Solution:
    def checkPossibility(self, A: List[int]) -> bool:
        # check if arr is mono increasing
        def monoIncreasing(arr):
            for i in range(len(arr)-1):
                if arr[i] > arr[i+1]:
                    return False
            return True

        new = A[:] # make a copy of nums
        for i in range(len(A)):
            new[i] = A[i-1] if i>0 else float("-inf")
            if monoIncreasing(new):
                return True
            new[i] = A[i]
        
        return False
            
        

# A = [4, 2, 3] 
A = [3, 4, 2, 3]
# A = [1,5,4,6,7,10,8,9]
# A = [1, 2, 3, 1, 3]
# A = [2,3,3,2,4] - T
test = Solution()
print(test.checkPossibility(A))