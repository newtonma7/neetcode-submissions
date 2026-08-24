# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        understand: add up linked list to their sum, starting with the ones place, tens place, etc.
        q's: what if not same length?
        match: linked list, probably need some modulo or division operation with remainder tracking
        plan: 
            init remainder var
            loop through list
                add them, if its over 10 then we % to get the current, 
                then add the // to the remainder var
        '''

        rem = 0
        dummy = ListNode(val=-1,next=None)
        currNode = dummy

        while l1 or l2 or rem:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sm = val1 + val2 + rem
            curr = sm

            curr = curr % 10
            rem = sm // 10

            currNode.next = ListNode(val=curr, next=None)
            currNode = currNode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None



        return dummy.next
            