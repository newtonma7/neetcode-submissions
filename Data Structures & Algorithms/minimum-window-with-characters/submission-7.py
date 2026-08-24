class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        understand: need to find an algo to grab the shortest substring window
        in s that exists in t
        q:
        ec: t longer than s, empty string for either
        match: expanding sliding window problem
        plan:
        once our substring/window representation is valid, shrink the window on the left
            use have and need to find out then reeval
        approach, 
            init hm for representation of t
            init hm for window
            have and need var to check hm
            init need as hm len, have 0
            init shortest []
            left ptr, 0 for s

            loop s, 
                add to window, check if we can increment have, if it is then we check if its enough for need
                
                rule violation VV
                while have < need:
                    increment l
                    reevaluate shortest
                    decrement from have if its in hm
        '''

        if len(t) > len(s):
            return ""

        counts = {}
        window = {}
        ans = ""
        shortest = float('inf')
        l, have = 0, 0

        for c in t:
            counts[c] = counts.get(c, 0) + 1

        need = len(counts)

        for r in range(len(s)):
            curr = s[r]
            window[curr] = window.get(curr,0) + 1

            if curr in counts and window[curr] == counts[curr]:
                have += 1
            
            while have == need:
                exit = s[l]
                window[exit] -= 1
                if exit in counts and window[exit] < counts[exit]:
                    have -= 1
                if r - l + 1 < shortest:
                    ans = s[l:r+1]
                    shortest = r - l + 1
                l+=1
        return ans



        