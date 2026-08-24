class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set()
        

        for x in nums:
            if x in dup:
                return True
            dup.add(x)
        
        return False