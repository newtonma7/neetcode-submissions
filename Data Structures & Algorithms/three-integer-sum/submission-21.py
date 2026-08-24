class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        target is 0
        keep ONE fixed and iterate two
        need to do duplicate checks, 
            i shouldn't redo something j already did
            k needs to avoid j and i 
        which ptrs do we iterate in which cases?
        it isnt sorted by default, so sort it

        approach
            init i, j, then k at the end,
            while i < k 

        '''
        nums.sort()
        ans = []

        i = 0
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums) - 1
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if curr < 0:
                    j+=1
                elif curr > 0:
                    k -= 1
                elif curr == 0:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while j < k and nums[j-1] == nums[j]:
                        j+=1
        return ans
