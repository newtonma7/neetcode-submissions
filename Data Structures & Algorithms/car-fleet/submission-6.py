class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        approach
            a car can join another car when it gets passed

            brute n^2
                increment each position by their own speed
                check if the next iteration of speed will catch this car up to any other ones,
                if it does then increment counter by one and add it to set
            stack
                make a new array that represents each car
                sort cars in desc order because if we go left to right, how will we know the cars combining into fleets?
                we can find car fleets by finding the time the hit target,
                    if a car behind another has a shorter time, then we know they become fleet
                iterate in desc order arr
                    
                time calculation is target - pos / speed
        '''

        stack = []
        cars = [[p,s] for p,s in zip(position, speed)]
        cars.sort(reverse=True)

        for p,s in cars:
            time = (target - p) / s
            if len(stack) == 0 or time > stack[-1]:
                stack.append(time)
        return len(stack)


