class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        sort the input array
            fix one number then l and r ptr the rest
                similar algo to sorted 2 sum
                but we need to skip the i we are on so no dupes
        '''

        ans = []
        nums.sort()

        for i in range(len(nums)):
            # duplicate check
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = len(nums) - 1

            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if curr == 0:
                    ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                if curr < 0:
                    l+=1
                else:
                    r -= 1
        return ans
