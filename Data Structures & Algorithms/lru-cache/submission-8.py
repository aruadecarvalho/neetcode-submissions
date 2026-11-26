class ListNode:
    def __init__(self, key = "", val = 0):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key -> Node

        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node: ListNode):
        prev, nxt = self.tail.prev, self.tail
        prev.next = node
        nxt.prev = node
        node.next, node.prev = nxt, prev

        self.cache[node.key] = node

    def remove(self, node: ListNode):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def evict_lru(self):
        lru = self.head.next
        assert lru is not self.tail, "evicting from empty list"
        self.remove(lru)
        del self.cache[lru.key]

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]           
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.insert(ListNode(key, value))

        if len(self.cache) > self.cap:
            self.evict_lru()
        