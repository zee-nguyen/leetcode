# https://leetcode.com/problems/remove-vowels-from-a-string/
class Solution:
    def removeVowels(self, S: str) -> str:
        sol = ""
        vowels = ["a", "e", "i", "o", "u"]
        for c in S:
            if c not in vowels:
                sol += c
        return sol
