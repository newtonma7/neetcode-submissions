class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        backtracking with dfs
            base case: 
                we go over the target, or i is out of range
                we hit target then we take a snapshot
            iterative step:
                add or dont add but always i+1 in the dfs
            no more duplicate of the same one,just iterate array instead

            duplicate check with a set?
            need to fix the dupe issue 
            sort array since time is already ass
            while candidate is == to the one before
                increment i
            dfs as normal after 
        
        '''

        curr = []
        ans = []
        candidates.sort()

        def dfs(i, curr, total):

            if total == target:
                ans.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return


            # add the candidate
            curr.append(candidates[i])
            dfs(i+1, curr, total + candidates[i])

            #dont add the candidate

            curr.pop()
            while i < len(candidates)-1 and candidates[i+1] == candidates[i]:
                i+=1
            dfs(i+1, curr, total)

        dfs(0,curr,0)
        return ans