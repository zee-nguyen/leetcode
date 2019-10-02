// https://leetcode.com/problems/first-missing-positive/

/*
===== Insights:
- If the array (of lenght n) only contains positive and distinct numbers, then when we go from 1 to n, whichever value
is not present is the first missing positive.
-  We don't have to worry about 0 or negative, but do check for arrays containing these values alone -> return 1.
- Empty array -> also returns 1

===== O(n) time, O(n) space using Array/HashMap

- Using hashmap, we can put all values in the array into the map, then iterate from 1 to n, if a value is not in the map,
return it. Else, when we reach n and all values are in the map, the first missing positive is n + 1.

- We can also use an array to keep count.
    - What is the length of the array? It is the max value in the given input array, because all possible values will be
    less than max. So, have an count array to keep count of each value in nums.
    - Need to check if max is negative (i.e. the array only contains negative numbers) --> return 1 if max <= 0
    - Since array index starts at 0, we want to map 1 to the first position in count array (i.e. 0). 2 will be mapped to
    1 and so on.
    - When we loop through it, if a value at index i is 0, i.e. it is not present in the input array, then we return i+1
    (since the actual value was mapped to the index before it).
    - If we reach the end of the array and no value is missing, then the first missing positive is max + 1.

 */



class FirstMissingPositive {
    public int firstMissingPositive(int[] nums) {
        if (nums.length == 0) {
            return 1;
        }

        int mx = Arrays.stream(nums).max().getAsInt();

        if (mx <= 0) {
            return 1;
        }

        int[] count = new int[mx];
        for (int num : nums) {
            if (num > 0) {
                count[num - 1]++;
            }
        }

        for (int i = 0; i < count.length; i++) {
            if (count[i] == 0) {
                return i + 1;
            }
        }

        return mx + 1;
    }
}