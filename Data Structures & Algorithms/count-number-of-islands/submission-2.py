class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        u: dfs into islands as we iterate over the entire board 
        p:
            global counter var
            iterate over board
                if we hit an island increment counter then
                    dfs into it and mark it as visited
                    can do inplace by marking it as 0

            what are we passing into dfs? what does it interact with?
                visited set is shared state
                r, c resides in local calls
            dfs, 
                explores and marks the chunk island we encountered as visited
                base case: invalid indices, visited or 0,
                iterative step:
                    explore all 4 directions from the spot
        '''
        num = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            if r >= rows or c >= cols or r < 0 or c < 0 or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'

            # dont care about any return values, 
            # we just need to mark the island visted
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)



        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r,c)
                    num+=1
        return num

