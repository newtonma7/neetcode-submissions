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
        ops = {"+","-","*","/"}
        for tok in tokens:
            if tok not in ops:
                stack.append(int(tok))
            else:
                a = stack.pop()
                b = stack.pop()
                
                if tok == "+":
                    stack.append(a+b)
                elif tok == "-":
                    stack.append(b-a)
                elif tok == "*":
                    stack.append(a*b)
                elif tok == "/":
                    stack.append(int(b/a))
        return stack[-1]

