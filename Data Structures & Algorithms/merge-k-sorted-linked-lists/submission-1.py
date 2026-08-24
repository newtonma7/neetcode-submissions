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
            edge cases:
            len 0 list or empty list
            
        minheap

        '''
        # edge cases
        if not lists or len(lists) == 0:
            return None

        # broad merge algo where we recycle input back into lists
        while len(lists) > 1:
            # holds current round/iteration to eventually put back into list
            merged = [] 

            # find pairs in lists to merge tg
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # odd edge case
                l2 = lists[i+1] if i+1 < len(lists) else None 
                # actually do the sort algo, then append the res to merged
                merged.append(self.sortAlg(l1,l2)) 
            # recycle input back into lists
            lists = merged 
        # should be sorted last remaining list
        return lists[0]
    
    # sort lists helper func
    def sortAlg(self, l1, l2):
        dummy = ListNode()
        ans = dummy

        while l1 and l2:
            if l1.val < l2.val:
                ans.next = l1
                l1 = l1.next
            else:
                ans.next = l2
                l2 = l2.next
            ans = ans.next
        if not l1:
            ans.next = l2
        else:
            ans.next = l1
        return dummy.next
            




