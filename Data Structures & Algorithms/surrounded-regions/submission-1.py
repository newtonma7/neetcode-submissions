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


        for i in range(COLS):
            if board[0][i] == 'O': # first row
                visited.add((0,i)) 
                q.append((0,i))
                board[0][i] = 'T'
            if board[ROWS-1][i] == 'O': # last row
                visited.add((ROWS-1,i))
                q.append((ROWS-1,i))
                board[ROWS-1][i] = 'T'

        for i in range(ROWS):
            if board[i][0] == 'O': # first col
                visited.add((i,0))
                q.append((i,0))
                board[i][0] = 'T'
            if board[i][COLS-1] == 'O': # last col
                visited.add((i,COLS-1))
                q.append((i,COLS-1))
                board[i][COLS-1] = 'T'
        
        while q:
            row, col = q.popleft()
            for dr, dc in dirs:
                nr = dr + row
                nc = dc + col

                if (nr >= ROWS or nc >= COLS 
                or nr < 0 or nc < 0 
                or board[nr][nc] == 'X'
                or board[nr][nc] == 'T'
                or board[nr][nc] in visited):
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
        
        






        
        
