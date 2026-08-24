# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        - u: can take advantage of bst properties
        - m: tree problem dfs
        - p: 
            compare curr to value of p and q 
            to see which way to iterate to find lca

            bc: null or find lca
            is: if curr  
        '''
        if not root:
            return

        if (root.val < p.val and root.val > q.val) or (root.val > p.val and root.val < q.val) or p.val == root.val or q.val == root.val:
            return root
        
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)

        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right,p,q)
    
        return None
        
        
