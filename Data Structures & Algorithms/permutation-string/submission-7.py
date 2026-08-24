class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        input: s1 and s2
        output: boolean indicator of if s1 is in s2
        problem: how do we check that s1 is in s2?

        approach
            brute 
                check every substring of size s1 in s2 and see if it matches with hashmap count
            sliding window
                initialize the sliding window in s2 of size s1
                hashmap will represent that window
                use left ptr to pop out that char and iterate our window
        '''
        check = {}
        window = {}

        for char in s1:
            check[char] = check.get(char,0) + 1

        for char in s2[0:len(s1)]:
            window[char] = window.get(char, 0) + 1

        l = 0

        if check == window: return True

        print(window)
        # start at +1 window size
        for r in range(len(s1), len(s2)):
            window[s2[l]] = window.get(s2[l]) - 1
            if window[s2[l]] == 0:
                window.pop(s2[l])
                
            l += 1

            window[s2[r]] = window.get(s2[r], 0) + 1

            if check == window:
                return True
        
        return False

