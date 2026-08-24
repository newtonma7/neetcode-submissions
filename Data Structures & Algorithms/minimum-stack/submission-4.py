class MinStack:
    '''
    want to maintain o(1) for the get min operation

    problem is that if we maintain a pointer to the min, 
    how will we know where the next min resides if we pop that min?

    two stack approach
        one stack operates normally
        one stack has the current min for that position in the normal stack
    
    approach
        whenever we add to the stack normally, we check if the push 
            is less than what we currently have as the min, if not we can just push
            the curr min then
            because if we pop that min off the stack, the new min will reside below it
    '''

    def __init__(self):
        self.stac = []
        self.minstack = []

    def push(self, val: int) -> None:
        if len(self.stac) == 0:
            self.stac.append(val)
            self.minstack.append(val)
        else:
            self.stac.append(val)
            if val < self.minstack[-1]:
                self.minstack.append(val)
            else:
                self.minstack.append(self.minstack[-1])

    def pop(self) -> None:
        self.minstack.pop()
        self.stac.pop()

    def top(self) -> int:
        return self.stac[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
