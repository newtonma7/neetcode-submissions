class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        q:
        numbers always first

        add to stack till we hit an op then pop from stack
        everytime we do an op add it back onto the stack

        edge cases:
        len 0 

        '''
        stack = []
        for tok in tokens:
            print(tok)
            print(stack)
            if tok == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif tok == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif tok == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            elif tok == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(tok))
        return stack[-1]

