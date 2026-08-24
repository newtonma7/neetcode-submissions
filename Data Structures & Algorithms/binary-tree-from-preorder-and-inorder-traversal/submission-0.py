# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        input : 
        preorder array
            parent, left, right
            root.val
            dfs(left)
            dfs(right)

        inorder array
            left, parent, right
            dfs(left)
            root.val
            dfs(right)
        output: root of the tree

        problem is that we dont know node relationships in correlation to spot in the array

        use preorder to iterate through all the nodes
        can use inorder to find node relationships
            all nums left of the root in inorder are left subtree
            all nums right of root in inorder are right subtree
        '''
        hm = {}
        for num in preorder:
            hm[num] = inorder.index(num)

        # index for us to iterate the preorder array
        preIdx = 0
        
        # use l and r ptrs to partition out the inorder array to build the subtrees
        def dfs(l, r):
            nonlocal preIdx
            # if l and r cross, then we have hit a leaf, return none
            if l > r:
                return None

            # create the node we will be building subtrees for
            rootVal = preorder[preIdx]
            preIdx += 1
            root = TreeNode(rootVal)
            mid = hm[rootVal]

            # in the inorder array, everything from l to mid - 1 is the left subtree
            root.left = dfs(l, mid - 1)

            # everything from mid + 1 to r is the right subtree
            root.right = dfs(mid + 1, r)

            return root

        return dfs(0, len(inorder) - 1)
            

            


    