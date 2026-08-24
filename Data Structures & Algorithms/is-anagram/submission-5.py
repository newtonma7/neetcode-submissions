class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Hashmap as a frequency array
        can use one for better memory space with increment decrement trick

        if not same len --> false

        iterate through the first string and add the characters with their count in the hm
            if char is not in hashmap create the key with default val 0

        iterate through the second string and decrement the key values 



        

        iterate 

        '''

        hm = dict()

        for char in s:
            hm[char] = hm.get(char, 0) + 1

        for char in t:
            if char not in hm:
                return False
            else:
                hm[char] = hm.get(char)-1

        for val in hm.values():
            if val != 0:
                return False
        return True
        
        
        


    

        