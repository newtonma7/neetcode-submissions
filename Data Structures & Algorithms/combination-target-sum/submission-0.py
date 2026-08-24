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
        index = 0

        def dfs(i, check, target):
            if i >= len(nums) or sum(check) > target:
                return
            if sum(check) == target:
                ans.append(check.copy())
                return

            check.append(nums[i])
            dfs(i, check, target)

            check.pop()
            dfs(i+1, check, target)

        dfs(0, curr, target)
        return ans
        
            