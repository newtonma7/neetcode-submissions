class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
        number then delim
        4#
        number represents the length to substring out as we iterate
        '''

        ans = ""
        for s in strs:
            ans +=  str(len(s)) + "#" + s
        return ans

    def decode(self, s: str) -> List[str]:
        '''
        our input will be one long string with a delim 
        of #(length of substring to slice)

        approach
        
        we want two indices to track when we finish substringing
        when we see a #, 
        grab the number right after it --> what if its double digit
            will a number always be after the #?
                no
                how do we approach this, look ahead?
                while loop?
                #10

            use while loops
            with two indices
                i,j
            i iterates till we hit the delim
            j starts iterating to grab the entire len,
            once we finalize the len
                chunk it with substring, move j ahead
            i=j
            continue
        '''
        ans = []
        ln = 0
        i = 0
        j = 0

        while j < len(s):
            if s[j] == "#":
                ln = int(s[i:j])
                ans.append(s[j+1:j+1+ln])
                i = j + 1 + ln
                j = i
            j += 1
        return ans
