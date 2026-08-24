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
        make a hashmap that maps old nodes to the new nodes {oldnode : new node}

        first pass through to map the nodes and create nodes without pointers yet
        second pass to map the next and random pointers to each other
        '''

        if not head:
            return None
        hm = {None: None}
        curr = head
        ans = head

        while curr:
            hm[curr] = Node(curr.val)
            curr = curr.next

        curr2 = head
        for k in hm:
            if k:
                hm[k].next = hm[k.next]
                hm[k].random = hm[k.random]
        
        return hm[ans]