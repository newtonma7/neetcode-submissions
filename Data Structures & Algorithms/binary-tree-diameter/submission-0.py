# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        BFS?
        DFS?
        Find the longest path between any two nodes in the tree <--
        everytime we reach a new node, increment the return val
        max()
        '''
        self.diam = 0

        # extra function to return height
        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            self.diam = max(self.diam, left + right)

            return 1 + max(left, right)

        dfs(root)
        
        return self.diam



        