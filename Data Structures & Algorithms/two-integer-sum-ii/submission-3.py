class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        left and right pointers
        left at 0
        right at the end
        iterate pointer based off of comparing sum to target
            if target is bigger, iterate left ptr
            if target is less, iterate right ptr
        '''
        l = 0
        r = len(numbers) - 1

        while l < r:
            curr = numbers[l] + numbers[r]
            if curr == target:
                return [l+1,r+1]
            elif curr < target:
                l+=1
            elif curr > target:
                r-=1
        return [0,0]


