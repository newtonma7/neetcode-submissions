class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        dfs vs bfs?
        dfs 
            inefficient and explores every path
        bfs
            bfs from each gate instead of dfs from each room
            initialize the q with positions of gates
            expand outward each traversal, marking dist
            we can use a set or check for INF to 
                make sure the room is marked with the min dist

            add logic
                return if index out of bounds or we hit water or we have visited already
        '''

        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        q = deque()
        
        # check if the add coords are valid
        # adds then to visit set and to queue
        def add(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visit or grid[r][c] == -1:
                return
            visit.add((r,c))
            q.append([r,c])

        # initialize the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))

        # traverse this layer of the queue
        dist = 0
        while q:
            for i in range(len(q)): # first iteration, we pop all the gates
                r, c = q.popleft()
                grid[r][c] = dist
                add(r + 1, c)
                add(r - 1, c)
                add(r, c + 1)
                add(r, c - 1)
            dist += 1



