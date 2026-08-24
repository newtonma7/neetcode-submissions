# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        DFS

        increment decrement trick
        we can keep track of a height var and it must be <2
        left we can +1
        right we can -1



        two pointer?
        if either right or left ever go beyond
        '''
        self.height = 0

        def dfs(curr):
            if not curr:
                return 0 

            left = dfs(curr.left)
            right = dfs(curr.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            
            return 1 + max(left,right) 

        return dfs(root) != -1






        
        