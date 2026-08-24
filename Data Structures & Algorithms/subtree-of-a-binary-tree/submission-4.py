# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        u: have to find if subroot exists as a subtree in root
        m: dfs, might have to use same binary tree code
        p: 
            base case:
                hit none/leaf
                    return false
                
                def same()

                run the helper method on each one to see subtree starts there
        '''

        if not root:
            return False
        if self.same(root,subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def same(self, p,q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.same(p.left, q.left) and self.same(p.right,q.right)
