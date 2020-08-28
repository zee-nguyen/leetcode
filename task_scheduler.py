# https://leetcode.com/problems/task-scheduler/

from collections import Counter
import heapq

'''
Intuition:
- We want to schedule the most frequent task as early as possible. That way, we have more chance of not being idled later
- To keep track of most frequent tasks, we need a max heap
- Need to also track # of cycles

Process:
- Get count of tasks and put all of them into a heap
- Keep going while we have stuff on the heap to process:
    - Within the cooling interval, process what we have on the heap if the heap is not empty
    - Also keep track of what stuff are being processed currently
    - When we're done with the cooling interval:
        - Check the list of stuff we just process, if they still need to be processed, put them back into the heap, with count - 1
    - Increment the number of cycles
        - If the heap is empty, that means we've processed everything --> no need to idle, cycle += len of the list of tasks just processed
        - If there are still item in the heap, that means we just processed all tasks + 1 idle --> cycle += n+1 (n tasks + 1 idle)
- return cycle
'''

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap, cycle = [], 0
        
        count = Counter(tasks)
        # python only has min heap so we insert negative value to make it a max heap
        for v in count.values():
            heapq.heappush(heap, -v)
        
        while heap:
            # track the processes we're current processing
            cur_process = []
            
            for i in range(n+1):
                # if there are stuff on the heap, pop and add to list of things we've processed
                if heap:
                    cur_process.append(heapq.heappop(heap))
            
            # check if any item still needs to be process
            # since the count in the heap are negative, we need to use abs(c) - 1 to check if the item still needs to be processed
            # if it is, push back to the heap with count + 1 (for it to come close to 0)
            for c in cur_process:
                if abs(c) - 1 > 0:
                    heapq.heappush(heap, c + 1)
            
            # if there are things to process in the heap, we just did all possible processes + 1 idle
            # else, no need to ilde at the end
            if heap:
                cycle += (n + 1)
            else:
                cycle += len(cur_process)
            
        return cycle