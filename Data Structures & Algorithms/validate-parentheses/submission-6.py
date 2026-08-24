class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for paren in s:
            if paren in ["(", "[", "{"]:
                stack.append(paren)
            if paren == ")":
                if len(stack) == 0 or stack.pop() != "(": return False
            if paren == "]":
                if len(stack) == 0  or stack.pop() != "[": return False
            if paren == "}":
                if len(stack) == 0 or stack.pop() != "{": return False
        

        return len(stack) == 0