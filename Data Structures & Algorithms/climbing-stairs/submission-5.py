class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        u:
        dp[i] represents the number of ways to reach the top

        choices we have at each step are
            take one step forward
            take two steps forward

        the dfs will choose between two choices to move us forward to saving an entry in dp[i]
            making progress to building state/memoization
        
        p:

        init dp array

        dfs(i)
            tracking state with index
            bc: 
                index out of bounds,
                we stop the recursion, return 0 bc it doesnt mean its valid if out of bounds

                found in the dp memo/array, no need to repeat work

            is:
                dfs forward either 1 or 2 steps, then save that entry into memo
                how does value change as we iterate and how does that exactly store?
                iteration is close to incrementing so i get it confused
        '''

        dp = [-1] * n

        def dfs(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if dp[i] != -1:
                return dp[i]
                
            dp[i] = dfs(i+1) + dfs(i+2)
            
            return dp[i]
        return dfs(0)