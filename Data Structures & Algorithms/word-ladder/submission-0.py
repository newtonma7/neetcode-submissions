class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        u: need to turn begin word to end word, 
            one character change at a time
            must return minimum turns to change start to end word

            how do we represent relationships between words
            graph -> what do edges represent

            adj list where the key is a word with 1 wildcard
            the value is the neighbors it has so we can 
            add neighbors to the q and explore their paths
        p:

        '''
        adj = defaultdict(list)
        q = collections.deque([beginWord])
        visited = set([beginWord])
        ans = 1

        if endWord not in wordList:
            return 0

        wordList.append(beginWord)

        for w in wordList:
            for idx in range(len(w)):
                wildcard = w[:idx] + "*" + w[idx + 1:]
                adj[wildcard].append(w)

        while q:
            for i in range(len(q)):
                curr = q.popleft()

                if curr == endWord:
                    return ans
                
                for idx in range(len(curr)):
                    wildcard = curr[:idx] + "*" + curr[idx + 1:]
                    for w in adj[wildcard]:
                        if w not in visited:
                            q.append(w)
                            visited.add(w)
            ans+=1
        return 0

