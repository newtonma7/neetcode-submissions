class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        there are two sorted subsets of arrays now but we dont know where the pivot is
            we need to figure out which portion contains our target
        how should we compare to optimize our search?
            compare target to mid and move the boundary
        binary search
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = l + r // 2
                if mid > r and mid > target

        '''
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid

            if nums[left] <= nums[mid]:
                #this portion should be sorted and falls within target range
                if nums[left] <= target and nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[right] >= target and nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

            