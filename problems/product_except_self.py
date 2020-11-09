class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1 for i in nums]
        right = [1 for i in nums]
        ret = [1 for i in nums]
        
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        
        for j in range(len(nums)-2, -1, -1):
            right[j] = right[j+1] * nums[j+1]
        
        for k in range(len(nums)):
            ret[k] = left[k] * right[k]
            
        return ret