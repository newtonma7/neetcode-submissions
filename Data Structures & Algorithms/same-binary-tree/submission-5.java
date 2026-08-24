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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        /*
            input: two tree node roots with left and right children
            output: true if the trees are equivalent
            
            same structure and same values in the nodes
                nulls need to be mimicked overall structure
            
            if left is null the other trees left also has to be null

            base case: if we dfs completely and hit a leaf and its null 
                then should be true
                both kids are null
                left null
                right null
        */
        if(p == null && q == null){
            return true;
        }
        if(q == null ||  p == null || (p.val != q.val)){
            return false;
        }
        
        return isSameTree(p.left, q.left) && isSameTree(p.right,q.right);

    }
}
