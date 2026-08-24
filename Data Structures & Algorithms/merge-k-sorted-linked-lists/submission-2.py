# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        naive approach
            find the smallest num amongst all k lists and add to final list
        how do we reduce repeated work?

        divide and conquer
            grab 2 lists at a time and merge them together to sort those
                use a merge helper function to actually sort the values
                recycle input through lists
            edge cases:
            len 0 list or empty list
            
        minheap
            we track all lists through a minheap
                init the minheap with the first values of lists
                    track value, index, and ptr to the node
                    index cuz of ties or use wrapper
        '''
        dummy = ListNode()
        curr = dummy
        minh = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minh, (node.val, i, node))
        
        while minh:
            val, i, node = heapq.heappop(minh)
            curr.next = node
            node = node.next
            curr = curr.next
            
            if node:
                heapq.heappush(minh, (node.val, i, node))
        return dummy.next
            



       
            




