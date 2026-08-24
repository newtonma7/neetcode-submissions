# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        understand: need longest path between any two nodes
        match: binary tree, dfs 
        plan:
            at each node, we need to evaluate left and right subtrees
            then pass up the longer child <------
            base case:
            none
            iterative step:

        '''
        self.ans = 0
        
        def dfs(boot):
            if not boot:
                return 0

            left = dfs(boot.left)
            right = dfs(boot.right) 
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.ans