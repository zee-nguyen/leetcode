// https://leetcode.com/problems/intersection-of-two-arrays/

class IntersectionTwoArrays {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> elements = new HashSet<Integer>();
        Set<Integer> intersection = new HashSet<Integer>();
        
        // get all elements of a list into a set
        for (int i=0; i < nums1.length; i++){
            if (!elements.contains(nums1[i])) {
                elements.add(nums1[i]);
            }
        }
        
        // go through second list, if item already in set -> add to intersect
        for (int j=0; j < nums2.length; j++) {
            if (elements.contains(nums2[j])) {
                intersection.add(nums2[j]);
            }
        }
        
        // get the result list
        int[] res = new int[intersection.size()];
        int i = 0;
        for (Integer num: intersection) {
            res[i++] = num;
        }
        return res;
    }
}