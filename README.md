# My LeetCode Journey


> You are learning. You are growing.
> Good things take time so be patient and learn every day. 


## Tips to consider 
Ref: [https://github.com/SeanPrashad/leetcode-patterns](https://github.com/SeanPrashad/leetcode-patterns)

```
If input array is sorted then
    - Binary search
    - Two pointers

If asked for all permutations/subsets then
    - Backtracking

If given a tree then
    - DFS
    - BFS

If given a graph then
    - DFS
    - BFS

If given a linked list then
    - Two pointers

If recursion is banned then
    - Stack

If asked for maximum/minumum subarray/subset/options then
    - Dynamic programming

If asked for top/least K items then
    - Heap

If asked for common strings then
    - Map
    - Trie

Else
    - Map/Set for O(1) time & O(n) space
    - Sort input for O(nlogn) time and O(1) space

```

Also

1. Consider preprocessing the input
2. Travel to mid of linked list using slow and fast pointers
```
    slow = fast = head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

\\ when the loop breaks, slow is at the middle of the linked list
\\ If the length is even, it'll be the rightmost item
```
