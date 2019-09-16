// https://leetcode.com/problems/add-binary/

// In Java, "" is for string. '' is for char.

class AddBinary {
    public String addBinary(String a, String b) {
        int carry = 0;
        String res = "";
        
        int i = a.length() - 1;
        int j = b.length() - 1;
        
        while (i >= 0 || j >= 0 || carry == 1) {
            carry += (i >= 0) ? Character.getNumericValue(a.charAt(i)) : 0;
            carry += (j >= 0) ? Character.getNumericValue(b.charAt(j)) : 0;
            
            res = (char)(carry % 2 + '0') + res;
            carry /= 2;
            
            i--;
            j--;
        }
        
        return res;
    }
}