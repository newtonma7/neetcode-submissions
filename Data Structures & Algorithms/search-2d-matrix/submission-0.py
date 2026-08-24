class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        left, right, mid
        how do we translate 1d binary search to 2d?
        
        flatten out 2d array and pretend it is 1d
        use // and % on the flattened index to find the proper row and col


        '''
        ROW, COL = len(matrix), len(matrix[0])

        left = 0
        right = ROW * COL - 1

        while left <= right:
            mid = (left + right) // 2
            midI = mid // COL
            midJ = mid % COL

            curr = matrix[midI][midJ]
            if curr < target:
                left = mid + 1
            elif curr > target:
                right = mid - 1
            else:
                return True
        return False



