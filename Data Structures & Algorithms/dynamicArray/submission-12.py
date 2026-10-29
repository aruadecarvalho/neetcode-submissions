class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * self.capacity
        return

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
        return

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        
        self.arr[self.size] = n 
        self.size += 1

        return

    def popback(self) -> int:
        self.size -= 1
        n = self.arr[self.size]

        return n

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        temp_arr = [0] * self.capacity
        for i in range (self.size):
            temp_arr[i] = self.arr[i]
        
        self.arr = temp_arr

        return

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity