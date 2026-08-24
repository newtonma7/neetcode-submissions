class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        dfs
            build a string from dfsing from a square
            base case:
                string equals the target
                string exceeds curr len
            iterative step:
                go in any of the 4 directions and add that character
                how to check if we have visited that square already?
        '''
        ROWS = len(board)
        COLS = len(board[0])
        seen = set()

        def dfs(k, i, j):
            if k == len(word):
                return True
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or word[k] != board[i][j] or (i,j) in seen:
                return False

            seen.add((i,j))
            res = dfs(k+1, i + 1, j) or dfs(k+1, i - 1 , j) or dfs(k+1, i, j + 1) or dfs(k+1, i, j - 1)
            seen.remove((i,j))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c):
                    return True
        return False