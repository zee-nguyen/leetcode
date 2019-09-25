// https://leetcode.com/problems/valid-anagram/

class IsAnagram {
    public boolean isAnagram(String s, String t) {
        // if (s == null || s == "" || t == null || t == "") {
        //     return false;
        // }

        // If they're anagram, must have the same length
        if (s.length() != t.length()) {
            return false;
        }
        
        int[] count = new int[26];
        
        // get count of all characters in s
        // for (int i = 0; i < s.length(); i++) {
        //     count[s.charAt(i) - 'a']++;
        // }
        
        // for (int j = 0; j < t.length(); j++) {
        //     if (count[t.charAt(j) - 'a'] <= 0) {
        //         return false; // this char is not in s
        //     }
        // }
        
        // now we know all char in t must be in s
        // decrement count
        // for (int j = 0; j < t.length(); j++) {
        //     count[t.charAt(j) - 'a']--;
        // }

        // INSTEAD OF ALL THE LOOPS ABOVE
        // For each char in s, increment
        // for each char in t, decrement
        // in the end the array should only contain 0

        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }
        
        for (int k = 0; k < count.length; k++) {
            if (count[k] != 0) {
                return false;
            }
        }
        
        return true;
    }
}