# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        c = dict(collections.Counter(nums))
        sorted_keys = sorted(c)
        msf = sorted_keys[0]
        dct = {msf:0}
        for k in sorted_keys:
            if k > msf:
                dct[k] = c[msf] + dct[msf]
                msf = k
        return [dct[i] for i in nums]