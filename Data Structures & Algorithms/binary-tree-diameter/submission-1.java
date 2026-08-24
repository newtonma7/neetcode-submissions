/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int diameterOfBinaryTree(TreeNode root) {
        /*
            helper function to find height
            base case: hitting null
            iterative step: dfs into left and right subtree

            calculate the diameter passing through the current node
                requires finding height of left and right subtree + 1
                we take the max height we've found
        */
        int[] diam = new int[1];
        dfs(root, diam);
        return diam[0];
    }

    public int dfs(TreeNode root, int[] diam){
        if(root == null){
            return 0;
        }

        int left = dfs(root.left, diam);
        int right = dfs(root.right, diam);
        diam[0] = Math.max(diam[0], left + right);

        return 1 + Math.max(left,right);

    }
}
