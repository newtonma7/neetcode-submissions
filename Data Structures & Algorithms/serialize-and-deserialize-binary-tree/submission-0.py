# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        '''
        dfs to encode
        preorder?
        '''
        ans = []

        def dfs(root):
            if not root:
                ans.append("N")
                return 
            
            ans.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(ans)    
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def build():
            if self.i >= len(vals):
                return
            if vals[self.i] == 'N':
                self.i += 1
                return None
            
            curr = TreeNode(int(vals[self.i]))
            self.i +=1

            curr.left = build()
            curr.right = build()
            return curr
        return build()




