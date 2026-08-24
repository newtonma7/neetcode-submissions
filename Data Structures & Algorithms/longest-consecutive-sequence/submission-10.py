class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        input: array of nums
        output: number of consecutive nums
        edge cases: 

        approach

        add all nums to a hashset { number : count}
        iterate the hashmap and check if the number before it exists
        if it does then we can increment the count
        '''

        s = set(nums)
        mx = 0
        
        # find the lowest num, start of the sequence and count up
        for key in s:
            if key - 1 not in s:
                length = 1
                while length + key in s:
                    length+=1
                mx = max(length, mx)
            
        return mx


