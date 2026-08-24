class Solution:
    def isValid(self, s: str) -> bool:
        '''
        reiterate problem to make it clear what the problem is
        what are we given?
        what do we need to return?

        --> move to the how

        stack approach because we need to keep track of the things that were added in last
        need something with first in last out 

        iterate through the string
            if we see an open bracket,
                add it to the stack
            if we see a close bracket,
                check if stack is empty --> wrong order for paren --> false
                pop from the stack and check that it matches
                if it doesn't match, return False

        if we complete the loop --> must check if stack is empty or not

        '''

        stack = []

        for paren in s:
            if paren in ["(", "[", "{"]:
                stack.append(paren)
            if paren == ")":
                if len(stack) == 0 or stack.pop() != "(": return False
            if paren == "]":
                if len(stack) == 0 or stack.pop() != "[": return False
            if paren == "}":
                if len(stack) == 0 or stack.pop() != "{": return False 
        return len(stack) == 0
