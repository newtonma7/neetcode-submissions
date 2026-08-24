class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        approach
            brute
                iterate and check each possible substring and in each one subtract the most
                frequent char by k to see if its violated, if it is then move on to the next substring
            sliding window
                left ptr at 0
                right ptr and end of string 
                
                hashmap represents the window and its characters
                    will use to calculate when we iterate left ptr
                left ptr will iterate when the rule is violated
                    rule is that window is only allowed to have
                    most freq char count - k > k
        '''
        l = 0
        hm = {}
        mostFreq = 0
        mx = 0

        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0) + 1
            mostFreq = max(mostFreq, hm[s[r]])
            while r-l+1 - mostFreq > k:
                hm[s[l]] = hm.get(s[l]) - 1
                l += 1
            mx = max(r-l+1, mx)
        return mx
