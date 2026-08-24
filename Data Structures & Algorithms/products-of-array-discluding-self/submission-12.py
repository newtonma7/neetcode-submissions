class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        prefix, postfix operations
        approach
            we need ans array to store answers and use nums for og nums
            running product prefix first
                iterate,
                    set that idx num to pre
                    update pre
            
            post
                iterate backwards
                set idx num to * post since we shouldn't overwrite
                update post
        '''
        pre = 1
        ans = [1] * len(nums)
        for i in range(len(nums)):
            ans[i] = pre 
            pre *= nums[i]

        post = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= post
            post *= nums[i]
        return ans
