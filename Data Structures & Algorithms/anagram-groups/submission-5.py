class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        any order, all lower, 

        approach
            hashmap where each key is the frequency array of the word
            iterate through each word, and then turn it into a freq array
            then just add it to the hashmap, if the freq array already exists
            it'll just be added anyways
        '''

        hm = defaultdict(list)
        ans = []
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord('a') - ord(c)] += 1
            hm[tuple(freq)].append(s)
        
        for v in hm.values():
            ans.append(v)
        return ans