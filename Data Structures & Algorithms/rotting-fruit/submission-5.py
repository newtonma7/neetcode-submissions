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
        self.fresh = 0
        
        def add(r,c):
            # we only want fresh fruits to turn rotten
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                return
            self.fresh -= 1
            grid[r][c] = 2
            q.append([r,c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                if grid[r][c] == 1:
                    self.fresh += 1

        minute = 0
        while self.fresh > 0 and q: # only rotten fruits are in the q beacuse we look for fruits around it
            for i in range(len(q)): 
                r,c = q.popleft()
                add(r + 1, c)
                add(r - 1, c)
                add(r, c + 1)
                add(r, c - 1)
            minute +=1
                    
        if self.fresh == 0:
            return minute
        else:
            return -1

