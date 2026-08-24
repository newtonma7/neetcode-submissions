# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        dfs and if we encounter any difference pass up false
        
        base case:
        if not q or if not p return True
            reached the end without a false
        '''
        if not q and not p: return True

        if q and not p: return False

        if not q and p: return False

        if q.val != p.val: return False

        leftCheck = self.isSameTree(p.left, q.left)
        rightCheck = self.isSameTree(p.right, q.right)

        return leftCheck and rightCheck

        