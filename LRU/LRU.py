class LRU:

    def __init__(self, size):
        self.size = size
        self.cache = []
        self.ele_count = 0
        self.front = 0
        self.rear = 0

    def find(self, ele):
        if ele not in self.cache:
            print("miss")
            self.cache.insert(0, ele)
            self.ele_count += 1
            if self.ele_count > self.size:
                self.cache = self.cache[:-1]
        else:
            print("hit")
            self.cache.remove(ele)
            self.cache.insert(0, ele)

    def print_cache(self):
        print(*self.cache)
