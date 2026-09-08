class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        u: course schedule but build the course order instead of returning true or false
            adj list w default dict

            detect cycle
            new base case and return values, but overall logic should be the same
        p:
            adj list init
            visited set to track local path, list param for the local path as well
            dfs
                bc: in the set --> false, prereqs cleared is true
                is: loop through prereqs, 
                        if true, add it to the list 
        '''

        courses = defaultdict(list)

        for u,v in prerequisites:
            courses[u].append(v)
        
        visiting = set()
        completed = set()
        path = []

        def dfs(curr):
            if curr in visiting:
                return False
            if curr in completed:
                return True
            
            visiting.add(curr)
            for pre in courses[curr]:
                if not dfs(pre):
                    return False

            visiting.remove(curr)
            completed.add(curr)
            path.append(curr)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return path
