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
        int n = nums1.length;
        int m = nums2.length;
        int[] res = new int[n];
        
        for (int i = 0; i < n; i++) {
            if (nums1[i] == nums2[m-1]) {
                res[i] = -1;
            }
            
            for (int j = 0; j < m; j++) {
                if (nums1[i] == nums2[j]) {
                    for (int k = j+1; k < m; k++) {
                        if (nums2[k] > nums1[i]) {
                            res[i] = nums2[k];
                            break;
                        } else {
                            res[i] = -1;
                        }
                    }
                }
            }
            
        }
        return res;
    }
}