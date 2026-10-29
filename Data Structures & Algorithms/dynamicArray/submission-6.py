class DynamicArray:
    capacity = 1
    size = 0
    arr = [0]

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * capacity
        return

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
        return

    def pushback(self, n: int) -> None:
        if self.size + 1 > self.capacity:
            self.resize()
        
        self.arr[self.size] = n 
        self.size += 1

        return

    def popback(self) -> int:
        self.size -= 1
        n = self.arr[self.size]
        self.arr[self.size] = 0

        return n

    def resize(self) -> None:
        resized_capacity = self.capacity * 2
        temp_arr = [0] * resized_capacity
        for i in range (self.capacity):
            temp_arr[i] = self.arr[i]
        
        self.arr = temp_arr
        self.capacity = resized_capacity

        return

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity