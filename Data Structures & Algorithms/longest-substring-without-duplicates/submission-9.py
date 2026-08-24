class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        have a set to identify duplicates that resets upon window reset
        
        loop through str
            add letters 1 by 1
            add the letter to the set
            increment our counter
            if we encounter a duplicate by checking the set
                reset the window and but maintain position in str
                reevaluate the max
                continue to iterate the rest of str
        '''
        


        seen = set()
        longest = 0
        l = 0

        if len(s) == 1:
            return 1

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            longest = max(longest, r - l + 1)

        return longest
            
