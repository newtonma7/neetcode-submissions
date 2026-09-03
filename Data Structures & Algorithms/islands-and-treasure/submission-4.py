class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        u: can do a bfs from a treasure chest 
            iterate the board,
                once we find a treasure chest,
                start the bfs for surrounding squares and move around
            NEED to init q with all of the chests in the q
        p:
            bfs 
                add all 4 directions to the q
                if moving in a certain direction is -1, then dont add it?
                increment counter for layer of bfs
        '''

        q = collections.deque()
        dist = 1
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = {(-1,0), (1,0), (0,-1), (0,1)}

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        while q:
            row, col = q.popleft()

            for dr, dc in dirs:
                nr = row + dr
                nc = col + dc
                if (nr >= ROWS or nc >= COLS or nr < 0 
                or nc < 0 or grid[nr][nc] != 2147483647):
                    continue
                else:
                    grid[nr][nc] = grid[row][col] + 1
                    q.append((nr,nc))
                


    
                
