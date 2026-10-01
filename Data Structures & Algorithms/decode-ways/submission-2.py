class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        u: 
            dp[i] represents number of ways to decode 
            at suffix starting at index i


            dfs finds the number of ways to decode the suffix
                need index for that so we compute the suffix,
                then logic for decode?

                how do we determine the number of mappings from
                suffix?
                    1012
                    2 represents one mapping

                    12 represents another
                    1 2 represents another

                    1 char represents a decode,
                    reuse that to determine the next one?

                one num represents a character, so that can be our
                base case?
        m:  
            init dp array

            dfs(i)
                compute suffix
                len 1 represents a mapping

        '''

        dp = [-1] * len(s)

        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if dp[i] != -1:
                return dp[i]

            ways = dfs(i+1)
            if i+1 < len(s) and int(s[i:i+2]) >= 10 and int(s[i:i+2]) <= 26:
                ways += dfs(i+2)

            dp[i] = ways
            return dp[i]

        return dfs(0)