// https://leetcode.com/problems/reverse-linked-list/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return null;
        }
        // iterative 
        ListNode prev = null;
        ListNode next = null;
        ListNode cur = head;
        
        while (cur != null) {
            // update next to be the next element before flipping link direction
            next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        // prev now is the head of reversed list
        return prev;
    }
}
