class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        can we still use a hashmap in this?
            hm {num : index}
            doesnt matter because its sorted i think


        two pointer technique
            left pointer starts at idx 0
            right pointer starts at the len -1


        '''
        
        seen = dict() 

        for i in range(len(numbers)):
            compl = target - numbers[i]
            if compl in seen:
                return [seen[compl]+1, i+1]
            seen[numbers[i]] = i
            
        return []
