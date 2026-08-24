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

        # creates the adjacency list
        for u,v in prerequisites:
            adj[u].append(v)

        # check the node and edges
        # if the current node appears
        
        visit = set() # tracks nodes in current DFS path
        
        def dfs(crs):
            #base cases
            if crs in visit: # there is a cycle in the graph
                return False
            if adj[crs] == []: # if we see [], there is a clear path and no prereqs
                return True

            # add course to visited and search its prereqs
            visit.add(crs)
            for pre in adj[crs]: # search through the prereqs to find a cycle
                if not dfs(pre): return False

            # this course has passed our dfs, so we can check it off
            visit.remove(crs) 
            adj[crs] = [] 
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True
        

