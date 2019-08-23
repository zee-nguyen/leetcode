// https://leetcode.com/problems/palindrome-linked-list/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null) {
            return true;
        }
        
        // O(n) space solution
        List<Integer> arr = new ArrayList<>();
        ListNode cur = head;
        while (cur != null) {
            arr.add(cur.val);
            cur = cur.next;
        }
        for(int i = 0; i < arr.size(); i++) {
            if (!arr.get(i).equals(arr.get(arr.size()-i-1))) {
                return false;    
            }
        }
        return true;
    }
}
