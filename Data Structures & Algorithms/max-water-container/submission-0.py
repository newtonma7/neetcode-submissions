class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        two pointer solution

        left = 0
        right = len(heights) - 1
        curr 
        
        we want the biggest area rectangle


        how do we iterate the left and right pointers?
            let go of the smaller one, keep the bigger one

        while left < right
            calculate the area with
                indices between left and right * min of left or right
                compare that with the current most water

                iterate based on which ptr is greater
                    if left is greater we decrement the rightside
                    if right is greater we increment the leftside
                
        '''
        left = 0
        right = len(heights) - 1
        most = 0

        while left < right:
            curr = (right - left) * min(heights[left], heights[right])
    
            most = max(curr, most)
            if heights[left] < heights[right]:
                left += 1
            else:
                right-=1

        return most
        
