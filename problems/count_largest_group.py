# https://leetcode.com/problems/count-largest-group/

class Solution:
    def countLargestGroup(self, n: int) -> int:
        def get_sum_digit(a):
            to = 0
            while a:
                to += (a%10)
                a //= 10
            return to
        
        groups = collections.defaultdict(list)
        max_len = count = 0
        
        for i in range(1, n+1):
            if i // 10 == 0: #one digit
                groups[i].append(i)
            else:
                groups[get_sum_digit(i)].append(i)
        
        for k, v in groups.items():
            if len(v) > max_len:
                max_len = len(v)
        for k, v in groups.items():
            if len(v) == max_len:
                count += 1

        return count        
