class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        input is
            integer array
        output is 
            product of all elements in nums except nums[i]
        
        edge cases : 
            0 as an element
            only 1 in the array

        division approach
            make a seperate array the length of nums
            multiply every nums[i] with everything else
            
            then iterate over that array and divide it by the same index at nums
                if we encounter a 0, do not divide

            need to consider edge case of 0
                we cannot divide by 0
        '''
        res = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res 

        
            


