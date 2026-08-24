# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        dfs problem
        what about equals case?
        base case for true? --> make it to the end of the tree 
        base case for false? violation of the bst rule

            if not node:
                ret true
            then check for violations of the bst rule for the node we are currently on
                this would only work if the node, do we need to think beyond the scope of just checking
                left and right? i dont think so

            return both left and right are isvalidbst <-- this will be our dfs step
        ###
        should do local check as well?
        for a valid bst, the property needs to hold true for all ancestors
        pass down a valid range to the children to check
        for the left side we have to check if it is lower than the greatest value we've seen
        for the right side we check against the greater than the lowest value we've seen
        
        '''

        def dfs(r, lowerbound, upperbound):
            if not r:
                return True
            
            if r.val >= upperbound or r.val <= lowerbound:
                return False
            
            return dfs(r.left, lowerbound, r.val) and dfs(r.right, r.val, upperbound)

        return dfs(root, float("-inf") , float("inf"))
            
    