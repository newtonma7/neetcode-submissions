# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        u: dfs from the parent to find its children
        m: dfs/ think like you are the parent node, what do we do?
        p:
            starting at paren, start the dfs into the kids,
            if we are a kid or find the kid, return found,
            if we find the kid in the left or right tree return found
            if we then find both, we are the lowest common ancestor?
        '''
        ans = None

        def dfs(curr):
            nonlocal ans
            if not curr:
                return False

            mid = (curr.val == p.val or curr.val == q.val)
            left = dfs(curr.left)
            right = dfs(curr.right)

            if left and right or left and mid or right and mid:
                ans = curr
            
            return left or right or mid
        dfs(root)
        return ans
 

        
            

