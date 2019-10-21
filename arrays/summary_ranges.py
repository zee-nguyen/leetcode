# https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        i, res = 0, []
        
        while i < len(nums):
            cur_range = str(nums[i])
            j = i + 1
            
            while j < len(nums):
                if nums[j] - nums[i] == j - i:
                    # if j is at the end, append A[j]
                    if j == len(nums) - 1:
                        cur_range += "->" + str(nums[j])
                    j += 1
                else:
                    # not consecutive, check if we've moved then append last number
                    if i != j - 1:
                        cur_range += "->" + str(nums[j-1])
                    break
            
            res.append(cur_range)
            i = j
        return res