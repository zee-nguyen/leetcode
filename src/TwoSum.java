/**
 * Given an array of integers, return indices of the two numbers such that they 
 * add up to a specific target. You may assume that each input would have 
 * exactly one solution, and you may not use the same element twice.
 */

public class TwoSum {
  public int[] twoSum(int[] nums, int target) {
    int[] result = new int[2];
    for (int i = 0; i < nums.length; i++) {
      for (int j = 1; j < nums.length; j++) {
        if ((i != j) && (nums[i] + nums[j] == target)) {
          result[0] = i;
          result[1] = j;
          return result;
        }
      }
    }
    return result;
  }

//  public static void main(String[] args) {
//    int[] arr = {3, 3};
//    int[] result = twoSum(arr, 6);
//    for (int i = 0; i < result.length; i++) {
//      System.out.println(result[i]);
//    }
//  }
}