# https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def str_to_digit(num):
            ''' turn a string into digit '''
            arr = list(num)
            power = 0
            ret = 0
            for i in reversed(range(len(arr))):
                ret += 10**power * (ord(arr[i]) - ord("0"))
                power += 1
            
            return ret
        
        total = str_to_digit(num1) + str_to_digit(num2)
        return str(total)