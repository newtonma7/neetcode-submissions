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

        
        visiting = set() # Tracks nodes in current DFS path

        def has_cycle(course):
            visiting.add(course)
            for neighbor in adj[course]:
                if neighbor in visiting:
                    return True # Cycle detected
                if has_cycle(neighbor):
                    return True
            visiting.remove(course) # Backtrack
            return False
        
        for i in range(numCourses):
            if has_cycle(i):
                return False
        return True
        

