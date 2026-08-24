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
        
        for key in s:
            if key + 1 in s:
                continue
            else:
                currKey = key
                count = 0
                while currKey in s:
                    currKey -= 1
                    count +=1
            mx = max(count, mx)
        return mx


