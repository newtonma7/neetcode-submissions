class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        u: dfs decision tree with a set tracking idx? or do we sort 
        p:
            base case:
                i >= len
            iterative step:
                decision tree,
                    include it
        '''
        ans = []
        curr = []
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                ans.append(curr.copy())
                return
            
            curr.append(nums[i])
            dfs(i+1)

            curr.pop()
            while i < len(nums) - 1 and nums[i+1] == nums[i]:
                i+=1
            
            dfs(i+1)

        dfs(0)
        return ans

                
