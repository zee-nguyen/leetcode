// https://leetcode.com/problems/reverse-linked-list-ii/

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
 
/* 
High-level:
- Use i to find the right starting place of the reverse
- Move i to right before the start
- start reversing when i <= C
- prev always has the head of the reversed LL
- edge cases: list is null, when we reverse from the front of the list...

- Runtime: O(N) where N is the number of nodes in the LL. 
    (Worst case we need to look at every item once)
- Space: O(1) since we just need a couple pointers.

*/

public class Solution {
    public ListNode reverseBetween(ListNode A, int B, int C) {
        if (A == null) {
            return A;
        }
        
        ListNode prev = null, next = null, cur = A;
        int i = 1;
        // move i to the starting point, i.e. B
        while (i < B && cur != null) {
            next = cur.next;
            prev = cur;
            cur = next;
            i++;
        }
        
        ListNode tmp = prev;
        
        // reverse
        while (i <= C && cur != null) {
            next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
            i++;
        }
        
        // tmp == null, we were at the front of the list
        if (tmp == null) {
            ListNode tmp_head = A;
            A.next = cur;
            A = prev;
        } else {
            tmp.next.next = cur;
            tmp.next = prev;
        }
        
        return A;
    }
}
