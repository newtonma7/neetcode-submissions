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
        if n <= 2:
            return n
            
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]