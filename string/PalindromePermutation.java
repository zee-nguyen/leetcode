// https://leetcode.com/problems/palindrome-permutation/

// A palindrome must have pairs of characters, with an exception that one letter might have just 1 occurance (in the middle)
// Put all chars into a hashtable and check for their counts
// If more than 1 characters have an odd count -> false

class Solution {
    public boolean canPermutePalindrome(String s) {
        if (s.length() == 0 || s.length() == 1) {
            return true;
        }
        
        Map<Character, Integer> count = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            count.put(s.charAt(i), count.getOrDefault(s.charAt(i), 0) + 1);
        }
        int odd = 0;
        for (Map.Entry<Character, Integer> entry: count.entrySet()) {
            if (entry.getValue() % 2 != 0) {
                odd++;
            }
        }
        return odd <= 1;
    }
}