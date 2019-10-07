# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        ans = 0
        left_to_right = [-1 for _ in height]
        right_to_left = [-1 for _ in height]
        
        left_h = right_h = -1
        
        for i, h in enumerate(height):
            left_h = max(h, left_h)
            left_to_right[i] = left_h
        
        for j in range(len(height)-1, -1,-1):
            right_h = max(right_h, height[j])
            right_to_left[j] = right_h
            
        for i, h in enumerate(height):
            ans += min(left_to_right[i], right_to_left[i]) - h
            
        return ans
        
            