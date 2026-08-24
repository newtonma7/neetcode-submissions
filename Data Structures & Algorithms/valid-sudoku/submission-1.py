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
                    row =  % 
                    col =  //
            
        is there any way we can optimize it so we dont need to iterate over the same spots when doing the checks?
            if we find that the entire row and column we check contains 0 duplicates, 
                shouldnt the 3x3 contain 0 dupes as well?
                how do we achieve this?
                    still need to track that 3x3 grid structure
                We can iterate sort of inwards/diagonally and increment r and c by one each time 
                until we reach that last entry in board

        '''


        for r in range(len(board)):
            seen = set()
            for c in range(len(board[0])):
                
                if board[r][c] != "." and board[r][c] in seen:
                    return False
                seen.add(board[r][c])
        
        for c in range(len(board[0])):
            seen = set()
            for r in range(len(board)):
                if board[r][c] != "." and board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        for sq in range(len(board)):
            seen = set()
            for r in range(3):
                for c in range(3):
                    row = (sq//3) * 3 + r
                    col = (sq%3) * 3 + c
                    if board[row][col] != "." and board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True



