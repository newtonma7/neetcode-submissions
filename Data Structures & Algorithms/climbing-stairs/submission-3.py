class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        u:
            dp[i] means the number of ways it took to get there
            at i, i can either take 1 step forward or 2 steps forward
            base case: 
            dp[1] = 1 way
            dp[2] = 2 ways
            formula : dp[i] = dp[i-1] + dp[i-2] ? holds for i=3
        p:
        '''
        cache = [-1] * n

        def dfs(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]
        return dfs(0)

