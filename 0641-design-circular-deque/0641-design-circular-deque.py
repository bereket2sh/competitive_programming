class MyCircularDeque:

    def __init__(self, k: int):
        self.current = 0
        self.arr = [-1] * k
        self.front = 0
        self.rear = 0
        self.size = k
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.arr[self.front] = value
            self.current += 1
            return True
        self.front = (self.front - 1) % self.size
        self.arr[self.front] = value
        self.current += 1
        # print(self.current, self.arr)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.arr[self.rear] = value
            self.current += 1
            return True
        self.rear = (self.rear + 1) % self.size
        self.arr[self.rear] = value
        self.current += 1
        # print(self.current, self.arr)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.arr[self.front] = -1
        self.front = (self.front + 1) % self.size
        self.current -= 1
        if self.isEmpty():
            self.front = self.rear
        
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.arr[self.rear] = -1
        self.rear = (self.rear - 1) % self.size
        self.current -= 1
        if self.isEmpty():
            self.front = self.rear
        return True

    def getFront(self) -> int:
        return self.arr[self.front]

    def getRear(self) -> int:
        return self.arr[self.rear]

    def isEmpty(self) -> bool:
        return self.current == 0

    def isFull(self) -> bool:
        return self.current == self.size
        
    

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()