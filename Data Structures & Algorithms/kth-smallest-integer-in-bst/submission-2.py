# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        brute/heap sol is nlogn
        
        u: dfs with a incrementer/decrementer
        m: since we want the kth smallest integer,
            we wanna find a way to iterate it like an array, 
            iterate with decermenter, 
            left subtree first and once finish with left, start going right 
        p:
        dfs left, decrement counter, then go right
        once decrement is 0 return current value
        '''
        self.ans = 0
        self.kth = k
        
        def dfs(curr):
            if not curr:
                return

            dfs(curr.left)
            self.kth -= 1
            if self.kth == 0:
                self.ans = curr.val
                return curr.val

            dfs(curr.right)

        dfs(root)
        return self.ans

        
        
            

