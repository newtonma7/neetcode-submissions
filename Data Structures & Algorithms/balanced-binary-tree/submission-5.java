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
    public boolean isBalanced(TreeNode root) {
        /*
            helper dfs function
            base case: null or check flag to see if we lost balance
            iterative step: dfs left and right

            through each node we calculate height of local left and right
                return the height, if the difference ever reaches more than 1 --> send flag
        */
        int check = dfs(root);

        if(check == -1){
            return false;
        }
        return true;
    }

    public int dfs(TreeNode root){
        if(root == null){
            return 0;
        }
        int left = dfs(root.left);
        int right = dfs(root.right);

        if(left == -1 || right == -1 || Math.abs(left - right) > 1){
            return -1;
        }

        return 1 + Math.max(left, right);
    }
}
