class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        frequency array/hm problem

        dict {number : # of times it appears}

        iterate through the array
            append the num to hm, increment if you have seen it already

        after we have found all # of times --> need to choose most freq ones

        ###
        bucket sort algo

        hm {count : values (list)}
        freq array [] up to size of input array
            index is the count
            entry is the list of values that hold that count

        iterate thru once with a hm to compile values and frequencies

        --> populate the frequency array
        iterate through the hm and put in the value at the counts array index

        -->
        then iterate through the freq array 
        and once the ans array reaches enough values then return
        '''
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        ans = []
        
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for num, cnt in count.items():
            freq[cnt].append(num)

        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
            


        
        
        





