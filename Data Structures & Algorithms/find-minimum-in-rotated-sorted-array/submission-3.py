class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        we only receive the rotated array in nums


        rotating the array creates two subsets of sorted arrays
            the min is the first element in the right subset

        
        binary search to find this cut
            left = 0
            right = len(nums) - 1
            mid = left + right // 2

            how should we update left and right pointers to find the cut?
                we dont have a target num, so we should use the left and right pointers to find the cut
                    what comparisons do we do?
                    what step do we take to move closer to that goal?
            if our right ptr is > mid
                right = mid -1
            if our right ptr is <= mid
                left = mid + 1
                
            
        '''
        left = 0
        right = len(nums) - 1
        

        while left < right:
            mid = (left + right) // 2
            if nums[right] > nums[mid]:
                right = mid
            elif nums[right] <= nums[mid]:
                left = mid + 1
        return nums[right]