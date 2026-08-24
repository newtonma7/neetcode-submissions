class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        backtracking?
            we want all valid permutations of the parenthesis with n pairs
            what makes a well-formed parentheses string?
                all open ones are closed
                we can use a stack to generate the valid parenthesis?
            
            at each step we choose to close or to not close the current parenthesis
                allowed to insert as long as we have not exceeded n
                if we close, decrement n by 1 --> one valid pair is out

                we are allowed to close if there are open parenthesis


            stack work?
                
        '''

        ans = []

        def dfs(opened,closed,currStr):
            curr = ""
            if opened == 0 and closed == 0:
                ans.append(currStr)
                return
            
            if opened > 0:
                dfs(opened - 1, closed, currStr + "(")

            if closed > opened:
                dfs(opened, closed - 1, currStr + ")")

        dfs(n,n,"")
        return ans

            



