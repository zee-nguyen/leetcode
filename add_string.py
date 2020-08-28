# https://leetcode.com/problems/add-strings/

class AddString:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(num1)
        num2 = list(num2)
        
        res, carry = "", 0
        
        while num1 or num2:
            n1, n2 = 0, 0
            n1 = ord(num1.pop()) - ord("0") if num1 else 0
            n2 = ord(num2.pop()) - ord("0") if num2 else 0
            total = n1 + n2 + carry
            carry = total // 10
            res = str(total % 10) + res
        if carry:
            res = str(carry) + res
        return res