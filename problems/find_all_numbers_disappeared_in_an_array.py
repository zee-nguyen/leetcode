# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

from collections import Counter

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # result = [i for i in range(1, len(nums)+1)]
        # for num in nums:
        #     if num in result:
        #         result.remove(num)
        # return result
        # dct = Counter(nums)
        # result = []
        # for i in range(1, len(nums)+1):
        #     if i not in dct:
        #         result.append(i)
        # return result

        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

