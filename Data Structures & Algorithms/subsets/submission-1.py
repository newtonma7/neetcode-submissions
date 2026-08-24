class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        might need a recursive solution/dfs

        use a set to avoid duplicates

        '''

        res = []
        subset = []

        def dfs(i):
            # basecase, once i is the length of nums then we have reached the end for this path
            if i >= len(nums): 
                res.append(subset.copy())
                return
            
            # include nums in the subset
            # left branch of the decision tree
            subset.append(nums[i])
            dfs(i+1)
            
            # remove nums in the subset
            # right branch of decision tree
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res
            



