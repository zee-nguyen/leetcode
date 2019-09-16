// https://leetcode.com/problems/valid-palindrome-ii/

// If we can remove just one letter and the string is valid palindrome, then, looking at index i and j
// if they are different, s[i:j] has to be a palindrome or s[i+1:j+1] has to be a palindrome.

class Solution {
    public boolean isPalindrome(String s) {
        int i = 0;
        int j = s.length() - 1;
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
    
    public boolean validPalindrome(String s) {
        int i = 0;
        int j = s.length()-1;
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) {
                return this.isPalindrome(s.substring(i, j)) || this.isPalindrome(s.substring(i+1, j+1));
            }
            i++;
            j--;
        }
        return true;
    }
}