
/**
 * Given a 32-bit signed integer, reverse digits of an integer.
 * Assume we are dealing with an environment which could only store integers within the 32-bit
 * signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your
 * function returns 0 when the reversed integer overflows.
 */

public class ReverseInteger {

  public static int reverse(int x) {
    String input = Integer.toString(x);
    String reversed;

    if (input.length() == 1) {
      return x;
    }

    if (x < 0) {
      reversed = "-";
      for (int i = input.length()-1; i > 0; i--) {
        reversed += input.charAt(i);
      }
    } else {
      reversed = "";
      for (int i = input.length()-1; i >= 0; i--) {
        reversed += input.charAt(i);
      }
    }

    int result = 0;
    try {
      result = Integer.parseInt(reversed);
    } catch (NumberFormatException e) {
      return result;
    }
    return result;
  }

  public static void main(String[] args) {
//    System.out.println(reverse(-2147483648));
    System.out.println(reverse(-123));
    System.out.println(reverse(123));
    System.out.println(reverse(0));
    System.out.println(reverse(1));
    System.out.println(reverse(-2147483648));
  }




}
