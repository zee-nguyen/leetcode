//https://leetcode.com/problems/symmetric-tree/


/**
 * Definition for a binary tree node.  */

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

class SymmetricTree {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }
        return helperIsSymmetric(root.left, root.right);
    }

    private boolean helperIsSymmetric(TreeNode left, TreeNode right) {
        if (left == null && right == null) {
            return true;
        } else if (left == null || right == null) {
            return false;
        } else {
            return left.val == right.val && helperIsSymmetric(left.left, right.right) && helperIsSymmetric(left.right, right.left);
        }
    }
}
