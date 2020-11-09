# https://leetcode.com/problems/intersection-of-two-arrays/
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        
        s1 = set(nums1)
        ans = []
        for num in nums2:
            if num in s1:
                ans.append(num)
                s1.remove(num)
        return ans
