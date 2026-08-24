# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        subroot will always be a node and two children? or 

        dfs
            DFS the first tree,
                if we encounter a match for the node value, 
                    we dfs the both root and subroot to check equality
                if we dfs the entire root and do not encounter anything return false
        '''
        #we have dfs'd all we can and theres nothing left
        def equals(root1,root2):
            # we've hit the end and theres no more to dfs so it checks
            if not root1 and not root2:
                return True

            if not root1 or not root2 or root1.val != root2.val:
                return False
            
            return equals(root1.right, root2.right) and equals(root1.left, root2.left)

        if not subRoot:
            return True

        if not root:
            return False

        if equals(root, subRoot):
            return True

        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)


            

        




