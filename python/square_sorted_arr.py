# Given an array of integers A sorted in non-decreasing order, return an array of 
# the squares of each number, also in sorted non-decreasing order.
# Example:
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # return [x*x for x in A]
        return sorted(x*x for x in A)
        # sq = []
        # for num in A:
        #     sq.append(num * num)
        # sq.sort()
        # print(sq)
    
    
# Test
obj = Solution()
print(obj.sortedSquares([-4,-1,0,3,10]))

# First off, when the problem is short, write your own sort function
# However, in interview, unless the problem is a sorting problem, like they ask you
# to implement bubble sort/ quicksort, you can use the built-in sort function like above.
# Second, python and other languages support a thing called compare function for sort.
# Read more: https://docs.python.org/3.3/howto/sorting.html
# For example:
# >>> def numeric_compare(x, y):
#         return x - y
# >>> sorted([5, 2, 4, 1, 3], cmp=numeric_compare)
# [1, 2, 3, 4, 5]
# For this problem, we can just write a compare function that compare elements by their abs value, right?
