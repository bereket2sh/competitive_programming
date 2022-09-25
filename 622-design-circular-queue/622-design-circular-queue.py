class MyCircularQueue:

    def __init__(self, k: int):
        self.n = k
        self.queue = [-1] * k
        self.f,self.r = -1, -1
        self.count = 0
        
    def enQueue(self, value: int) -> bool:
        if self.count == self.n:
            return False
        if self.count == 0:
            self.f += 1
        self.r = (self.r + 1) % self.n
        self.queue[self.r] = value
        self.count += 1
        return True        

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        if self.count == 1:
            self.f, self.r = -1, -1
        else:
            self.f =( self.f + 1) % self.n
        self.count -= 1
        return True
        

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.f]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.r]

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.count == self.n:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()