# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        always symmetric?

        recursion
        what kind of tree search should we do?

        DFS

        swap the two children of the curr node

        base case:
            root none --> return

        iterative step:
            go left 
            go right
        '''


        if root is None:
            return root

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.right)
        self.invertTree(root.left)
        
        
        return root