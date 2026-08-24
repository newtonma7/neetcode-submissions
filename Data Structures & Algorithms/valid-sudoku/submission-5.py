class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        no duplicates, we can use 3 hashsets for row, cols, and the current square
        
        how to get square index?
            row index / 3 is square index
            translates into 0, 1 , 2

            col index is col idx / 3 as well
        
        use default dict to have each entry in hashmap be 
            row num : values in that row

        we then check that list in that row
        
        approach:

        we must iterate and check each row, 

        iterate and check each co

        then iterate and check each square
            iterate as normal but divide row index to translate into which square it is
        
        is it possible to do one pass?

        '''

        ROWS = len(board)
        COLS = len(board[0])

        rset = defaultdict(set)
        cset = defaultdict(set)
        sset = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rset[r] or board[r][c] in cset[c] or board[r][c] in sset[(r//3,c//3)]:
                    return False
                rset[r].add(board[r][c])
                cset[c].add(board[r][c])
                sset[(r//3, c//3)].add(board[r][c])

        return True
                


