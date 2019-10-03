import java.util.Stack;
//https://leetcode.com/problems/same-tree/


public class SameTreeIterative {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        Stack<TreeNode> stack = new Stack<>();

        stack.push(p);
        stack.push(q);

        while (!stack.isEmpty()) {
            TreeNode first = stack.pop();
            TreeNode second = stack.pop();
            if (first == null && second == null) {
                continue;
            } else if (first == null || second == null) {
                return false;
            } else {
                if (first.val != second.val) {
                    return false;
                }
                stack.push(first.left);
                stack.push(second.left);

                stack.push(first.right);
                stack.push(second.right);
            }
        }
        return true;

        // RECURSIVE

        // if (p == null && q == null) {
        //     return true;
        // } else if (p == null || q == null) {
        //     return false;
        // } else {
        //     return p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        // }
    }
}
