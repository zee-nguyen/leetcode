// https://leetcode.com/problems/binary-tree-inorder-traversal/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        Stack s = new Stack<TreeNode>();
        List<Integer> inorder = new ArrayList<Integer>();
        
        while (root != null || !s.empty()) {
            // keep going left if still possible
            while (root != null) {
                s.push(root);
                root = root.left;
            }
            // when cannot go left anymore, pop stack and go right
            root = (TreeNode) s.pop();
            inorder.add(root.val);
            root = root.right;
        }
        return inorder;
    }
}
