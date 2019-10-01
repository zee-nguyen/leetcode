// Write a function:

// class Solution { public int solution(int[] A); } that, given an array A of N integers,
// returns the smallest positive integer (greater than 0) that does not occur in A.

// For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
// Given A = [1, 2, 3], the function should return 4.
// Given A = [−1, −3], the function should return 1.

// Write an efficient algorithm for the following assumptions:

// N is an integer within the range [1..100,000];
// each element of array A is an integer within the range [−1,000,000..1,000,000].


// you can also use imports, for example:

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

import java.util.Arrays;
import java.util.Collections;

/*
* Analysis:
*
* - Runtime: O(n) where n is the number of items in the array
*           - We go through array once to find max item - O(n)
*           - Go through it again for the count of each item - O(n)
*           - Go through the mapping array to check for first missing positive. - O(max)
*             Even though this mapping array might be big, the algorithm cannot go to the end of it because that would
*             mean the length of the array is just as big.
*   Overall, O(n) runtime
*
* - Space: O(max) where max is the max value in the array
*
* Can optimize to O(n) time and O(1) space. That'll come up next!
* */

class FirstMissingPositive {
    public int firstMissingPositive(int[] A) {
        // create a count map for all items in A from 1 to max value
        // first positive number with value of 0 is the missing one.
        // careful about indexing
        int max = 0;
        for (int num : A) {
            if (num > max) {
                max = num;
            }
        }

        int[] map = new int[max + 1];
        for (int num: A) {
            if (num >= 1) {
                map[num - 1]++;
            }
        }

        // map from 0 onwards. If the input array only contains negative numbers then we'll be able to return 1.
        for (int i = 0; i < map.length; i++) {
            if (map[i] == 0) {
                return i + 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        FirstMissingPositive obj = new FirstMissingPositive();
        int[] input = {6};
//        int[] input = {-1,1,3,0,2,4,3,-2,6,9,15,4};
        System.out.println(obj.firstMissingPositive(input));
    }
}
