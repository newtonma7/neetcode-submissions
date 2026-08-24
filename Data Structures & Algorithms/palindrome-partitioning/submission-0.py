class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        dfs into the decision tree
            cut the string up and track current partitions
            try every possible cut in s
        '''

        ans = []
        curr = []

        def dfs(i):
            if i >= len(s):
                ans.append(curr.copy())
                return
            
            for j in range(i, len(s)):
                currStr = s[i:j + 1]
                if currStr == currStr[::-1]:
                    curr.append(currStr)
                    dfs(j + 1)
                    curr.pop()
                 
        dfs(0)
        return ans