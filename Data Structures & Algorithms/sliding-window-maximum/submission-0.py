class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        fixxed sliding window approach
            brute
                if we do the sliding window approach, we have to iterate through each window to find the maximum
                    close to n^2 
                how do we not repeat work?
            sorting
                each window we can sort the window and append the one at k'th - 1 index
        '''

        window = []
        ans = []

        for i in range(len(nums)-k + 1):
            window = nums[i:i+k]
            window.sort()
            ans.append(window[k-1])
        return ans

