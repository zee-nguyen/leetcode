class MergeIntervals {
    public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1 || intervals == null) {
            return intervals;
        }
        
        // sort arrays by starting time
        Arrays.sort(intervals, (i1, i2) -> i1[0]-i2[0]);
        
        int[] cur = intervals[0];
        List<int[]> res = new ArrayList<>();
        
        // can use for each loop here
        for (int i = 1; i < intervals.length; i++) {
            if (this.isOverlapped(cur, intervals[i])) {
                cur = this.mergeTwoIntervals(cur, intervals[i]);
            } else {
                res.add(cur);
                cur = intervals[i];
            }
        }
        res.add(cur);
        
        // int[][] result = new int[res.size()][2];
        
        // for (int j = 0; j < res.size(); j++) {
            // System.out.println(res.get(j));
            // result[j] = res.get(j);
        // }
        
        // return result;
        return res.toArray(new int[res.size()][]);
    }
    
    // i1 and i2 are sorted by starting time
    // two sorted intervals are overlapped if the second invertal's starting time is before the first interval's ending time
    public boolean isOverlapped(int[] i1, int[] i2) {
        return i2[0] <= i1[1];
    }
    
    // merge two intervals
    // the resulting intervals has the smaller starting time and bigger ending time out of the two given intervals
    public int[] mergeTwoIntervals(int[] i1, int[] i2) {
        int[] result = new int[2];
        result[0] = i1[0] <= i2[0] ? i1[0]:i2[0];
        result[1] = i1[1] >= i2[1] ? i1[1]:i2[1];
        return result;
    }
}