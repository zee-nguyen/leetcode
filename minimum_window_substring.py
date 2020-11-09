# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # to find the min window, we need to know what char are in t
        table = collections.Counter(t)
        # counter to track when a window is valid
        counter = len(table)
        
        # begin and end mark of the window
        begin = end = 0
        min_len = float("inf") # min len of window
        ans = ''
        
        # shift the end pointer toward the right to find a valid window
        while end < len(s):
            end_char = s[end]
            if end_char in table: #found a char in t
                table[end_char] -= 1
                if table[end_char] == 0:
                    counter -= 1
            end += 1
            
            # we have a valid window when all the character in t are within the current window
            # i.e. counter will be 0
            while counter == 0: 
                # update ans if window is smaller than current
                if end - begin < min_len:
                    min_len = end - begin
                    ans = s[begin:end]
                
                # now, we shift the begin pointer forward to shrink the window as much as possible 
                # while remaining valid
                begin_char = s[begin]
                if begin_char in table:
                    # if the begin_char is not in t, we can skip it as it's not needed to be in the window
                    # if it is in t and we're skipping it, we need to increment the table count to 
                    # keep track of the state of current windows
                    table[begin_char] += 1
                    if table[begin_char] > 0:
                        counter += 1
                begin += 1
        
        return ans
