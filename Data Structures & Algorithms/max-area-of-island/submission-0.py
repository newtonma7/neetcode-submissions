class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        max counter

        traversal
        iterate the 2d matrix and when we encounter a 1, begin the dfs

        dfs algo
            base case:
                when the index will become out of bounds for our search
                    we hit any of the 4 walls of the grid
                        return
                when we encounter a 1 set it to 0, increment counter
                for grid[r][c], we check
                up = [r-1][c]
                down = [r+1][c]
                left = [r][c-1]
                right = [r][c+1]
        '''

        self.curr = 0
        currMax = 0
        ROWS = len(grid)
        COLS = len(grid[0])


        def dfs(i,j):
            if i >= ROWS or j >= COLS or i < 0 or j < 0 or grid[i][j] != 1:
                return
            else:
                grid[i][j] = 0
                self.curr += 1
                dfs(i-1, j)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i,j+1)
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    dfs(i,j)
                    currMax = max(self.curr,currMax)
                    self.curr = 0
        dfs(0,0)
        return currMax