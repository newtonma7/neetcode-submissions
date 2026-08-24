class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        input: array of temps
        output: array where array[i] represents the number of days after it that is greater than it
        problem: how do we know when to "set" that index
    
        approach
            brute
                need to look ahead of that current temp
                could use a nested for loop with counter variable to look ahead
                    for each temp, we look at temp + 1 index till end of temps
                        counter for each loop
                        once we find a greater temp, break the loop and set that index
            stack
                use indices on stack so we can just set it to array[i]
                use a stack so we can remember the previous temps
                iterate through the temps
                    is this temp greater than the top of the stack?
                        if it is then we can pop the top of the stack and finalize that indices pos
                    add temp onto stack
        '''

        st = []
        

        for idx, temps in enumerate(temperatures):
            while len(st) > 0 and temps > st[-1][0]:
                put = st.pop()
                temperatures[put[1]] = idx - put[1]
            else:
                temperatures[idx] = 0
            st.append([temps,idx])


        return temperatures
