# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        understand: find algo to reverse k nodes,
                    then start again and reverse again
                    fewer than k nodes, then leave them

        match: multiple pointers, one looks ahead, 
                helper function to reverse?
        plan:
            dummy node,
            get kth helper function

            we need the prev of each group and the kth of each group
            so we can figure out where to repoint too at the end of each
            group, we also need groupnext to figure out when to stop 
            iterationg

            we want to grab the 1st node to repoint  
            it to the kth node of the next group at the end of each loop
        '''

        dummy = ListNode(0,head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # save the first node that now points to groupNext
            temp = groupPrev.next  
            groupPrev.next = kth # points to the new head of list
            # prev is the node that used to be the head aka points to next group
            groupPrev = temp 


        return dummy.next



    def getKth(self, node, k):
        while node and k:
            node = node.next
            k-=1
        return node
