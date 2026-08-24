class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        we need a hashmap to map the numbers to their potential letter

        dfs algo
            base case: 
                once the string we have built has hit the length of digits 
            iterative step:
                how do we iterate through the string that maps to the number to append to curr?
                use i to substring it and add it to curr
        '''
        hm = {"2" : "abc",
         "3": "def",
         "4": "ghi",
         "5": "jkl",
         "6": "mno",
         "7": "pqrs",
         "8": "tuv",
         "9": "wxyz"}

        ans = []
        curr = ""

        def dfs(i, curr):
            if len(curr) == len(digits):
                ans.append(curr)
                return

            # iterate through all the possibilties of that single digit
            # need to make recursive call for each possible choice
            for c in hm[digits[i]]:
                dfs(i+1, curr + c)
            
                

        if digits: dfs(0, curr)
        return ans