# https://leetcode.com/problems/find-anagram-mappings/
class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        d = {a: i for i, a in enumerate(B)}
        return [d[val] for val in A]
