class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        sliding window
            not fixxed window, sorta combination of both

            we need a hashmap of all the characters in t
                can have duplicates

            two conditions to save the window to ans
                every character needs to be in that window
                window needs to be shorter than current min

            min window size is 
                valid window will be equal or greater than the len t

            we start with window of size t and then from there shrink and expand?

            what are the conditions for shrinking?
                when the window turns valid, shrink window till invalid
                    save ans in each shrink

            valid window when
        '''
        tmap = {}
        window = {}
        have = 0
        res = [-1,-1]
        resLen = float("infinity")
        
        if t == "": return ""

        for c in t:
            tmap[c] = tmap.get(c, 0) + 1
        
        need = len(tmap)
        l = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0) + 1

            if s[r] in tmap and window[s[r]] == tmap[s[r]]:
                have += 1

            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in tmap and window[s[l]] < tmap[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""
            

                




                

            



            
        


