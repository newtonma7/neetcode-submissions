class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        sort the input array

        left pointer on idx 0 
        curr pointer on left + right // 2
        right pointer on len - 1

        left + right
        while left < right
            while left < mid and mid < right
                if l + r + m < 0 then
                    curr pt ++
                if l + r + m > 0 then
                    curr pt --
                if target hit then append
            left ++ 
            right --
            recalc new mid
        '''

        ans = []

        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            j = i + 1
            k = len(nums) - 1
            while j < k:
                curr = nums[i] + nums[k] + nums[j]
                if curr < 0:
                    j += 1
                elif curr > 0:
                    k -= 1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while nums[j] == nums[j -1] and j < k:
                        j+=1

        return ans




