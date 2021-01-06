from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.q = []
        # (key, value)
        
    def get(self, key: int) -> int:

        val = None

        # Find
        for idx, cached in enumerate(self.q):
            if cached[0] == key:
                val = cached[1]
                self.q.pop(idx)
                self.q.insert(0, (key, val))

        if val:
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        found = None

        # Find
        for idx, cached in enumerate(self.q):
            if cached[0] == key:
                found = cached[1]
                self.q.pop(idx)
                self.q.insert(0, (key, found))

        if not found:
            if len(self.q) == self.capacity:
                self.q.pop(len(self.q)-1)
                self.q.insert(0, (key, value))
            else:
                self.q.insert(0, (key, value))


if __name__ == "__main__":
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)       # returns 1
    cache.put(3, 3)    # evicts key 2
    cache.get(2)       # returns -1 (not found)
    cache.put(4, 4)    # evicts key 1
    cache.get(1)       # returns -1 (not found)
    cache.get(3)       # returns 3
    cache.get(4)       # returns 4