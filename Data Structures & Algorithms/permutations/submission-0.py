class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        order matters
        forwards and backwards recursion from the index youre on?
        have to include every single number

        need to answer the question, have i seen this num before?

        dfs
            basecase: 

            iterative step:
        '''

        curr = []
        ans = []
        seen = set()

        def dfs():
            if len(curr) == len(nums): 
                ans.append(curr.copy())
                return

            for num in nums:
                if num not in seen: # if the num is not already in our curr
                    curr.append(num)
                    seen.add(num)
                    dfs() # go down that path with dfs
                    
                    # we remove after we finish the dfs for that path
                    seen.remove(curr.pop())
            
        dfs()
        return ans

