// https://leetcode.com/problems/product-of-array-except-self/

/**
Observations:
1/ With division, it's easy... Compute the product of the whole array, then loop through the array,
dividing product/ nums[i].
*/

class Solution {
    public int[] productExceptSelf(int[] nums) {
        // With division, it's easy...
        int prod = 1;
        int[] res = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            prod *= nums[i];
        }
        for (int i = 0; i < nums.length; i++) {
            res[i] = prod/nums[i];
        } 
        return res;
    }
}