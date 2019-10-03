// https://leetcode.com/problems/binary-tree-preorder-traversal/
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class PreorderTraversalBT {
    public List<Integer> preorderTraversal(TreeNode root) {
        Stack<TreeNode> s = new Stack<TreeNode>();
        List<Integer> res = new ArrayList<Integer>();
        s.push(root);

        while (!s.empty()) {
            TreeNode u = s.pop();
            if (u != null) {
                // Right goes in first so left can come out first
                s.push(u.right);
                s.push(u.left);
                res.add(u.val);
            }
        }
        return res;
    }
}
