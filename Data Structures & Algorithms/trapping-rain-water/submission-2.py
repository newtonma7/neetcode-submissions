class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        left and right ptr 

        look index by index,

        build the left max, right max arrays first
        then loop to calculate water index by index
        '''
        if not height:
            return 0

        left = [0] * len(height)
        right = [0] * len(height)
        water = 0

        # +1 and -1 because leftmost and right most are 0
        for i in range(1,len(height)):
            left[i] = max(left[i-1], height[i-1])
        
        for i in range(len(height) - 2, -1, -1):
            right[i] = max(right[i+1], height[i+1])
        
        for i in range(len(height)):
            water += max(min(left[i],right[i]) - height[i],0)

        return water

        
