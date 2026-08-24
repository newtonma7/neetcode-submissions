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
        use a 1 hashmap with tuples for mapping of the next and the random
            {3 : tuple(val of next, random .val)} we need values because we're making deep copy
        and one where we store the nodes after finishing the next mapping
        
        when we map the random, we dont need to iterate again to find the spot to point to the random
            just do a lookup in the hashmap

        we first need to create the list with the .next pointers
            then pass through again and add the random pointers
        '''
        # {old Node : copy Node}
        # this gives us easy lookup to the right values while maintaining the deep copy requirement
        og = {None : None} 

        # this pass creates all the nodes, no ptr stuff yet
        curr = head
        while curr:
            copy = Node(curr.val)
            og[curr] = copy
            curr = curr.next
            
        #we now have a map that links all old nodes to the new nodes
        
        #second pass assigns the pointers
        curr = head
        while curr:
            copy = og[curr] #grab the copy node
            copy.next = og[curr.next] #assign the node's next ptr by doing a lookup bc old.next maps to copy.next
            copy.random = og[curr.random]
            curr = curr.next
        return og[head]

        
        
        
            


