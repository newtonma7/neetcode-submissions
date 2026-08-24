# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        two passes
            pass through once collect length
            calculate index to remove the node

            pass second time and repoint the pointer

        one pass
            slow and fast ptr = L, R ptr
            add a dummy node so we can get the node before the node to remove
        '''
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n-=1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next


        
        

        


        


