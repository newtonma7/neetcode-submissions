class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        u: dfs path
            base case:
                curr == len of digits
            iterative step:
                include current index i
                iterate index i and use that one

                exclude whatever we chose
        p:
            create mapping of number to letters

        '''
        nums = {"2": "abc", 
                "3" : "def",
                "4" : "ghi",
                "5" : "jkl", 
                "6" : "mno",
                "7" : "pqrs",
                "8" : "tuv",
                "9" : "wxyz"}

        ans = []

        def dfs(i, curr):
            if len(curr) == len(digits):
                ans.append(curr)
                return

            for j in nums[digits[i]]:
                dfs(i+1, curr + j)

                

        if digits:
             dfs(0, "") 
        else:
            return []
        return ans
            
                

