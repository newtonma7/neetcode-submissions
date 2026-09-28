class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        u:
            hm[i] represents the length longest substring
            for starting the cut at that index

            choices?
                seems like we should just check that path?
                then scan the max at the end 

        p:
            dfs
                bc:
                    memoized
                    index out of bounds
                is:
                    iterate all cuts with i:j
                    if find palindrome
                        store the max for that tuple,
                        how do we actually calculate the length?
                        hm[(i,j)] = max(dfs(i:j), j - i + 1)
        '''
        ans = ""

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > len(ans):
                    ans = s[l:r+1]
                l -= 1 
                r += 1
            
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > len(ans):
                    ans = s[l:r+1]
                l -= 1 
                r += 1
        return ans

    