class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        u:

            choices are:
                include/exclude this number

            dp[(i,currsum)] represents is it possible to reach target from
            i and currsum with elements in array from i to the end

            partitions are not contiguous

            dfs(i, currsum) -> can we reach target with 
            current sum and the rest of the array?

        p:
        
        '''

        dp = {}

        total = sum(nums)
        
        if total % 2 == 1:
            return False

        target = total // 2

        def dfs(i,currSum):
            if currSum == target:
                return True
            
            if currSum > target or i >= len(nums):
                return False
            
            if (i, currSum) in dp:
                return dp[(i,currSum)]
            
            dp[(i,currSum)] = dfs(i+1, currSum) or dfs(i+1, currSum+nums[i])

            return dp[(i,currSum)]
        
        return dfs(0,0)

            

            
