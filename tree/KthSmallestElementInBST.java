// https://leetcode.com/problems/kth-smallest-element-in-a-bst/

// Intuition:
// Build an pre-order traversal, which will be the correct ascending order
// Then return the item k-1

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class KthSmallestElementInBST {
    public int kthSmallest(TreeNode root, int k) {
        List<Integer> res = new ArrayList<>();
        preorder(root, res);
        return res.get(k-1);
    }
    
    private void preorder(TreeNode root, List<Integer> res) {
        if (root == null) {
            return;
        }
        preorder(root.left, res);
        res.add(root.val);
        preorder(root.right, res);
    }
}