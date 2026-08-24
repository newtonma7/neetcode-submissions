class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        string that is equivalent when reading left to right and right to left
        

        stack approach,
            add all char to stack
            iterate stack and pop add to new str
            return stack str and normal str

        two pointer, must ignore non alnum char and capitalization
            left pointer = 0
            right pointer = len(s) - 1

            increment left pointer to a valid character to compare

            increment right pointer to a valid char to compare

            do the comparison with case-insensitive,
                if left != right --> return false
                if it checks out, then continue
                if loop fully iterates and ends, str is a palindrome
        '''

        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True


        