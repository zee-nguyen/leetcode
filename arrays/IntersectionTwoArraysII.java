// https://leetcode.com/problems/intersection-of-two-arrays-ii/

// [1,2,5,3,5,6,-1,11,-23]
// [1,0,2,5,9,-23]
// -->[1,2,5,-23]

// RT: O(n+m) since we go through each list only once
// Space: O(n) for hashMap and the intersection list

class IntersectionTwoArraysII {
    public int[] intersect(int[] nums1, int[] nums2) {
        if (nums1.length == 0 || nums2.length == 0) {
            return new int[0];
        }
        List<Integer> res = new ArrayList<>();
        // create a HM of nums1
        Map<Integer, Integer> count = new HashMap<>();
        for (Integer num : nums1) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }
        // check each item in nums2 in HM
        for (Integer num : nums2) {
            if (count.containsKey(num) && count.get(num) != 0) {
                res.add(num);
                count.put(num, count.get(num)-1);
            }
        }
        return res.stream().mapToInt(i->i).toArray();
    }
}