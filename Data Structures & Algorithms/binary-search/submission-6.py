class Solution:
    def search(self, nums: List[int], target: int) -> int:

        '''
        if target is less than mid --> must be on the left side of mid
            repeat search with right = mid 
            recalculate new mid 
            redo search
        if target is greater than mid
            repeat search with left = mid
            recalculate new mid
            redo search
        if target is hit
            return curr index
        '''
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = ((right - left) // 2) + left

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return -1
