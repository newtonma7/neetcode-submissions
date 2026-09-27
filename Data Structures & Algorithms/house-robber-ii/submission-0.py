class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        u: top down memo
        circular array? 
            % len(nums)
        no longer left -> right, we can go backwards technically

        just need to check the 0 and n-1 case?
        if we rob 0, we cannot rob n-1 vice versa 

        '''
        dp = [[-1] * 2 for _ in range(len(nums))]

        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums)-1):
                return 0

            if dp[i][flag] != -1:
                return dp[i][flag]
            
            dp[i][flag] = max(dfs(i+1, flag), nums[i] + dfs(i+2, flag or (i==0)))
            return dp[i][flag]

        no0 = dfs(1, True)
        nolast = dfs(0, False)

        return max(no0, nolast)