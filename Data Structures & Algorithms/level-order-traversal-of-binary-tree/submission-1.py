# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        bfs with a deque
            append root first
            
            while deque has nodes
                append children
        '''
        ans = []
        q = collections.deque()
        #add root to start the deq loop
        q.append(root)

        #while the q is not empty
        while q:
            #level to add the the list
            currLevel = []

            #iterate through the deq
            for i in range(len(q)):
                #pop the node currently at the front
                node = q.popleft()
                #if non null then we want to add it to the current level
                #take its children and add it to the deque as well so we can iterate again
                if node:
                    currLevel.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            #if the node wasnt null, currlevel should exist
            if currLevel:
                ans.append(currLevel)

        return ans
                
