class MyHashSet:

    def __init__(self):
        self.hash = {}

    def add(self, key: int) -> None:
        self.hash[key] = 1
   

    def remove(self, key: int) -> None:
        if key in self.hash:
            self.hash[key] = 0
        

    def contains(self, key: int) -> bool:
        return True if key in self.hash and self.hash[key] > 0 else False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)