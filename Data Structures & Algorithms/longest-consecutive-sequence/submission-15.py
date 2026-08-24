class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        brute:
        sort and iterate nlogn time

        approach:
            set to track for o1 lookup
            iterate
                for each number iterate and see if its consecs are in
                seen
        '''

        seen = set(nums)
        ln = 1
        mx = 1

        if len(nums) == 0:
            return 0

        for i in range(len(nums)):
            curr = nums[i]
            while curr+1 in seen:
                ln+=1
                mx = max(ln,mx)
                curr+=1
            ln = 1
                
        return mx