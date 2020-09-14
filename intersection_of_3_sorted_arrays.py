# https://leetcode.com/problems/intersection-of-three-sorted-arrays/

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        c = collections.Counter(arr1)
        track = dict()
        res = []
        for el in arr2:
            if el in c:
                track[el] = 1
        for el in arr3:
            if el in track:
                res.append(el)
        return res

        # Sol 2:
        # return [k for k, v in collections.Counter(arr1+arr2+arr3).items() if v == 3]
