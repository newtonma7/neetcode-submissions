class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        left ptr at 0 
        right ptr at len - 1
        mx variable holding max area

        area = min(heights[l],heights[r]) * (l-r)
        we want to maximize height so we can judge the left and right ptr
            and keep the taller one
        '''

        l = 0
        r = len(heights) - 1
        mx = 0

        while l < r:
            curr = min(heights[l], heights[r]) * (r - l)
            if curr > mx:
                mx = curr
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return mx

