class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        u: build adjacency list from prereqs,
            dfs the adjacency list with a visited set to determine if we can finish all courses
            we are detecting if there is a cycle in the list 
                determine with numcourses == len(visited)
        p:
            build adjacency list from prereqs
                course : prereq
            dfs
                visited set
                base case: visited already, prereq is already cleared, or no prereqs
                iterative step:
                    loop through prereqs of that one course to continue dfs
                    mark as visited
                    clear it as a prereq
        '''
        courses = defaultdict(list)
        visited = set()

        for u,v in prerequisites:
            courses[u].append(v)

        def dfs(curr):
            if curr in visited:
                return False
            if courses[curr] == []:
                return True
    
            visited.add(curr)

            for pre in courses[curr]:
                if not dfs(pre):
                    return False
        
            visited.remove(curr)
            courses[curr] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


        
