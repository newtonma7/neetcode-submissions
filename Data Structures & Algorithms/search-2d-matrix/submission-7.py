class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        flatten the array
        '''
        ROWS = len(matrix)
        COLS = len(matrix[0])
        l = 0
        r = ROWS * COLS - 1

        while l <= r:
            mid = (l + r) // 2
            midR = mid // COLS
            midC = mid % COLS

            curr = matrix[midR][midC]
            if target < curr:
                r = mid - 1
            elif target > curr:
                l = mid + 1
            else:
                return True
        return False
