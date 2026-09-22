class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        u: cycle detection graph problem, 
            undirected graph
            how do we recognize the last edge we took?
                check for cycle then, 
                check current node to parent edge in dfs param
            how do we return the last edge if we detect a cycle early?
                could we have an outside var that points to the one we last removed?
        m: 
            adj list
            visited set
            dfs with parent pointer

            dfs(curr, parent)
                check if in visited
                    if yes, return the cycle edge we just took
                    or set var to edge
                        delete the edge, the dfs should still go on

                add to visited
                iterate edges, ignoring parent
                    dfs
            
            for len(edges):
                if len(dfs) >0 return the thing
        '''
        adj = defaultdict(list)
        

        def connected(start, end):
            visited = set()
            
            # dfs to find end node
            def dfs(curr):
                if curr == end:
                    return True
                
                visited.add(curr)
                for n in adj[curr]:
                    if n not in visited:
                        if dfs(n):
                            return True
                return False

            return dfs(start)

        for u,v in edges:
            if connected(u,v):
                return [u,v]
            adj[u].append(v)
            adj[v].append(u)


