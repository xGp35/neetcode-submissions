class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.tail
            node.prev = self.tail.prev
            self.tail.prev.next = node
            self.tail.prev = node
            return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.tail
            node.prev = self.tail.prev
            self.tail.prev.next = node
            self.tail.prev = node
            node.value = value
        else:
            new_node = Node(key = key, value = value)
            self.cache[key] = new_node
            self.tail.prev.next = new_node
            new_node.next = self.tail
            new_node.prev = self.tail.prev
            self.tail.prev = new_node
            if len(self.cache) > self.capacity:
                key_to_remove = self.head.next.key
                del self.cache[key_to_remove]
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                
