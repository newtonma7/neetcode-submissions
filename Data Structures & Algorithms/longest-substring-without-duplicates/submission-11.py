class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        input: string to check for longest substring
        output: size of largest substring
        edge cases: 0 char, 1 char

        left pointer + right ptr trick
        sliding window
        left ptr at 0 
        right ptr at 1

        set that represents current window

        max var to check window size on every iteration

        increment right ptr then check window
            if window is violated, shrink window on left ptr side 
            and pop from the set
        '''

        l = 0
        mx = 0
        window = set()

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l]) 
                l += 1

            window.add(s[r])
                
            mx = max(mx, r - l + 1)

        return mx

        