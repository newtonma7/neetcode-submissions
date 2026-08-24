# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        cut lists in half
            first half you dont need to reverse
            the other one you do
            use a fast and slow pointer to find middle of the list
        reverse second half of list
        remerge the reversed second half and first half
        '''

        # get middle ptr of linked list, 
        # since we need to get the node before the middle, do we add dummy node?
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # cut the second half off and grab the new head of the second half
        slow2 = slow.next 
        slow.next = None

        # reverse second half, prev is new head
        prev = None
        while slow2:
            temp = slow2.next
            slow2.next = prev
            prev = slow2
            slow2 = temp
        
        # remerge both lists, prev is new head
        while prev:
            next1 = head.next
            next2 = prev.next
            head.next = prev
            prev.next = next1
            head = next1
            prev = next2



            
        


        
        