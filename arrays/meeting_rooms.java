// https://leetcode.com/problems/meeting-rooms/

// Sort the array by starting time
// Check for overlapping, i.e. finishing time of i > starting time of i+1

class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));
        for (int i = 0; i < intervals.length-1; i++) {
            if (intervals[i][1] > intervals[i+1][0]) {
                return false;
            }
        }
        return true;
    }
}