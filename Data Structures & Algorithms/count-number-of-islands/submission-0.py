class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        iterate the grid, once we encounter a 1 --> dfs surrounding ones and replace them as a 0
        need to go up down left right with the dfs

        '''
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] != '1':
                return
            else:
                grid[i][j] = '0'
                dfs(i, j+1) #right
                dfs(i+1, j) #down
                dfs(i, j-1) #left
                dfs(i-1, j) #up
                
        islands = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i,j)
        return islands
                 

