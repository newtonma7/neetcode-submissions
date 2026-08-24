class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        frequency array/hm problem

        dict {number : # of times it appears}

        iterate through the array
            append the num to hm, increment if you have seen it already

        after we have found all # of times --> need to choose most freq ones

        with no .sort instead just find max one, then once we append it to the ans list, remove that entry
        k times ^^^ 
        
        if an element is in the hm

        '''

        hm = dict() # {num : frequency}
        ans = []

        for n in nums:
            hm[n] = hm.get(n, 0) + 1
        
        arr = []
        for num, freq in hm.items():
            arr.append([freq, num])
        arr.sort()
        
        for i in range(k):
            ans.append(arr.pop()[1])

        return ans

