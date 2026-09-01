class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        u: dfs the decision tree for backtracking
        p:
            base case: 
                curr is same len as nums

            iterative step:
                we want to add the num if we havent included it in our curr yet
                can use a set for o1 lookup

                exclude it in the backtrack
        '''
        curr = []
        seen = set()
        ans = []

        def dfs():
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            
            for num in nums:
                if num not in seen:
                    seen.add(num)
                    curr.append(num)

                    dfs()

                    seen.remove(curr.pop())
                    
            
        dfs()
        return ans
