# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        dfs
            since this is a binary search tree,
                 all values to the left are lesser
                 all values to the right are greater
            how does this help us?
                help us make decisions on which subtree to dfs
            traverse from root
                if p and q greater than root
                    root = root.right
                if p and q less than root
                    root = root.left
                if we enter a part where p and q diverge, then we have found our ancestor?
        '''

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if (p.val > root.val and q.val < root.val) or (p.val < root.val and q.val > root.val) or p == root or q == root:
            return root
            
        return root