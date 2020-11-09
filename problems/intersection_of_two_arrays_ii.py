# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Hashmap solution

        # c1 = collections.Counter(nums1)
        # c2 = collections.Counter(nums2)
        # ans = []
        # for k, v in c1.items():
        #     if k in c2:
        #         for i in range(min(v, c2[k])):
        #             ans.append(k)
        # return ans

        # 2 pointers
        nums1.sort()
        nums2.sort()
        
        i = j = 0
        ans = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else: # same
                ans.append(nums1[i])
                i += 1
                j += 1

        return ans
