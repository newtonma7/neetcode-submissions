# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        understand:
        remove the nth node from the end of the list, how do we do it in one pass?
        match:
            we have to land on the node right before the nth node and cut it
                pad one node
            fast and slow pointer, so when the fast hits null the slow one is on the target
            must iterate fast n times so it has a headstart of n
        plan:
            pad one node
            standard fast slow ptr
            iterate n times, then chop
            return
        '''
        fast = head
        dummy = ListNode(val=None,next=head)
        slow = dummy

        for _ in range(n):
            fast=fast.next
            
        while fast:
            fast = fast.next
            slow = slow.next
    
        slow.next = slow.next.next

        return dummy.next
