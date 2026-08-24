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
            deque
            monotonic decreasing queue

        '''

        q = deque()
        l = 0
        ans = []

        for r in range(len(nums)):
            while q and nums[r] > q[-1]:
                q.pop()
            q.append(nums[r])

            # window size is now valid 
            if r - l + 1 >= k:
                ans.append(q[0])
                if nums[l] == q[0]:
                    q.popleft()
                l += 1
        return ans
        


        

