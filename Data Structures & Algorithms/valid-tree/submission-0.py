class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        u: valid tree = no cycle in the graph
            graph prob, dfs and look for a cycle?
            use an adj list since we have undirected edges

            cycle detection with completed, visiting sets?
                do we need two sets? 
            undirected edges so we have to append edge both ways 
            am i missing something since its undirected edges?

        p:
            visiting set --> currently visiting in local path
            completed --> fully explored this node and all its edges
            
            dfs
                base case: 
                    if we hit a node we already completed, True 
                    if we hit a node in visiting, False since there is a cycle
                inductive step:
                    add current node to visiting
                    iterate through all its edges
                mark node as complete
                remove it from visiting to reflect local state
            how is traversal different when we have more edges/ edges go to both nodes
                do i need to mark the node off in both maps?
        '''

        visited = set()
        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(curr, parent):
            if curr in visited:
                return False
                
            visited.add(curr)
            for j in adj[curr]:
                if j == parent:
                    continue
                if not dfs(j,curr):
                    return False
            return True
            
        return dfs(0,-1) and len(visited) == n
