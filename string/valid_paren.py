# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                # pop from empty stack
                if not stack:
                    return False
                # check for matching pair
                if c == ")":
                    if stack.pop() != "(":
                        return False
                elif c == "}":
                    if stack.pop() != "{":
                        return False
                else:
                    if stack.pop() != "[":
                        return False
                        
        # True only if stack is empty
        return len(stack) == 0
