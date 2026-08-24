class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        fast and slow pointer method
            iterate the fast pointer fast ptr times till it meets the slow,
                to find the start of the cycle
            then iterate it slow times and you will land on the dupe

        marking method
            since all values of nums are valid indices,
                we can traverse each num (idx)
                mark it as negative 
                if we find its already negative, we can return the prev idx we used
        '''
        fast = 0
        slow = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        
        # we are now at the start at the cycle, we can iterate by
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow


