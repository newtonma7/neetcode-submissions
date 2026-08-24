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
        
        def equals(root1,root2):
            # we've hit the end and theres no more to dfs so it checks
            if not root1 and not root2:
                return True

            if root1 and root2 and root1.val == root2.val:
                return equals(root1.right, root2.right) and equals(root1.left, root2.left)
            
            return False

        # empty subtree is always subtree
        if not subRoot:
            return True

        # there is no more root to check
        if not root:
            return False

        #this checks if at any point, subtree is equal to a point in the tree
        if equals(root, subRoot):
            return True
        
        #checks if either child node is a subRoot
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)


            

        




