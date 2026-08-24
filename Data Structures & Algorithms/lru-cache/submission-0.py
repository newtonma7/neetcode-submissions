class Node():
    def __init__(self, key, val):
        self.val, self.key = val, key
        self.prev = self.next = None

class LRUCache:
    '''
    LRU with linked list + hashmap
        most recently used should be first node 
        what data does the node store?
            data in the node should be the key
        rearrange the nodes for every get/put operation
            linked to hashmap key 
        hashmap seperate for easy get and put

        steps for rearrange with prev and next ptrs
        most recently used will be the left side, least recently is right side
            if the cache has nodes in it already
                we need to reappend the pointers surrounding the node we just pulled
                make the node before it point to the node after it
                then take the ptrs of the pulled node and readd to the left

    '''
    def __init__(self, capacity: int):
        self.cache = {} # {key : node}
        self.cap = capacity
        #sentinel nodes
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    #remove node from list
    def remove(self, node):
        pre, nxt = node.prev, node.next
        pre.next, nxt.prev = nxt, pre

    # insert at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    #updates/inserts into list and hashmap
    def put(self, key: int, value: int) -> None:
        #case where key is already in the cache 
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value) # insert into hashmap
        self.insert(self.cache[key]) # insert into list

        #remove lru node/key
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


            


