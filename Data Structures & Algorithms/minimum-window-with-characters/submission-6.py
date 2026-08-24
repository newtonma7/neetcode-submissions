class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        understand:
            find an algo where we are able to find a substring of t in s including dupes
            q's: t is allowed to have dupe chars?
            ec's:
        match:
            sliding window with hashset, we can shrink the window when the set becomes valid?
        plan:
            init seen hashset representing window validity
            l ptr, r scouting ptr

        '''
        if len(s) < len(t):
            return ""

        l = 0
        mn = float('inf')
        target = {}
        window = {}
        have = 0
        need = 0
        ans = ""

        for i in range(len(t)):
            target[t[i]] = target.get(t[i], 0) + 1

        need = len(target)

        for r in range(len(s)):
            enter = s[r]
            window[enter] = window.get(enter, 0) + 1

            if enter in target and window[enter] == target[enter]:
                have += 1
            
            while have == need:
                exit = s[l]
                if r - l + 1 < mn:
                    ans = [l, r + 1]
                    mn = r - l + 1
                window[exit] -= 1
                if exit in target and window[exit] < target[exit]:
                    have -= 1
                l+=1
        return s[ans[0]: ans[1]] if mn != float("inf") else ""






        