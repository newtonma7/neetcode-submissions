# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        approach
            create new list with dummy node to return

            merge in place? or ^^ 

            pointer on list 1
            pointer on list 2

            compare
                case 1 : 1 > 2
                    append lesser val to the list
                    iterate that list 2's pointer after appending
                case 2 : 1 < 2
                    append lesser val to the list
                    iterate list 1's pointer after appending
                case 3 : 1 = 2
                    append both vals to the list
                    iterate both list pointers
    
        if one list is exhausted, append remainder to third list
        '''

        list3 = ListNode()
        dummy = list3
        
        while list1 and list2:
            if list1.val < list2.val:
                list3.next = list1
                list1 = list1.next
            else:
                list3.next = list2
                list2 = list2.next
            list3 = list3.next

        if not list1:
            list3.next = list2
        else:
            list3.next = list1

        return dummy.next

