class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        stack problem
            add numbers onto stack
            we should always see 2 nums before we see an operation
            once see operation pop twice from the top and do the op
                order of the op matters, like subtraction or division
                see - sign then
                    pop1, pop2, --> pop2 - pop1
            add that result back onto stack
            iterate
            once loop is done, return stack.pop()
            string to operator or num to operator translate? 
            eval or hashmap
        '''


        
        stack = []

        for tok in tokens:
            if tok.isnumeric() or (len(tok) > 1 and tok[0] == "-"):
                stack.append(int(tok))
                print(stack)
            else:
                print(stack)
                print(tok)
                pop1 = stack.pop()
                pop2 = stack.pop()
                match tok:
                    case "+":
                        stack.append(pop2 + pop1)
                    case "*":
                        stack.append(pop2*pop1)
                    case "-":
                        stack.append(pop2-pop1)
                    case "/":
                        stack.append(int(pop2 / pop1))
        
        return stack.pop()

                

