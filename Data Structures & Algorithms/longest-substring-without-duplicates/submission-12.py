class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        understand:
            find an algo to get the length of continuous substring
            where there are no dupe chars
            q's: how do we track the window? what variables do we need to begin?
            ec: len 0, all dupes, no dupes
        match:
            sliding window with a set for o(1) look for dupes
        plan:
            init left ptr = 0
            init set
            loop with r 
                if we find a character in the set (scouting ptr), 
                iterate the left ptr till its not violating anymore
                then check for new max?
        '''
        l = 0
        mx = 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            mx = max(mx, len(seen))
        return mx
            