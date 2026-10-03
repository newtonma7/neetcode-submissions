class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        u: 
        what is the smallest num of coins we need to create target? 
        
        choices:
            pick i'th coin
            dont pick i'th coin and pick another one
        
        dp[i] represents the min amount of coins to represent an amount i
        dfs should return the min amount of coins to rep amount i 
            have the logic to calculate number of coins,

        overlap: some dfs will overlap because you'll use some combination of calls
            to find the num of coins it takes to make the num

        recurrence: dp[i] = min(dfs(i+1), nums[i] + dfs(i+2))

        p:
            init dp array
            
            def dfs(i)
                bc:
                    idx out of bounds, we ran out of coins to check
                    memo'd
                    do we check if val exceeds?
                is:
                    recurrence above
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
                candidate = 1 + dfs(i+coin)
                dp[i] = min(best, candidate)
                best = dp[i]

            return dp[i]
        
        if dfs(0) == float('inf'):
            return -1
        return dfs(0)

