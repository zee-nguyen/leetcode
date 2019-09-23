// https://leetcode.com/problems/binary-tree-paths/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
*/

// Input: a root node that represent a binary tree
// Output: The list of all paths from root to leaf node as string in the form "1 -> 2 -> 3"

// Intuition:
// We know we have a path when we hit a leaf node.
// If we're at a non-leaf node, that's not a path. So we only add to the resulting list if we're at the leaf.
// Use a string to build the path as we go. Only when we hit a leaf node, add the end string to the resulting list.


class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> output = new ArrayList<>();
        helperTraverse(root, "", output);
        return output;
    }

    // Need a private method that will recurse through the tree and build the string as we go
    // Params: root node of the tree, path is the string we're building, output is the list of all paths
    private void helperTraverse(TreeNode root, String path, List<String> output) {
        if (root == null) {
            return;
        }
        //If we're at the leaf node, add it to the path and add the path to the output
        //Else, keep going left or right and build the path
        else if (root.left == null && root.right == null) {
            path += Integer.toString(root.val);
            output.add(path);
        }
        else { // either left or right or both is present
            path += Integer.toString(root.val) + "->";
            helperTraverse(root.left, path, output);
            helperTraverse(root.right, path, output);
        }

    }
}