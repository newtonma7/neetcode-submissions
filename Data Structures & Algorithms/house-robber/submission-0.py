class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        u: top down
            dp[i] represents the max money path
            we can get from robbing a house

            must move left -> right

            choices:
                 rob then jump by two
                 dont rob and increment by 1
                choose whatever makes most money

            dp[i] = max(dfs(i+1), dfs(i+2))

            dfs(i)
                base case: 
                    index out of bounds
                is: 
                    checking of the dfs into other choices
                what logic do we write to determine money path
                dfs finds money,
        p:
        """
        dp = [-1] * len(nums)
        
        def dfs(i):
            if i >= len(nums):
                return 0

            if dp[i] != -1:
                return dp[i]
            
            skip = dfs(i+1)
            rob = nums[i] + dfs(i+2)
            dp[i] = max(skip,rob)

            return dp[i]
            
        return dfs(0)
            

        
