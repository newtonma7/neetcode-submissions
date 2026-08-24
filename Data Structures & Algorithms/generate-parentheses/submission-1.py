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

                we are allowed to close if there are open parentheses
                if closed < opened we can add closing paren


            stack work?
                
        '''

        ans = []
        stack = []

        def dfs(opened,closed):
            if opened == n and closed == n:
                ans.append("".join(stack))
                return
            
            if opened < n:
                stack.append("(")
                dfs(opened+1, closed)
                stack.pop()
            
            if closed < opened:
                stack.append(")")
                dfs(opened,closed+1)
                stack.pop()

        dfs(0,0)
        return ans

            



