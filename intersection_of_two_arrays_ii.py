# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        ans = []
        for k, v in c1.items():
            if k in c2:
                for i in range(min(v, c2[k])):
                    ans.append(k)
        return ans
