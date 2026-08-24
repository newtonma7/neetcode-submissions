"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        understand: need to make a completely new list in memory with random pointers
        match: 
            can use a hashmap here to create mappings and kinda act as a layer between new nodes and old nodes
        plan:
            init hashmap of {old node : new node}
            first iteration, create the nodes before starting to point pointers
            second iteration, 
                point the next ptrs easily since the nodes are already created
                point the random ptrs according to the hashmap guide 
        '''

        hm = {None : None}

        curr = head
        while curr:
            hm[curr] = Node(curr.val,next=None,random=None)
            curr = curr.next

        for node in hm.keys():
            if node:
                hm[node].next = hm[node.next]
                hm[node].random = hm[node.random]
        
        return hm[head]