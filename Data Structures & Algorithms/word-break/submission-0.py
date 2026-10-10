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

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i +len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break

        return dp[0]
