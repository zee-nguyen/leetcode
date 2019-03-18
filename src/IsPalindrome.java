/**
 * Determine whether an integer is a palindrome. An integer is a palindrome when it
 * reads the same backward as forward.
 */
public class IsPalindrome {
  public static boolean isPalindrome(int x) {
    String input = Integer.toString(x);
    String[] splitted = input.split("");

    for (int i = 0; i < splitted.length; i++) {
      if (!splitted[i].equals(splitted[splitted.length-1-i])) {
        return false;
      }
    }
    return true;
  }

  public static void main(String[] args) {
    System.out.println(isPalindrome(121)); // true
    System.out.println(isPalindrome(-121)); // false
    System.out.println(isPalindrome(10)); // true
    System.out.println(isPalindrome(100001)); // true
  }
}
