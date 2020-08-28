# https://leetcode.com/problems/happy-number/

# Observation:
# What is the condition to terminate the program, besides checking when n == 1?
# If a number appear more than once, it'll keep looping. What does this mean? 
# For example, after one or two loops, we see 81. Then the code keeps running and if we see 81 again (code hasn't terminated), it'll be in an infinite loop. Results from 81 onward will be repeated.
# So to check for that, have a set and check if value is already in set. If not, add to set. If it's already in the set, break out of the loop and return whether n == 1

class Solution:
    def isHappy(self, n: int) -> bool:
        mem = set()
        while n not in mem:
            mem.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        return n == 1
        