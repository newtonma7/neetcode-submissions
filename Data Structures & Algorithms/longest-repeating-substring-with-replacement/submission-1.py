class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        sliding window
            left = 0
            right = i in for loop
            seen = hm {char : count}

            1 by 1 add each char in string into the window and add it to the seen dict
                if append to the hm and the number of characters > k
                    shrink and remove from hm and window until k is satisfied
                        while all the other characters other than the most frequent one are greater than k
                            how do we find out what is the current most frequent char?
        '''

        left = 0
        seen = dict()
        most = 0
        mostFreq = 0

        for i in range(len(s)):
            seen[s[i]] = seen.get(s[i], 0) + 1
            mostFreq = max(seen[s[i]], mostFreq)

            while (i-left+1) - mostFreq > k: 
                seen[s[left]] = seen.get(s[left]) - 1
                if seen[s[left]] <= 0:
                    seen.pop(s[left])
                left +=1

            most = max(i - left + 1, most)

        return most
            