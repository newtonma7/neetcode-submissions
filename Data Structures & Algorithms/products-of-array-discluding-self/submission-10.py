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
        temp = 0
        ans = [1] * len(nums)

        for i in range(len(nums)):
            temp = nums[i] * pre
            ans[i] = pre 
            pre = temp

        post = 1
        for i in range(len(nums)-1, -1, -1):
            temp = nums[i] * post
            ans[i] *= post
            post = temp
        return ans
