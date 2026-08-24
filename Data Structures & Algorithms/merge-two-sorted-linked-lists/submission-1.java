/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        /*
        input: sorted LL 1, sorted LL 2
        output: head of the combined two lists
        edge cases: 1 list is one node, or empty
        
        node 1 < node 2
            LL3 point to lesser node, node 1
            iterate node1

        node 1 > node 2
            LL3 point to lesser node, node 2
            iterate node2

        node 1 == node 2
            pick one and add 
            iterate that LL

        iterate LL3
        */
        ListNode dummy = new ListNode(-1);
        ListNode l3 = dummy;

        while(list1 != null && list2 != null){
            if(list1.val < list2.val){
                l3.next = list1;
                list1 = list1.next;
            }
            else{
                l3.next = list2;
                list2 = list2.next;
            }
            l3 = l3.next;
        }
        if(list1 == null){
            l3.next = list2;
        }
        else if(list2 == null){
            l3.next = list1;
        }

        return dummy.next;

    }
}