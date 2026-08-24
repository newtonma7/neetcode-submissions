class Node:
    def __init__(self, key, val):
        self.val, self.key = val, key
        self.prev = self.next = None

class LRUCache:
    '''
    sentinel nodes to simplify the code, doubly linked list
    helper methods
        remove
        insert
    '''
    def __init__(self, capacity: int):
        '''
        init sentinel nodes
        '''
        self.left = Node(None,None)
        self.right = Node(None,None)
        self.cap = capacity

        self.left.next = self.right
        self.right.prev = self.left

        # holds key to access node with k,v
        # if we have ptr to node, we can do o(1) ops bc no traversal
        self.hm = {} 
    
    def insert(self,node):
        '''
        insert into right node position
        '''
        second = self.right.prev
        second.next = node
        node.prev = second
        node.next = self.right
        self.right.prev = node



    def remove(self,node):
        '''
        get prev ptr 
        '''
        before = node.prev
        nxt = node.next
        nxt.prev = before
        before.next = nxt



    def get(self, key: int) -> int:
        '''
        o(1) --> hashmap?
        if we get, we need to move the node to the top
        if key is in hm, remove it from nodes then reinsert to update based on policy
        '''
        if key in self.hm:
            self.remove(self.hm[key])
            self.insert(self.hm[key])
            return self.hm[key].val
        return -1
            
        

    def put(self, key: int, value: int) -> None:
        '''
        look in hm for existence
        '''
        if key in self.hm:
            self.remove(self.hm[key])

        self.hm[key] = Node(key, value) 
        self.insert(self.hm[key])

        if len(self.hm) > self.cap:
            rem = self.left.next
            self.remove(rem)
            self.hm.pop(rem.key)

        
