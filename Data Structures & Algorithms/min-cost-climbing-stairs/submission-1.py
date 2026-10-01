class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        u:
            top down 
            dp[i] needs to store the MIN cost to reach the end from
                ith floor
                pay the current cost of the i'th floor then make the
                choices
            dfs determines cost to get to the end from i'th floor

            choices:
                step forward 1 or 2
            subproblems overlapping,
                we store precomputed costs into the dp array
        p: 
            dfs(i)
                bc: 
                    pass last idx, ret 0
                    memoized, ret memo
                is: 
                    incur cost + dfs toward two choices

        '''
        dp = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = cost[i] + min(dfs(i+1),dfs(i+2))
            return dp[i]
        return min(dfs(0),dfs(1))