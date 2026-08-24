class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        input: array of sequential temperatures
        output: replace that temperature with the number of days after it
                when we encounter a greater temperature
            
        brute force:
            loop through temperatures
                loop through i+1 temperatures
                    find the first num greater than it
                    break the loop and replace it

        stack problem
            monotonic stack problem

            stack values are the indices of days that are waiting for a warmer day

            if we encounter a warmer day, we should continually pop from the stack
                because all of those days are less than the warmer day
            
            iterate through the temperatures
                if stack is not empty and curr value is greater than the peek of stack
                    while the currtemp is greater than the top of the stack:
                        pop and finalize that position for that day in the answer array
                add val onto the stack


        '''
        ans = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            # we need to check if the current temperature can satisfy the vals on the stack
                # if it does we will continue to pop and finalize the days for vals we satisfy
            while stack and temp > temperatures[stack[-1]]:
                add = stack.pop()
                ans[add] = i - add 
                # position is current temp we are on and the index of the temp that satisfies 
            stack.append(i) # if curr temp doesnt work then add to stack and let it wait for warmer day
        return ans
        


        