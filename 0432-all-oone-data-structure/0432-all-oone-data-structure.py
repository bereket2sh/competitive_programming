class AllOne:

    def __init__(self):
        self.dic = defaultdict(int)
        

    def inc(self, key: str) -> None:
        self.dic[key] += 1
        

    def dec(self, key: str) -> None:
        self.dic[key] -= 1
        if self.dic[key] == 0:
            del self.dic[key]
        

    def getMaxKey(self) -> str:
        ans = ""
        _max = 0
        for key, value in self.dic.items():
            if value > _max:
                ans = key
                _max = value
        return ans

    def getMinKey(self) -> str:
        ans = ""
        _max = float('inf')
        for key, value in self.dic.items():
            if value < _max:
                ans = key
                _max = value
        return ans


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()