class Node:
    def __init__(self,key=0,val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _remove(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def _add_to_front(self,node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key,value)
        self.cache[key]=node
        self._add_to_front(node)

        if len(self.cache)>self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]


