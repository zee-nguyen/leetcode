// https://leetcode.com/problems/meeting-rooms-ii/

class MeetingRoomsII {
    public int minMeetingRooms(int[][] intervals) {
        if (intervals.length == 0) {
            return 0;
        }

        // sort by starting time
        Arrays.sort(intervals, (a,b) -> a[0]-b[0]);

        // use a priority queue to track earliest time that a room will become available
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.offer(intervals[0][1]);

        for (int i = 1; i < intervals.length; i++) {
            // if the current interval starts after the next earliest one finishes,then we can reuse the room. 
            // take the top time off the queue and add the new finishing time to the queue.
            if (intervals[i][0] >= pq.peek()) {
                pq.poll();
            } 
            pq.offer(intervals[i][1]);
        }
        return pq.size();
    }
}