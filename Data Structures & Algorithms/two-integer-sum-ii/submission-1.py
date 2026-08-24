class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        can we still use a hashmap in this?
            hm {num : index}
           we can but the size wont be O(1)


        two pointer technique
            left pointer starts at idx 0
            right pointer starts at the len -1


        '''
        le = 0
        ri = len(numbers) - 1

        while le < ri:
            curr = numbers[le] + numbers[ri]

            if curr == target:
                return [le + 1, ri + 1]
            elif curr < target:
                le += 1
            else:
                ri -= 1
        
        
