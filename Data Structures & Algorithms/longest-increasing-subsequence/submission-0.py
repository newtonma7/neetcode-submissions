class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        u:
            dp[i] represents the longest increasing subseq from index i to the end
            dfs(i) should represent the length of the longest increasing subseq from index i

        p:
        '''

        dp = [-1] * len(nums)


        def dfs(i):
            if i >= len(nums):
                return 0
            
            if dp[i] != -1:
                return dp[i]

            LIS = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS = max(1+dfs(j), LIS)

            dp[i] = LIS
            return dp[i]

        return max(dfs(i) for i in range(len(nums)))
