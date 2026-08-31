class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        u: backtrack
            no dupes so cant stay on index
            decision tree is 
            append
            include it and add it

            pop then
            exclude it and dont add it

        p:
            bc is i greater or target is over
        '''

        ans = []
        curr = []
        candidates.sort()

        def dfs(i, total):
            if total == target:
                ans.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            dfs(i+1, total+candidates[i])

            curr.pop()
            while i < len(candidates)-1 and candidates[i+1] == candidates[i]:
                i+=1
            dfs(i+1,total)

        dfs(0,0)
        return ans