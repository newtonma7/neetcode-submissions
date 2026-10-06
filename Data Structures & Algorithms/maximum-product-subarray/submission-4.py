class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        u:
            choices:
                pick neighbor to continue
                or start a new subarray
    
            dp[i] represents the max product between index i to the end
            dfs should return the max product subarray btween i to the end
                i can represent the index? 
                or should it represent an amount lets try amount
            recurrence: max out of all candidates: dfs(i*candidate)
        '''
        mn,mx,ans = nums[0], nums[0], nums[0]


        for i in range(1,len(nums)):
            n = nums[i]
            prevMax = mx
            prevMin = mn

            mn = min(n, n*prevMax, n*prevMin)
            mx = max(n, n*prevMax,n*prevMin)
            ans = max(ans,mx)
            

        return ans

