class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        prefix and postfix arrays

        create output array 


        '''

        res = [1] * len(nums)

        # we want to multiply all the values on the left of the number and put it into the res arr
        # then multiply all the values on the right of the number and put it into the res arr

        pre = 1
        for i in range(len(nums)):
            # set var in the res array to prefix var
            res[i] = pre
            # multiply pre to accurately show the running prefix multiplication
            pre *= nums[i]
    
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            # now as we go backwards, we want to multiply by post and finalize that spot for the num
            res[i] *= post 
            # to find the new post, we multiply by the pos in nums
            post *= nums[i]
        return res