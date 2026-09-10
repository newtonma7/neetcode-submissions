class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        u:  undirected graph with number of components
                edges go both ways

            need a way to recognize whole connected component 

            how do we understand that the current dfs path
            represents one whole connected component?

            iterate all edges from one node, and add them to a set,
                from there we should've found all connected nodes to that start node 
                and added them to a set
            if we iterate the rest of the nodes in the adj list and we haven't seen it
            yet, then it means its a new component
        

            dfs
                base case: 
                    if is in visited already: return True

                    add to set
                    iterate all its edges:

            in the actual loop iterating all nodes, if one node is not in the set yet
            increment the component counter
        p:
            visited set 
            components count

            dfs
                visited check, true is same component or already seen

                add to visited,
                iterate all edges
                    dfs
        '''

        visited = set()
        components = 0
        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)


        def dfs(i):
            if i in visited:
                return

            visited.add(i)
            for e in adj[i]:
                dfs(e)

        for j in range(n):
            if j not in visited:
                components +=1
                dfs(j)
        return components