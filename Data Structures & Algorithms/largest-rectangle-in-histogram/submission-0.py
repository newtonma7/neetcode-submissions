class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        rectangle area is the min height of all of the heights times how many heights we are considering
            we can find how many heights to consider by tracking how many are consecutively greater than min?

        approach
            brute
                for each rectangle,
                    treat the current bar we are on as the shortest one
                    we go left and right to see how many heights we can add to the area
                    if we hit a bar shorter, then we stop looking
                    
            stack
                stack
                    iterate
                        while loop: check if current add is less than the top of the stack
                            if it is then pop it and calculate the area it could've been
                        once we reach a value that is not less than current add, we calculate the
                        possible area that we popped (track which index it could start from)    
        '''

        maxarea = 0
        stack = []

        for idx, h in enumerate(heights):
            start = idx
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                maxarea = max(maxarea, height * (idx-index))
                start = index
            stack.append([start, h])

        for idx, h in stack:
            maxarea = max(maxarea, h * (len(heights) - idx))
        return maxarea
            