# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        min heap
        init min heap by traversing all nodes

        while minheap exists
            pop and iterate pointers
            add the next node of that list onto the heap
        '''
        if not lists or len(lists) == 0:
            return None
            
        dummy = ListNode()
        curr = dummy

        hp = []

        for idx, node in enumerate(lists):
            heapq.heappush(hp, (node.val, idx, node))

        while hp:
            val, idx, node = heapq.heappop(hp)

            curr.next = node
            curr = curr.next
            node = node.next

            if node:
                heapq.heappush(hp, (node.val, idx, node))
        return dummy.next










    