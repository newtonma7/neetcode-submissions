class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        understand:
            qs:
            ec:
        match:
            monotonic stack
        plan:
            init max, stack
            if value doesnt beat max, add to stack
            how do we know what to calculate to check against max?
                curr min, multiply by len of stack?
                need ptr to min, also doesnt account for a 5,5,1 
                1 would bottleneck the algo as well so how do we pop that?
                if the curr min * len doesn't beat the max, pop till it does?
            approach
                keep the stack strictly increasing, 
                if rule is violated --> we pop
                store tuples that track idx and width
                area form = (curr idx - stored idx) * curr h

        '''
        maxWidth = 0
        stack = []
        
        for idx, h in enumerate(heights):
            start = idx
            while len(stack) and h < stack[-1][1]:
                currIdx, currH = stack.pop()
                currWidth = currH * (idx - currIdx)
                maxWidth = max(maxWidth, currWidth)
                start = currIdx
            stack.append((start,h))
        
        while stack:
            currIdx, currH = stack.pop()
            maxWidth = max(maxWidth, (len(heights) - currIdx) * currH)
        return maxWidth
