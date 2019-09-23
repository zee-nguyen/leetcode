// https://leetcode.com/problems/top-k-frequent-elements/

class TopKFrequentElements {
    public List<Integer> topKFrequent(int[] nums, int k) {
        // count the number of occurances for each number in nums
        Map<Integer, Integer> count = new HashMap<>();
        for (int n: nums) {
            count.put(n, count.getOrDefault(n, 0) + 1);
        }
        
        // Use a priority heap (min heap) 
        // When size of the heap reaches k, take out the min items
        // Repeatedly doing this will result in the top k frequent elements left in the queue
        
        // Sort the heap by occurance every time to add a new item to the heap
        PriorityQueue<Integer> heap = new PriorityQueue<>((n1, n2) -> count.get(n1) - count.get(n2));
        
        // for each key in the hashmap, put it in the heap (min heap sorted by # of occurances)
        for (int n: count.keySet()) {
            heap.add(n);
            if (heap.size() > k) {
                heap.poll();
            }
        }
        
        List<Integer> res = new ArrayList<>();
        
        while (heap.size() > 0) {
            res.add(heap.poll());
        }
        
        // The heap was min heap, so when we poll the item out, it was in ascending order
        // We need it to be in descending order, so the most frequent item is at the beginning of the list and the less frequent ones follow
        // Hence, reverse before returning
        
        Collections.reverse(res);
        return res;
    }
}