class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        understand: need to find duplicate number, 
        all integers are in range 1-n (so we can use values as an index)
        match: fast and slow pointer here
        plan:
        fast and slow pointer technique so we can find the start of the cycle,
        from there we can walk from the start of the cycle to land on the duplicate 
        and iterate slow and slow2 to find
        '''
        slow = 0
        fast = 0
        
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        
        slow2 = 0

        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow