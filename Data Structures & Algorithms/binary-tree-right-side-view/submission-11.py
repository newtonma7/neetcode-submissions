# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        dfs on the right side only
            needs a dfs function bc we dont want to return list all the time
            this is only true when there is always a right child 
        bfs
            since a left or right child could be visible, we gotta go level by level
            right child should have priority over the left children
                still will always append the left child, 
                incase the next level only has left children
            algo for priority and adding to the deq
                add all nodes to the queue
                if the node is non null:
        '''
        if not root:
            return []
        ans = []
        q = collections.deque()

        q.append(root)
        while q:
            levelSize = len(q)
            for i in range(levelSize):
                node = q.popleft()

                if node and node.left:
                    q.append(node.left)

                if node and node.right:
                    q.append(node.right)

                # if the node is the last one, we record it
                if i == levelSize - 1:
                    ans.append(node.val)
                    
        return ans


