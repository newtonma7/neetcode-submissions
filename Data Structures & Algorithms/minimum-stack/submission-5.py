class MinStack:
    '''
    two stacks
    one stack keeps track of the local minimum 
    by comparing for each push
    the other is a normal one

    the min stack keeps track of the min next to it for 
    that corresponding index in the main stack
    '''
    def __init__(self):
        self.minstack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # if the val isnt new min, 
        #just append whatever min was tracked
        if self.minstack and val < self.minstack[-1] or len(self.minstack) == 0:
            self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[-1])

    def pop(self) -> None:
        if not self.stack:
            return None
        self.minstack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
