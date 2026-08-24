# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        understand:
        need an algorithm to interweave the n-1 nodes between every node
        match: 
        linked list, we can split the list --> reverse the second half --> braid in the nodes
        plan:
        fast and slow pointer to find middle of the list
        cut off the second list and set up pointers for reversal

        braid in the nodes by having a prev and next pointer for the first half list
        '''
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # now slow is in the middle, so cut it 
        curr = slow.next
        slow.next = None
        prev = None

        # reverse
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # now prev is new head of the reversed list, so we braid
        newcurr = head
        while newcurr and prev:
            temp = newcurr.next
            temp2 = prev.next
            newcurr.next = prev
            prev.next = temp
            newcurr = temp
            prev = temp2





