/**
 * Given an array nums and a value val, remove all instances of that value in-place and
 * return the new length.
 *
 * Do not allocate extra space for another array, you must do this by modifying the input array
 * in-place with O(1) extra memory.
 *
 * The order of elements can be changed. It doesn't matter what you leave beyond the new length.
 */
public class RemoveElement {
  public static int removeElement(int[] nums, int val) {
    // case len = 0
    if (nums.length == 0) {
      return 0;
    }

    if (nums.length == 1) {
      if (nums[0] == val) {
        return 0;
      } else {
        return 1;
      }
    }


    int i = 0;
    int j = nums.length - 1;

    while (i < j) {
      // if i and j are both what we're looking for, move j one to the left
      if (nums[i] == val) {
        if (nums[j] == val) {
          j--;
        } else { // j is not val
          // swap
          nums[i] = nums[j]; //check
          i++;
          j--;
        }
      } else { // nums[i] != val
        i++;
      }
    } // end while

    // at this point, i = j, check one more time
    if (nums[j] == val) {
      j--;
    }

    return j + 1;
  }

  public static void main(String[] args) {
    int[] nums = {3, 2, 2, 3};
    int[] mul = {0, 1, 2, 2, 3, 0, 4, 2};
    int[] empty = {};
    int[] one = {1};

    System.out.println(removeElement(nums, 3)); // 2
    System.out.println(removeElement(empty, 3)); // 0
    System.out.println(removeElement(one, 3)); // 1
    System.out.println(removeElement(one, 1)); // 0
    System.out.println(removeElement(mul, 2)); // 5
  }
}
