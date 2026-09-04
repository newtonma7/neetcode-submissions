class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        u: multi-source bfs but we absorb more sources into the q
        p:
            init the queue with rotten fruit positions,
                find total fresh fruits as well
            bfs,
                iterate q (rotten fruits)
                    minute represents level,
                    for each rotten fruit, 
                    check neighboring squares if they're fresh
                        mark and add to queue to continue next round


            how determine if rotten fruit cant get all fresh 1s?
                if queue is empty and theres still fresh left, 
                    we know we havent reached any new ones
        '''

        ROWS = len(grid)
        COLS = len(grid[0])
        minutes = 0
        fresh = 0
        q = collections.deque()
        dirs = {(1,0), (0,1), (-1,0), (0,-1)}
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                curr = grid[r][c]
                if curr == 1:
                    fresh +=1
                elif curr == 2:
                    q.append((r,c))
                    visited.add((r,c))
        
        while fresh > 0 and q:
            for i in range(len(q)):
                row, col = q.popleft()

                for dr, dc in dirs:
                    nr = row + dr
                    nc = col + dc
                    if (nr >= ROWS or nc >= COLS 
                    or nr < 0 or nc < 0 
                    or grid[nr][nc] == 0 or (nr,nc) in visited):
                        continue
                    else:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        visited.add((nr,nc))
                        fresh -=1
            minutes +=1
            
        
        if not q and fresh:
            return -1
        
        return minutes

        
                