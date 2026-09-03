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
        u: need to create exact mapping and deep copy of graph 
            can use hashmap to map old to new
            dfs each node in the neighbors list to create mapping/find edges

        p:
            dfs,
                base case:
                    the node has no neighbors, return

                iterative step:
                    iterate neighbors, dfs each one

                pass in current node,
                make the current node with hashmap mapping,
                iterate over list of neighbors and dfs into each one

                can just use old node as the key to the hashmap to new node

            add all values of hashmap to the ans
        '''

        ans = []
        oldtonew = {None : None}

        if not node:
            return

        def dfs(curr):
            if not curr.neighbors:
                return Node(curr.val)
            if curr in oldtonew:
                return oldtonew[curr]

            copy = Node(curr.val)
            oldtonew[curr] = copy
            
            for n in curr.neighbors:
                oldtonew[curr].neighbors.append(dfs(n))
                    
            return copy

        return dfs(node)

        