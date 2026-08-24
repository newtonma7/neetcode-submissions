# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        u: dfs
        m: dfs but partition the arrays
        p:
            use the preorder array to find value in inorder
            partition accordingly to find subtrees and recursively find what to build

        '''
        hm = {val: idx for idx, val in enumerate(inorder)}

        self.preord = 0
        def dfs(l,r):
            if l > r:
                return None

            val = preorder[self.preord]
            self.preord += 1
            mid = hm[val]
            curr = TreeNode(val)

            curr.left = dfs(l, mid - 1)
            curr.right = dfs(mid + 1, r)
            return curr
        return dfs(0, len(inorder) - 1)

            
            
