class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        problem is that the operations and numbers are in a weird order

        use a stack
            iterate through tokens
                if we see numbers then push onto stack
                once we see an operand, 
                    pop twice from stack and then do the operation
                    then push that result back onto stack
            
            return last remain in stack
        '''

        stack = []

        for tok in tokens:
            if tok.isdigit() or len(tok) > 1 and tok[0] == "-":
                stack.append(int(tok))
            else:
                print(stack)
                print(tok)
                num1 = stack.pop()
                num2 = stack.pop()
                if tok == "+":
                    stack.append(num1+num2)
                elif tok == "*":
                    stack.append(num1*num2)
                elif tok == '-':
                    stack.append(num2-num1)
                elif tok == "/":
                    stack.append(int(num2/num1))
        return stack.pop()
                    