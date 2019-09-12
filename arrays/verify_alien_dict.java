class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        // create an index to speed up checking position in order
        int[] order_map = new int[26];
        for (int i = 0; i < order.length(); i++) {
            order_map[order.charAt(i) - 'a'] = i;
        }
        
        search: for (int i = 0; i < words.length-1; i++) {
            String word1 = words[i];
            String word2 = words[i+1];
            
            for (int k = 0; k < Math.min(word1.length(), word2.length()); k++) {
                // if the char are different
                if (word1.charAt(k) != word2.charAt(k)) {
                    if (order_map[word1.charAt(k) - 'a'] > order_map[word2.charAt(k) - 'a']) {
                        return false;
                    }
                    // if that's not the case, i.e. w1 and w2 are already in order, break out of here and go back to search
                    // this round, i is incremented and we check the next pair of word.
                    continue search;
                }
            }
            // check for case when one word is shorter than other
            if (word1.length() > word2.length()) {
                return false;
            }
        }
        return true;
    }
}