class ListNode:
    def __init__(self, key = 0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.capacity = capacity
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insertBeforeMRU(self,node):
        temp = self.right.prev
        temp.next = node
        node.prev = temp
        self.right.prev = node
        node.next = self.right
    
    def moveToMRU(self,node):
        # If its already most frequent
        if node.next == self.right:
            return
        # if it's anywhere else, first disconnect it from there
        self.removeNode(node)
        # now insert it before mru
        self.insertBeforeMRU(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # self.cache[key] is reference to the ListNode.
        # If this is currently before MRU - we're done
        node = self.cache[key]
        self.moveToMRU(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.moveToMRU(self.cache[key])
            self.cache[key].val = value
        else:
            node = ListNode(key, value)
            self.cache[key] = node
            self.insertBeforeMRU(node) 

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.removeNode(lru)
            del self.cache[lru.key]


        
