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

        slow = nums[0]
        fast = nums[nums[0]]

        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow2 = 0
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow
            
