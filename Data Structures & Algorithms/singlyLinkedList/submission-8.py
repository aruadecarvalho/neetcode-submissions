class ListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        curr = self.head
        i = 0

        while curr is not None:
            if i == index:
                return curr.value
            
            curr = curr.next
            i += 1
        
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
    
        if index == 0:
            self.head = self.head.next

            if self.head is None:
                self.tail = None
            
            return True

        predecessor = self.head
        i = 0

        while i < index - 1 and predecessor.next is not None:
            predecessor = predecessor.next
            i += 1
        
        if predecessor.next is None:
            return False
        
        predecessor.next = predecessor.next.next

        if predecessor.next is None:
            self.tail = predecessor
        
        return True

    def getValues(self) -> List[int]:
        values = []
        curr = self.head

        while curr is not None:
            values.append(curr.value)
            curr = curr.next
        
        return values