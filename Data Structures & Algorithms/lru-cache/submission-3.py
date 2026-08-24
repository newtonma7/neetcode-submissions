class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = self.next = None
    
class LRUCache:
    '''
    understand: make lru cache with 
                o1 get, and o1 put
    match: 
        linked list with sentinel nodes and doubly linked to make
        put o1, use a hashmap to make get o1
        linked list makes the lru policy easy to implement
    plan:
        front node, end node as sentinels,
        hashmap to make lookup o(1)
        since put is o(1) we should put nodes into hm
        
    '''
    def __init__(self, capacity: int):
        self.front = Node(None, None)
        self.back = Node(None, self.front)
        self.front.next = self.back

        self.cap = capacity
        self.hm = {}  # key : node

    def get(self, key: int) -> int:
        if key in self.hm:
            self.remove(self.hm[key])
            self.add(self.hm[key])
            return self.hm[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.remove(self.hm[key])

        self.hm[key] = Node(key, value)
        self.add(self.hm[key])

        if len(self.hm) > self.cap:
            rem = self.back.prev
            self.remove(rem)
            self.hm.pop(rem.key)


    def add(self, node):
        second = self.front.next
        self.front.next = node
        node.next = second
        node.prev = self.front
        second.prev = node

    def remove(self,node):
        temp = node.next
        temp2 = node.prev
        node.prev.next = node.next
        temp.prev = temp2




