# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        u: bfs
        m: bfs but only care abt right most
        p: standard bfs
            init deq w root
                push entire layer onto deq,
                peek the rightmost node in q for that layer -> done once
                pop as we iterate and add the kids -> done over the layer
                append to ans
        '''

        q = collections.deque()
        q.append(root)
        ans = []

        while q:
            right = None
            for i in range(len(q)):
                curr = q.popleft()
                if curr:
                    right = curr
                    q.append(curr.left)
                    q.append(curr.right)
            if right:
                ans.append(right.val)
        return ans
                
                

                