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
        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt +=  1
                
        if zero_cnt > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt:
                if c != 0:
                    res[i] = 0
                else:
                    res[i] = prod
            else: res[i] = prod // c
        return res
            


