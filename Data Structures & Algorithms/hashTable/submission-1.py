class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.map = [None]*self.capacity
    
    def hash(self, key):
        index = key
        return index % self.capacity

    def get(self, key: int) -> int:
        index = self.hash(key)

        # return self.map[index].val # this is my basic return
        # # but first check if key at this index actually our key
        # # if not, then move index forward

        while self.map[index] is not None:
            print(self.map[index])
            if self.map[index].key == key:
                return self.map[index].val
            
            index += 1
            index = index % self.capacity
        
        return -1

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)

        while True:
            if self.map[index] is None:
                # if that index is empty
                self.map[index] = Pair(key, value)
                print(f"Inserted into map {self.map[index].key}")
                self.size += 1
                if self.size >= self.capacity // 2:
                    #self.rehash()
                    self.resize()
                return
            elif self.map[index].key == key:
                # index not empty but the key there is our key
                self.map[index].val = value
                return
            index += 1
            index = index % self.capacity

    def resize(self) -> None: # this is the rehash
        self.capacity = self.capacity*2
        newMap = [None]*self.capacity

        oldMap = self.map
        self.map = newMap
        self.size = 0  # imp to set this because the insert operation will increase the size on each operation and we are going to need insert operation.

        for pair in oldMap:
            if pair is not None:
                self.insert(pair.key, pair.val)

    def remove(self, key: int) -> bool:
        index = self.hash(key)

        while self.map[index] is not None:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1
                return True
            index += 1
            index = index % self.capacity
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity
