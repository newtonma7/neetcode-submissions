class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        can do in one pass
        for each num in the dict,
            we can calculate the complement with the target 
            --> check if that complement is in the hm
                    return true
                else
                    add compl into hm with its idx
        curr + compl = target
        target - curr = compl
        '''
        hm = dict()

        for i, num in enumerate(nums):
            compl = target - num
            if compl in hm:
                return [hm.get(compl), i]
            hm.update({nums[i]:i})
        return [0,0]
            


        
