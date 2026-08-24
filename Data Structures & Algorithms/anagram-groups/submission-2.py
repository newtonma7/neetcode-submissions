class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        sort trick?
        frequency table with hashmaps?
        '''

        ans = defaultdict(list)

        for word in strs:
            # create frequency array that will act as the key to the hm
            countChar = [0] * 26

            # count the characters in each word using ascii values 
            for c in word:
                countChar[ord(c) - ord('a')] += 1

            # add the word to the hashmap entry with the freq array as the key
            ans[tuple(countChar)].append(word)

        return list(ans.values())