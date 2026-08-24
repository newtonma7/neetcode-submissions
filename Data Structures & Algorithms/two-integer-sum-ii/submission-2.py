class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        left ptr on the left 
        right ptr on the right

        if nums[l] + nums[r] > target
            we iterate the right ptr so it moves to lesser num,  
        if nums[l] + nums[r] < target
            iterate left ptr so it moves to greater num
        '''

        l = 0
        r = len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]

            if numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
    
        return []
