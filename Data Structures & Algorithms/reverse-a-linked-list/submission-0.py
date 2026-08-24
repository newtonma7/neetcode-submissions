# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        in place approach

            have 3 pointers
            prev = head
            curr = prev.next
            post = curr.next

            need curr to point to prev and have post become new curr then update curr to be new prev

            loop thru linked list
                #reversing here
                curr.next = prev 

                #update pointers
                prev = curr
                curr = post
                post = curr.next
        '''
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev






