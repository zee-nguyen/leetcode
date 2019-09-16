// https://leetcode.com/problems/product-of-array-except-self/

/**
Observations:
1/ With division, it's easy... Compute the product of the whole array, then loop through the array,
dividing product/ nums[i].

2/ Brute force: O(n^2)
Iterate over the array n times, each time compute the product of other numbers except current index's value.
Compute left product and right product then multiple them together.

3/ Take the given input for example: [1,2,3,4]
What we want: [a2a3a4, a1a3a4, a1a2a4, a1a2a3]

We can use multiplying two arrays...
*/

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] left = new int[n];
        int[] right = new int[n];
        int[] res = new int[n];
        // set up
        left[0] = 1;
        left[1] = nums[0];
        right[n-1] = 1;
        right[n-2] = nums[n-1];
        
        int k = 2;
        int j = n-3;
        while (k < n) {
            left[k] = left[k-1] * nums[k-1];
            k++;
        }
        while (j >= 0) {
            right[j] = right[j+1] * nums[j+1];
            j--;
        }
        
        for (int i = 0; i < n; i++) {
            res[i] = left[i] * right[i];
        }
        return res;
        
    }
}