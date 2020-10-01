class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.k = k
        self.items = 0

        self.front = None
        self.back = None

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """

        if self.isFull():
            return False

        new = Node(value)

        if self.items == 0:
            self.front = self.back = self.front.next = self.front.prev = self.back.next = self.back.prev = new
        else:
            new.next = self.front
            new.prev = self.back
            self.back = new
            self.front.prev = new
            self.back.prev.next = new

        self.items += 1

        return True
        
    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """

        if self.isEmpty():
            return False

        if self.items == 1:
            self.back = None
            self.front = None
        else:
            next = self.front.next
            self.back.next = next
            next.prev = self.back
            self.front = next

        self.items -= 1

        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """

        if self.front:
            return self.front.val
        else:
            return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """

        if self.back:
            return self.back.val
        else:
            return -1
        
    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """

        return self.items == 0
        
    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """

        return self.items == self.k
        

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(10)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()