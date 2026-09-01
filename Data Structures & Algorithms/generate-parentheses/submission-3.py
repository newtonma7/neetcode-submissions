class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        u: 
            backtracking,
            must even out the number of open paren to closed paren
            keep count of open vs closed

            dec tree:
                add open
                add closed

                pop the last one regardless to backtrack
            can keep track of current state with a stack
        p:
            base case:
                open =n= closed
            iterative step:
                if open < n then we can add open
                if closed > open then we can add closed
        '''
        stack = []
        ans = []

        def dfs(opened, closed):
            if opened == n and closed == n:
                ans.append("".join(stack))
                return
            
            if opened < n:
                stack.append("(")
                dfs(opened + 1, closed)
                stack.pop()

            if closed < opened:
                stack.append(")")
                dfs(opened, closed + 1)
                stack.pop()
            
        dfs(0,0)
        return ans
