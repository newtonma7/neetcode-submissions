class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        u: 
            we want min cost to past last idx of the array
            cost[i] represents cost of taking step from ith floor
                so in dp[i] can represent the min cost to reach i
            choices are, 
                we can go to the i+1 step or i+2 step
            base case:
                cost at 0 idx
                cost at 1 idx

            
            dp[i] = cost at i + min(cost of dfs(i+1), cost of dfs(i+2))
        p:
        '''
        dp = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0

            if dp[i] != -1:
                return dp[i]
            
            dp[i] = cost[i] + min(
                dfs(i+1), 
                dfs(i+2)
            )
            return dp[i]

        return min(dfs(0), dfs(1))
