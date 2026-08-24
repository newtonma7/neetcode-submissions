class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        hashmap with key as frequency array of the word
        {frequency table/ count of the letters : list that holds words with that count}
        have to use freq array because we cant push hm in the key area

        iterate through word list
            turn current word into freq array,
            add that word into the list at that freq array (key)
        '''

        hm = defaultdict(list)
        

        for word in strs:
            arr = [0] * 26
            for c in word:
                arr[ord(c) - ord('a')] += 1 
            hm[tuple(arr)].append(word)
            
        return list(hm.values())

