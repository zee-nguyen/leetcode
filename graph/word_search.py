# https://leetcode.com/problems/word-search/
# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, 
# where "adjacent" cells are those horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        