#Cache is a dict as a whole
#Each value of the dict contains a dictionaty - {val:, age:}

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.counter = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache[key]["age"] = self.counter
            self.counter += 1
            return self.cache[key]["val"]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = {"val": value, "age": self.counter}
        
        else:
            if len(self.cache) >= self.capacity:
                lru_key = min(self.cache, key = lambda k: self.cache[k]["age"])
                self.cache.pop(lru_key)
            self.cache[key] = {"val": value, "age": self.counter}
        
        self.counter += 1

    
        

