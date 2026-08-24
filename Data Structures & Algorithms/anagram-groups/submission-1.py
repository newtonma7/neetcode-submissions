class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        sort trick?
        frequency table with hashmaps?
        for each word create a new list inside of an array
            turn curr word into hm frequency table

            use the decrement trick instead of creating multiple hm
            maintain freq of letters of curr word
                iterate to next word
                    iterate letters of word 
                        if letter not in hm, break early
                        if letter is in, decrement
                        loop thru hm to ensure count is 0
                        if checks then add to list
            this is so many loops ^^

        special cases
            empty
            one input
        '''

        ans = defaultdict(list)

        if len(strs) == 0:
            return [[""]]
        
        if len(strs) == 1:
            return [[strs[0]]]


        for word in strs:
            # create frequency array that will act as the key to the hm
            countChar = [0] * 26

            # count the characters in each word using ascii values 
            for c in word:
                countChar[ord(c) - ord('a')] += 1

            # add the word to the hashmap entry with the freq array as the key
            ans[tuple(countChar)].append(word)

        return list(ans.values())