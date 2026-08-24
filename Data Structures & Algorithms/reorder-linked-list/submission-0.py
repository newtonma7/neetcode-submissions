# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        slow pointer and fast pointer
            slow ptr reaches the middle
            fast ptr reaches the end
                reverse second half of the linked list
            zipper merge them back together
            
        '''

        slow = head
        fast = head
        ans = head

        #iterate to the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #cut second half off
        newSlow = slow.next
        slow.next = None

        #reverse the second half
        prev = None
        curr = newSlow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        #zipper merge back together
        first = head
        while prev:
            tempSlow = prev.next
            tempHead = first.next
            first.next = prev
            prev.next = tempHead
            first = tempHead
            prev = tempSlow




        
        
