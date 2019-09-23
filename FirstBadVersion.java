// https://leetcode.com/problems/first-bad-version/

/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */


// All versions after bad version are bad
// Find first bad version

// Intuition:
// Use binary search
// If mid is bad, we know that everything after it is bad. Need to check the left to see if the first bad version is in the left portion.
// If mid is not bad, we know that everything before it is good. Check right portion for bad version.

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        return binarySearch(1, n);
    }

    // Need a function to perform BS
    private int binarySearch(int start, int end) {
        while (start < end) {
            int mid = start + (end - start)/2;
            if (isBadVersion(mid)) {
                // check left, but mid could be first bad version so include it
                end = mid-1;
            } else {
                // check right
                start = mid + 1;
            }
        }
        return start;
    }
}