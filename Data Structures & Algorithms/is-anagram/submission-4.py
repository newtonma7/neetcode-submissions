class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        hashmap as a frequency table
        iterate first word
            first add letter into hashmap with count 1
            if letter in hm already, increment its count 
            doesnt need if statement can just search with value

        iterate through second word
            if recognize letter --> decrement count by 1
            if no recognize letter in hm then return false

        iterate through hm final time
            all counts should be 0
            
        '''
        d = dict()

        if len(s) != len(t):
            return False;

        for letter in s:
            d[letter] = d.get(letter,0)+1

        for letter in t:
            if letter not in d:
                return False
            d[letter] = d.get(letter)-1

        for val in d.values():
            if val != 0:
                return False

        return True


    

        