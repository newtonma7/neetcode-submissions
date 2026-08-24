class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        default dict set for rows and cols,
        but what about squares
        need to index the 9 squares into its own thing
        use % and /

        
        '''
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqs = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                curr = board[r][c]
                if curr == ".":
                    continue
                if curr in rows[r] or curr in cols[c] or curr in sqs[(r//3, c//3)]:
                    return False
                rows[r].add(curr)
                cols[c].add(curr)
                sqs[(r//3, c//3)].add(curr)
        return True