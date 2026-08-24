class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        backtracking with a dfs
            how do we deal with unlimited combinations?
        basecase: 
            once all the vals in nums add up to target
            append to ans and return
        iterative step:
            if sum of check is less than target
                add
            if sum of check is greater than target
                pop
        '''

        ans = []
        curr = []

        def dfs(i, curr, total):
            if i >= len(nums) or total > target:
                return
            if total == target:
                ans.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i, curr, total + nums[i])

            curr.pop()
            dfs(i+1, curr, total)

        dfs(0, curr, 0)
        return ans
        
            