class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        turn s1 in freq hashmap
        and iterate through s2 and add letters to another freq hm
            if there are enough letters to make s1, return True

        optimal strategy
            turn s1 into hashmap to create checks without ordering

            we need to traverse s2 in window sizes of s1
                and check if those windows are a permutation of s1

            while right < len(s2):
                
        '''
        hm = {}
        for char in s1:
            hm[char] = hm.get(char,0) + 1

        window = {}
        for char in s2[0:len(s1)]:
            window[char] = window.get(char,0) + 1

        if window == hm: return True

        for i in range(len(s1), len(s2)):
            charIn = s2[i]
            charOut = s2[i-len(s1)]

            window[charIn] = window.get(charIn,0) + 1
            window[charOut] = window.get(charOut) - 1

            if window[charOut] <= 0:
                window.pop(charOut)
            
            if window == hm: return True

        return False

        

        