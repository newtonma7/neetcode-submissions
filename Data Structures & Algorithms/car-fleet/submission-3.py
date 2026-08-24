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
                    compare adjacent cars on teh stack and calculate time
                    if car 2 time shorter than car 1, 
                        pop that one and continue iteration
                    push car onto stack 
                    return stack len
                time calculation is target / speed
        '''

        stack = []
        road = []

        for i in range(len(position)):
            road.append([position[i], speed[i]])

        road.sort(reverse = True, key = lambda cars: cars[0])

        for car in road:
            stack.append((target - car[0]) / car[1])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


