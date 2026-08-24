class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        input: 2d array
        output: true or false if the rules are not broken
        edge cases:
            in the 3x3 case, we are allowed to have empties, just no dupes

        use hashsets to check for duplicates --> o(1) lookup time
            row set
            col set
            current 3x3 set

        brute force:
            iterate over each row and check if there are duplicates
            iterate by column and check if there are duplicates
            iterate by 3x3 grid to check duplicates
                iterate by grid is going to be
                    row =  square % 3  * 3 + r
                    col =  square // 3 * 3 + c


        '''
        #in these hashsets {row/col/square ID: set}
        rows = defaultdict(set) 
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if board[r][c] == ".":
                    continue
                if curr in rows[r] or curr in cols[c] or curr in squares[(r//3,c//3)]:
                    return False
                rows[r].add(curr)
                cols[c].add(curr)
                squares[(r//3, c//3)].add(curr)
        return True
                

        



