class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        u: queen can go positive diag, negative diag, up, down, left, right
            keep set for cols, pos diag, neg diag, 

            neg diag has constant r - c 
            pos diag has constant r + c

            cannot place queen if col, pos diag spot, or neg diag spot is taken
            if we place a queen, go next row

            base case:
                if invalid in any of the sets, dont place a queen/continue
                join all rows into one string

            iterative step:
            decision tree:
                place a queen, update all sets then go next row

                take a queen back, remove from all sets

        q: why dont we just add a row sets as well?
        p:
            init board with .
            iterate over all board, 
                place a queen whereever we can 
        '''

        ans = []
        board = [['.'] * n for i in range(n)]
        col = set()
        posD = set()
        negD = set()

        def dfs(r):
            if r == n:
                curr = ["".join(rows) for rows in board]
                ans.append(curr)
                return
            
            for c in range(n):
                if c in col or (r-c) in negD or (r+c) in posD:
                    continue
                
                board[r][c] = 'Q'
                col.add(c)
                posD.add(r+c)
                negD.add(r-c)
                dfs(r+1)

                board[r][c] = '.'
                col.remove(c)
                posD.remove(r+c)
                negD.remove(r-c)
                #dfs(r+1)
        dfs(0)
        return ans

