class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        bucket sort algorithm
            create a frequency array that holds the number of elements
                need to be [0] * len
                or can we use hashmap to find num for it 
                faster lookup but less space
            index is the count
            list at each index

            once we sort the list with this algo 
            we can iterate through the hashmap and add to list then return

            create count
            iterate through nums and place nums into their proper index area


            edge cases: tie ? --> should be a list as entries
        '''

        count = [[] for i in range(len(nums)+1)]
        hm = {}
        ans = list()
        
        # {number : count}
        for nm in nums:
            hm[nm] = hm.get(nm, 0) + 1

        
        for key in hm:
            count[hm[key]].append(key)

        for i in range(len(count)-1, 0, -1):
            for curr in count[i]:
                ans.append(curr)

            if len(ans) == k:
                break

        return ans
        




        
        
        





