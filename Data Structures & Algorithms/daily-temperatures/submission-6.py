class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        monotonic stack pattern?
        understand:
            q: 
            ec: non increasing is all 0's
            figure out an algo to find the num of days 
            it took to have a greater temp on that day,
        match:
            we can use a stack here
            stack will help us preserve the prev day and index for us
            as we look forward to a future day
        plan:   
            approach
                use stack with (value, idx) tuple
                iterate temps and store the val,idx
                if the temp we see is greater, 
                    then pop the stack continually and update that pos

        '''
        res = [0] * len(temperatures)
        stk = []

        for i in range(len(temperatures)):
            curr = temperatures[i]
            while stk and curr > stk[-1][0]:
                off = stk.pop()
                res[off[1]] = i - off[1]
            stk.append((curr,i))
        return res


