class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        u: multi-source bfs, 
            the cells on the border are completely safe
            so we can check all the other o's close to it 
            
        p:
            init the q with all border o cells
                bfs outward from all those cells to mark them 

            do a pass and redo all X's to O's
            redo all T's

        '''
        ROWS = len(board)
        COLS = len(board[0])
        dirs = {(1,0), (0,1), (-1,0), (0,-1)}
        visited = set()
        q = collections.deque()


        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS - 1 or
                    c == 0 or c == COLS - 1) and board[r][c] == "O":
                    q.append((r, c))
                    board[r][c] = 'T'
        
        while q:
            row, col = q.popleft()
            for dr, dc in dirs:
                nr = dr + row
                nc = dc + col

                if (nr >= ROWS or nc >= COLS 
                or nr < 0 or nc < 0 
                or board[nr][nc] == 'X'
                or board[nr][nc] == 'T'
                or (nr, nc) in visited):
                    continue
                else:
                    visited.add((nr,nc))
                    q.append((nr,nc))
                    board[nr][nc] = 'T'
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
        
        






        
        
