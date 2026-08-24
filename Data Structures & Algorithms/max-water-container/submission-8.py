class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        max amount of water
        approach
        water = min(h[l], h[r]) * r - l + 1

        two ptr
        l = 0
        r = len - 1
        iterate based off of what?
        iterate based off of height 
        because we want the higher bar for more area
        ''' 
        l = 0
        r = len(heights) - 1
        mx = 0

        while l < r:
            curr = min(heights[l], heights[r]) * (r-l)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
            mx = max(curr,mx)
        return mx
