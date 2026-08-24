class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        if there is a cycle in the graph then we return false

        how do we create this kind of graph?
            hm adjacency list
        
        class becomes the node
        we create a directed edge between classes --> keeps the flow in one direction
            hashmap with adjacency list

        if we notice that there are is a cycle between two nodes then we return false
            dfs to find a cycle
        '''

        adj = defaultdict(list)

        for u,v in prerequisites:
            adj[u].append(v)

        # check the node and edges
        # if the current node appears

        visit = set() # Tracks nodes in current DFS path
        def dfs(crs):
            if crs in visit:
                return False
            if adj[crs] == []:
                return True

            visit.add(crs)
            for pre in adj[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            adj[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True
        

