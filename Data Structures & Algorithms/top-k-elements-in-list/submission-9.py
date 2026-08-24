class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        bucket array sort algo 

            len(nums) sized list, index represents how many times
            its appeared in the list

            approach 
                break it down instead of doing it all at once
                find frequencies, then insert into buckets
                hm to count nums
                iterate hm and insert into len(nums) list
        '''
        hm = {}
        freqs = [[] for _ in range(len(nums)+1)]
        ans = []

        for n in nums:
            hm[n] = hm.get(n,0) + 1
        print(hm)
        print(freqs)
        for key,v in hm.items():
            freqs[v].append(key)
        
        for i in range(len(freqs) - 1, -1, -1):
            if k == 0:
                break
            if len(freqs) > 0:
                for x in freqs[i]:
                    if k == 0:
                        break
                    ans.append(x)
                    k -= 1
            
        return ans