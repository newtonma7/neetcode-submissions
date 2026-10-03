class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        choices are
            pick any coin

        dp[i] represents the min amount of coins to get an amount i 
        from i to the end
        dfs should return min amount of coins to get amt i
        recurrence 
            i doesnt represent index, it represents the amount of money we
            need to check how many coins it represents
        '''

        dp = [-1] * amount

        def dfs(i):
            if i > amount:
                return float('inf')
            if i == amount:
                return 0

            if dp[i] != -1:
                return dp[i]
            
            best = float('inf')
            for coin in coins:
                candidate = 1 + dfs(i + coin)
                dp[i] = min(best, candidate)
                best = dp[i]
            return dp[i]
        if dfs(0) == float('inf'):
            return -1
        return dfs(0)