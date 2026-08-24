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
            if tok == "+":
                stack.append(stack.pop() + stack.pop())
            elif tok == "*":
                stack.append(stack.pop() * stack.pop())
            elif tok == '-':
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num2-num1)
            elif tok == "/":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(num2/num1))
            else:
                stack.append(int(tok))
        return stack.pop()
                    