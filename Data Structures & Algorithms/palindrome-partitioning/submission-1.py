class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        u:
            cut up s into every substring combo and determine if palindrome

            dfs decision tree,
                i and j
        p:
        '''
        ans = []
        curr = []

        # decision tree is
        # is this valid palindrome?
        #   build on it and explore this cut/path
        #   go back
        # we can try each substring partition of s
        def dfs(i):
            if i >= len(s):
                ans.append(curr.copy())
                return

            for j in range(i, len(s)):
                currStr = s[i:j+1]
                if currStr == currStr[::-1]:
                    curr.append(currStr)
                    dfs(j+1) # continue down this path,found valid palindrome
                    curr.pop()
        dfs(0)
        return ans