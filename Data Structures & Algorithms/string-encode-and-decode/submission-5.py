class Solution:

    
    def encode(self, strs: List[str]) -> str:
        '''
        add number length + delimiter to the start of the word
        4#neet4#code4#love3#you
        '''
        ans = ""
        for word in strs:
            ans+= str(len(word)) + "#" + word
        return ans

    def decode(self, s: str) -> List[str]:
        '''
        formula to find the string length after the delimiter
            

        loop through the string and once we find the
        '''
        ans = []
        currLen = 0
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            currLen = int(s[i:j])
            i = j + 1
            j = i + currLen
            ans.append(s[i:j])
            i = j

        return ans
                



