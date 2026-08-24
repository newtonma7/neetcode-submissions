class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        can do in one pass
        for each num, 
            check the hm again and see if the complement exists within the hm
            num + compl = target
            num - target = compl <--
        '''
        hm = dict()

        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in hm:
                return [hm.get(compl), i]
            else:
                hm[nums[i]] = i
        return [0,0]
