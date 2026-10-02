class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        u:
            want the max amount of money we can rob 
            but we cant rob any two houses in a row (i-1) or (i+1)

            choices:
                rob or skip

            dp[i] represents the max amount of money we can have stored
            in the i'th position after exploring both the choices of 
            rob or dont rob
            

            dfs needs to find total amount of the choice path, rob or skip
                rob would jump two positions and take the money
                skip just looks at the next one 

            we reduce into subproblems by exploring the skip or rob paths
            for each i'th position
        p:

        init dp array for memo

        dfs(i)
            bc: 
                index oob
                memoized alr
            is:
                our choices are
                    skip or rob
                    if we rob, we take money and have to skip
                    if we skip, just increment and explore
        '''

        dp = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]

            dp[i] = max(dfs(i+1), nums[i] + dfs(i+2))

            return dp[i]
        return dfs(0)