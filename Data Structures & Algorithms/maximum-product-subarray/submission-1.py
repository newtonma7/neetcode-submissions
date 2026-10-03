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
        ans = max(nums)
        currMin, currMax = 1, 1

        for n in nums:
            if n == 0:
                currMin, currMax = 1, 1
                continue

            temp = currMax * n
            currMax = max(temp, n * currMin, n)
            currMin = min(currMin * n, temp, n)
            ans = max(currMax, ans)
        
        return ans

