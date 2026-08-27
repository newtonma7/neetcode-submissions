# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        u: 
            find the max path for binary tree, doesn't need
            to be the root
            need to consider split path or never splitting
            also local paths
        m:
            dfs
        p:
        postorder traversal
        dfs
            dfs and find max left and right
            check for negatives

            check if local (split case) max path passes through current node

            if not just return with the curr and max left or right subtree
        '''
        self.mx = root.val

        def dfs(curr):
            if not curr:
                return 0

            leftMax = dfs(curr.left)
            rightMax = dfs(curr.right)

            leftMax = max(leftMax, 0)
            rightMax = max(rightMax,0)

            self.mx = max(self.mx, curr.val + leftMax + rightMax)

            return curr.val + max(leftMax, rightMax)

        dfs(root)
        return self.mx


