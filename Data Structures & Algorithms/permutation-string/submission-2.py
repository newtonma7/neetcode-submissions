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
        if len(s2) < len(s1):
            return False

        

        hm = {}
        for char in s1:
            hm[char] = hm.get(char,0) + 1

        left = 0
        right = len(s1)

        while right <= len(s2):
            window = s2[left:right]
            comp = {}

            for char in window:
                comp[char] = comp.get(char,0) + 1

            if comp == hm: return True
            left +=1
            right +=1

        return False

        

        