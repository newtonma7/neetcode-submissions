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

        
        '''
        ans = []

        for i in range(len(temperatures)):
            j = i+1
            counter = 1
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    temperatures[i] = counter
                    break
                j += 1
                counter += 1
            if j == len(temperatures):
                temperatures[i] = 0
        return temperatures