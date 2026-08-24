# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        dfs?
            how do we keep track of the nodes before we reach node x
            pass in a list through the method header

            basecase: reach null then ret
            iterative step: 
                check if node is less than all of the ones in the list
                if it isnt then
                    dont count it
                if it is
                    count it
                continue the dfs
        '''

        self.count = 0

        def dfs(node, currMaxInPath):
            passIn = currMaxInPath
            if not node:
                return

            if currMaxInPath <= node.val:
                self.count +=1
                passIn = node.val
            
            dfs(node.right, passIn)
            dfs(node.left, passIn)

        dfs(root, root.val)
        return self.count
