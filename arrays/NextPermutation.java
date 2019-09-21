// 1. if the sequence is descending, there is no bigger permutation -> reverse the list and return
// Notice, if a subsequence is descending, 4-3-2-1 for ex, we cannot swap any item to make a bigger permutation. Any swap will result in a smaller permutation.
// The item of interest is the first item that is not part of a descending sequence, going from right to left. Why right to left? The next bigger intuitively is something that can be swapped on the right, for ex, 4-3-1-2, swap 2 and 1 we can next bigger permutation 4-3-2-1. 
// Once we find the item of interest (called i), the next bigger permutation can be made from swapping i with the next number that is bigger than i on its right side. 

//Ex: 6-2-1-5-4-3-0
// item of interest: 1
// next bigger number: 3
// At index 2, we have number 1. All permutations of form 6-2-1-X-X-X-X have been exploited and we cannot have anything bigger.
// The next item we can plant at index 2 is the next bigger number than 1, which is 3.

// Swap 1 and 3, we get 6-2-3-5-4-1-0
// but again, 5-4-1-0 is descending sequence, it is THE LAST PERMUTATION of form 6-2-3-X-X-X-X
// we want the first permutation, so we reverse the list starting from the right of 3.
// Hence, we get 6-2-3-0-1-4-5, which is the next bigger permutation we're looking for.

class NextPermutation {
    public void nextPermutation(int[] nums) {
        // find the item of interest, i
        int i = nums.length - 2;
        while (i >= 0) {
            // still descending, keep going back
            while (i >= 0 && nums[i] >= nums[i+1]) {
                i--;
            }
            // only swap if i is inbound
            // i is out of bound means the whole array is in descending order - no next permutation.
            if (i >= 0) {
                // find and swap with next bigger number than i
                int j = nums.length-1;
                while (nums[j] <= nums[i]) {
                    j--;
                }
                swap(nums, i, j);
            }
            reverse(nums, i+1);
            break;
        }
        
        // reverse the list from i+1 to end of list
    }
    
    // Helper function to swap the values at index i and index j
    public void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    
    // Helper function to reverse a given array from the starting index to the end of the array
    public void reverse(int[] nums, int start) {
        int i = start, j = nums.length-1;
        while (i < j) {
            swap(nums, i, j);
            i++;
            j--;
        }
    }
}