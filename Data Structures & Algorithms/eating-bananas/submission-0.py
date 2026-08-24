class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        we must find the minimum banana eating rate k
        
        given the time constraint of h hours we have to find the smallest rate of bananas we can eat per hour

        lower bound: it will take koko x / k hours to finish the pile of banas
        upperbound: max amt of time itll take is the biggest pile

        brute solution
            iterate through piles
                figure out how long it will take to eat curr pile
                have counter for return
                as soon as we find the value 

        optimized soln
        '''
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            time = 0
            k = (l + r) // 2
            for banan in piles:
                time += math.ceil(banan/k)
            # if k is less than h, set right pointer to k - 1
            if time <= h:
                res = k
                r = k-1
            else: # if k is greater than h, set left to k + 1
                l = k+1
        return res
            