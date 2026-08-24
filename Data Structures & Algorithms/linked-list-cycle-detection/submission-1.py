# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        are all values in the list unique?
        approach
            use a set
            iterate through the list
            if value is seen then return true
        '''
        hs = set()

        curr = head

        while curr:
            if curr in hs:
                return True
            hs.add(curr)
            curr = curr.next

        return False