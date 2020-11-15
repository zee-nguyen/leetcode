# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

class Solution:
    def maxDiff(self, num: int) -> int: 
        digits = [int(n) for n in str(num)]
        len_d = len(digits)
        a = [n for n in digits]
        b = [n for n in digits]
        x = -1
        y = -1
        first = False
        foundX = False
        foundY = False
        
        # find x and Y
        for i in range(len_d):
            if digits[i] < 9 and not foundX:
                x = digits[i]
                foundX = True
            if digits[i] > 1 and not foundY:
                y = digits[i]
                if i == 0:
                    first = True
                foundY = True
        
        # update all occurences
        for i, num in enumerate(a):
            if num == x:
                a[i] = 9
        
        # update all occurences
        for i, num in enumerate(b):
            if num == y:
                if first: 
                    b[i] = 1
                else:
                    b[i] = 0
        a = int(''.join(str(n) for n in a))
        b = int(''.join(str(n) for n in b))
        
        return abs(a-b)
