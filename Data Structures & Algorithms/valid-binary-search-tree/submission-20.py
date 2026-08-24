# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        u: dfs?
        m: dfs with many base cases?
        p:
            base case:
                none 
                    -> return
                curr.val is greater than right node
                curr.val is less than left node
                    -> false

                dfs more and check each node 
        '''
        def dfs(curr, low, hi):
            if not curr:
                return True
            if curr.val >= hi or curr.val <= low:
                return False

            return dfs(curr.right, curr.val, hi) and dfs(curr.left, low, curr.val)

        return dfs(root, float('-inf'), float('inf'))
