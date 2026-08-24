class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        sort and then 
        iterate

        hashset approach
            how can a hashset help us here?
            if we have found a num before in s, then 
        '''

        s= set(nums)
        streak = 0

        for num in s:
            if num - 1 in s: # if we see a smaller num already in the set
                continue    # no need to try to find it because we should have already counted that streak
            else: # if we havent seen that number yet, we should iterate it all the way down
                curr = 0
                while num in s:
                    curr+=1
                    streak = max(streak,curr)
                    num +=1
        return streak


        
