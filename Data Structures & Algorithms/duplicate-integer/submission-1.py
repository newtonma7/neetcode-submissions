class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = dict()
        

        for x in nums:
            if dup.get(x,8) != 8:
                return True
            dup.update({x:1})
            
        
        
        return False