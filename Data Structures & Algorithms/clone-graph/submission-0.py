"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        edge cases: 1 node, 0 node
        create a hashmap of old node to new node

        dfs algo, assuming no cycles or dupe edges
        we can just use our hm to check if we cloned it already
            base case: we have already seen the node, return the copy node
            iterative step: append as neighbor, add to set --> loop through and dfs each node
        '''
        # map from old node to new node
        hm = {}

        #dfs to clone tha graph
        def dfs(node):
            if node in hm:
                return hm[node]
            else: # create the clone if we havent seen it, and append to neighbor list
                hm[node] = Node(node.val)
                for neigh in node.neighbors:
                    dfs(neigh)
                    hm[node].neighbors.append(hm[neigh])
        if not node: return node
        dfs(node)
        return hm[node]




        