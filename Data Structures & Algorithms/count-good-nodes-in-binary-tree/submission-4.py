# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        u:dfs
        m:dfs with a param to compare
        p:dfs helper
            carry a param through the dfs
            that is the greatest value in the path, 
            if the node we are at is greater 
                then increase the global var
        '''

        self.ans = 0

        def dfs(curr, mx):
            if not curr:
                return

            param = mx
            if curr.val >= mx:
                self.ans+=1
                param = curr.val
    
            dfs(curr.left, param)
            dfs(curr.right, param)
        
        dfs(root,float('-inf'))
        return self.ans

