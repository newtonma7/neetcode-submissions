# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        understand: find algo to swap left and right of tree nodes
        match: binary tree with a dfs
        plan:
            dfs
            base case: we hit a leaf or node with no kids
            iterative step: go left and right
            for each node we are at, swap left and right
        '''
        if not root:
            return

        if not root.left and not root.right:
            return root

        root.right, root.left = root.left, root.right

        self.invertTree(root.right)
        self.invertTree(root.left)

        return root