class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        understand:
            find an algo to check substrings 
            that equate to the same char count in one string as the other
            q's: s1 always less in len? repeat chars?
            ec's:
        match:
            fixxed size sliding window in s2 and check across from s1 
            with hashmaps to keep track of char count
        plan:
            transform s1 into a hashmap,
            window on s2 starting at len of s1,
                init into hm and check s1 hm
            if no match, then iterate l and r ptr by one to iterate entire window
        '''
        if len(s2) < len(s1):
            return False
        hm1 = {}
        hm2 = {}

        for i in range(len(s1)):
            hm1[s1[i]] = hm1.get(s1[i], 0) + 1
            hm2[s2[i]] = hm2.get(s2[i], 0) + 1
        
        if hm1 == hm2:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            enter = s2[r]
            exit = s2[l]

            hm2[exit] -= 1
            if hm2[exit] == 0:
                hm2.pop(exit)
            hm2[enter] = hm2.get(enter, 0) + 1

            if hm1 == hm2:
                return True
            l+=1

        return False
            
