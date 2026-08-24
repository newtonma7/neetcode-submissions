# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        plan:
            dfs where we track height of the left and right children
            if abs(dfsleft - dfsright) > 1 pass up flag


        '''

        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            
            return 1 + max(left,right)

        return dfs(root) != -1




