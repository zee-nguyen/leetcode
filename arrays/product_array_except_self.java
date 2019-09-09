// https://leetcode.com/problems/product-of-array-except-self/

/**
Observations:
1/ With division, it's easy... Compute the product of the whole array, then loop through the array,
dividing product/ nums[i].

2/ Brute force: O(n^2)
Iterate over the array n times, each time compute the product of other numbers except current index's value.
Compute left product and right product then multiple them together.
*/

class Solution {
    public int[] productExceptSelf(int[] nums) {
        // n^2 solution... improved to handle duplicates
        int[] res = new int[nums.length];
        Map<Integer, Integer> mp = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            if (mp.containsKey(nums[i])) {
                res[i] = mp.get(nums[i]);
            }
            
            int prod = 1;
            
            // left to right
            for (int j = 0; j < i; j++) {
                prod *= nums[j];
            }
            
            // right to left
            for (int k = nums.length-1; k > i; k--) {
                prod *= nums[k];
            }
            mp.put(nums[i], prod);
            res[i] = prod;
        }
        return res;
    }
}