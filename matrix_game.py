#!/bin/python3

import math
import os
import random
import re
import sys



import heapq 

#
# Complete the 'play' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def play(arr):
    if not arr or not arr[0]:
        return 0

    tom_score = 0
    jerry_score = 0

    tom_turn = True
    jerry_turn = False 

    # gameover = False
    inactive = {}

    heap = []

    # build the heap
    rows = len(arr)
    cols = len(arr[0])

    for r in range(rows):
        for c in range(cols):
            heapq.heapqpush(heap, (arr[r][c], (r, c) )

    while (len(heap) != 0):
        if tom_turn:
            val, r, c = heapq.heappop(heap)
            if c not in inactive:
                tom_score += val 
                inactive[c] = True

            tom_turn = False
            jerry_turn = True
        
        if jerry_turn:
            val, r, c = heapq.heappop(heap)
            if c not in inactive:
                jerry_score += val 
                inactive[c] = True

            jerry_turn = False 
            tom_turn = True

    return tom_score - jerry_score


if __name__ == '__main__':