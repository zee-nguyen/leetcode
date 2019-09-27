// n1 = [4,1,2] - len: n
// n2 = [1,3,4,2] - len: m
// --> [-1, 3, -1]

// n1 = [4,1,2]
// n2 = [1, 0, 4, 2]
// --> [-1, 4, -1]

// output length == n1 len
// n1 is subset of n2, so n2 len >= n1 len

// end of array? --> yes --> -1

class NextGreaterElementI {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        public int[] nextGreaterElement(int[] nums1, int[] nums2) {
            // Improving upon brute force
            // We can preprocess the data to find the next greater number of each element using a stack
            
            // Put all elements in n1 into a map with form [value, next_greater_number]
            Map<Integer, Integer> map = new HashMap<>();
            Stack<Integer> stack = new Stack<>();
            
            for (int i = 0; i < nums2.length; i++) {
                while (!stack.isEmpty() && nums2[i] > stack.peek()) {
                    map.put(stack.pop(), nums2[i]);
                }
                stack.push(nums2[i]);
            }
            
            while (!stack.isEmpty()) {
                map.put(stack.pop(), -1);
            }
            
            int[] res = new int[nums1.length];
            for (int i = 0; i < nums1.length; i++) {
                res[i] = map.get(nums1[i]);
            }
            
            return res;
        }
    }
}