class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        u: 
            choices:
                at position i in s, what dict words can start here?
            
            we are reducing the problem, into subproblems one word at a time
            what overlaps? what do we memoize?

            dfs(i) can the rest of s[i:] be segmented using words from dict?
                can i break down the suffix (i to the end) into valid sequence from dict?

            dp[i] if substring s[i:] can be segmented into valid words from dict

        s:

        '''

        dp = {}
        
        def dfs(i):
            if i == len(s):
                return True

            if i in dp:
                return dp[i]

            for w in wordDict:
                if s[i:i+len(w)] == w:
                    if dfs(i + len(w)):
                        dp[i] = True
                        return True
            dp[i] = False
            return dp[i]

        return dfs(0)
                 
