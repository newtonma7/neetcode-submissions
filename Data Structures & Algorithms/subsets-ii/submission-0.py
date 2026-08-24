class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        solution cannot contain duplicates,
            sort and while loop trick?
        
        base case: if i is out of bounds
        iterative step: increment i

        '''

        ans = []
        curr = []
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                ans.append(curr.copy())
                return
            
            # include the number
            curr.append(nums[i])
            dfs(i+1)

            curr.pop()
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1)

        dfs(0)
        return ans

