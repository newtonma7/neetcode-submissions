class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        use a set 
            o(n) space though
        sort the array 
            o(nlogn) bc we sort the array

        fast and slow pointer?
            might be similar to linked list cycle
            slow pointer looks at i
            fast pointer looks at i+2
            
            slow, fast
            iterate through the array
            slow = i
            fast = i+1
        '''

        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2: break
        return slow
            
