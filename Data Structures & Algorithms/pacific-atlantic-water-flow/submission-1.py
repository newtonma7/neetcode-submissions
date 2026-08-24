class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        input: grid of heights
        output: all indices where water flows from one to the other

        set that tracks the cells we are building

        notice that the corner cells in the top right and the bottom left
            always flow to the atlantic and the pacific

        we can dfs from the borders and build a path
            check if the surrounding cells are greater than the corner ones
                dfs into that cell
        '''

        pac = set()
        atl = set()
        ROWS = len(heights)
        COLS = len(heights[0])
        res = []

        def dfs(r,c, visit, prev):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or (r,c) in visit or prev > heights[r][c]:
                return
            currPos = heights[r][c]
            visit.add((r,c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            
        
        for c in range(COLS):
            dfs(0,c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS-1])

        return list(pac & atl)


