class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        multisource bfs
            initial pass, check for rotten fruits
                and add those to the deq
            once we find the init pos for rotten fruits
                look around for fresh fruit,
                add helper function with logic to check for bounds

            counter for minutes will end once deq is empty
            instead of set, we can set the fruit to rotten to say we visited alr
        '''

        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        
        def add(r,c):
            # we only want to add fresh fruit to turn rotten
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or grid[r][c] == 2:
                return
            grid[r][c] = 2
            q.append([r,c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])

        minute = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                add(r + 1, c)
                add(r - 1, c)
                add(r, c + 1)
                add(r, c - 1)
            if len(q) > 0:
                minute +=1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
                    
        return minute

