class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        understand:
            find an algo that cam replace k amount of chars in the substring
            and then check length
            q's:
            ec:
        match:
            sliding window with hashmap to keep count 
        plan: 
            approach:
            init hm to keep count, track the most freq char with variable
            hm represents current window
            scouting ptr char gets added but once violated, increment left and pop it/rmv
                reeval most freq char and check max length at every add
            rule: we must redo the window if k < window length - most freq count
           

        '''

        hm = {}
        mostfreq = 0
        mx = 0
        l = 0

        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r],0) + 1
            if hm[s[r]] > mostfreq:
                mostfreq = hm[s[r]]
            while k < (r - l + 1) - mostfreq:
                hm[s[l]] -= 1
                l+=1
            mx = max(mx, r - l + 1)
        return mx
