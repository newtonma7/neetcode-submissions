class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        prefix, postfix operations
        approach
            running product prefix first
            pre is 0 at first
            iterate till
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
