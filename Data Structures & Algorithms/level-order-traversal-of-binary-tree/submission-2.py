# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        u: bfs
        m: bfs
        p: init the deque with the root, then while deq exists
            iterate and add the kids to the deque
            continue till null
        '''
        q = collections.deque()
        q.append(root)
        ans = []

        while q:
            level = []
            for i in range(len(q)): 
                curr = q.popleft()
                if curr:
                    level.append(curr.val)
                    q.extend([curr.left, curr.right])
            if level:
                ans.append(level)
        return ans
        
        