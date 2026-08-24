class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        understand:
            q: 
            ec:
            find an algo that finds the number of car fleets
            iterating each step, check if a car will overtake another
            then make that one fleet

        match:
            monotonic stack increasing?

        plan:
            zip to combine then sort by position to get 
            representation of cars on the highway
            brute:
                iterate each car by their speed for each loop iteration till target
                check each individual car to see if their pos overlaps the other 
            time = (target - pos) / speed
            iterate backwards and calc time for each car, 
            add car onto stack based on time 
        '''

        stk = []
        cars = sorted(zip(position,speed), reverse=True)

        for p, s in cars:
            time = (target - p) / s
            if len(stk) == 0 or time > stk[-1]:
                stk.append(time)
        return len(stk)


