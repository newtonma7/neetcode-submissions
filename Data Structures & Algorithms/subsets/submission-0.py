class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        might need a recursive solution/dfs

        use a set to avoid duplicates

        '''

        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)

        dfs(0)
        return res
            



