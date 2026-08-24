# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        input: root and a number kth
        output: kth smallest value from tree

        utilize bst properties to help us in this search
            k = 1 --> we find the smallest value in bst, all the way left

        how does the kth thing help bc we dont have index'd
            if we go right subtree, 
                we have to get height of left to subtract from k
        '''
        self.ans = 0
        self.kay = k

        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            self.kay -= 1

            if self.kay == 0:
                self.ans = root.val
                return
            dfs(root.right)
        dfs(root)
        return self.ans



        