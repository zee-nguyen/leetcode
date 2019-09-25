// https://leetcode.com/problems/valid-anagram/

class IsAnagram {
    public boolean isAnagram(String s, String t) {
        if (s == null || s == "" || t == null || t == "") {
            return false;
        }
        
        // build a count of all char in s
        Map<Character, Integer> count = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            count.put(s.charAt(i), count.getOrDefault(s.charAt(i), 0) + 1);
        }
        for (int j = 0; j < t.length(); j++) {
            // if char isn't in map or it is in map but count is 0 -> false
            if (!count.containsKey(t.charAt(j)) || count.get(t.charAt(j)) == 0) {
                return false;
            }
            
            // else, decrement count
            count.put(t.charAt(j), count.get(t.charAt(j)) - 1);
        }
        
        for (Map.Entry<Character, Integer> entry : count.entrySet()) {
            if (entry.getValue() > 0) {
                return false;
            }
        }
        
        return true;
    }
}