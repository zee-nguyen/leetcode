# https://leetcode.com/problems/intersection-of-three-sorted-arrays/

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        counter = collections.Counter(arr1)
        
        for el in arr2:
            if el in counter:
                counter[el] += 1
        for el in arr3:
            if el in counter:
                counter[el] += 1
        
        return [k for k in counter.keys() if counter[k] >= 3]

        # Sol 2:
        # return [k for k, v in collections.Counter(arr1+arr2+arr3).items() if v == 3]
