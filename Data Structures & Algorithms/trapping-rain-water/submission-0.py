class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        input: heights
        output: max area of water
        stack?

        left ptr on start
        right ptr on len - 1

        algo that finds areas of water


        we can calculate total water between two heights by
            min(h[l], h[r]) * (l-r) - heights in between
        '''

        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        
        water = 0
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(height[l], leftMax)
                if min(leftMax, rightMax) - height[l] > 0:
                    water += min(leftMax, rightMax) - height[l]
            else:
                r -= 1
                rightMax = max(height[r], rightMax)
                if min(leftMax, rightMax) - height[r] > 0:
                    water += min(leftMax, rightMax) - height[r]
        return water
                