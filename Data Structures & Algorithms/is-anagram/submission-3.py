class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        list1 = [*s]
        list2 = [*t]
        list1.sort()
        list2.sort()

        for i in range(len(s)):
            if list1[i] != list2[i]:
                return False
        return True
    

        