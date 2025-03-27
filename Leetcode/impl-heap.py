

"""

Complete binary tree

Heap is a complete binary tree, which means all levels of the tree are fully filled except possibly for the last level, which is filled from left to right.

Max heap
- A parent node is always greater than its children
- The root node is the largest element in the heap

"Binary": two children
Assigned from left to right

Heapify
- The process of converting a binary tree into a heap
- O(n) time complexity

Min heap
- A parent node is always smaller than its children
- The root node is the smallest element in the heap

Heap operations
- Peek O(1)
- Push O(log n)
- Pop O(log n)

Push
- Add a new element to the heap

Pop
- Remove the root element from the heap
- O(log n) time complexity ( because may have to heapify the tree)

As an array
Root is at index 0
Parent of node at index i is at (i-1) // 2
Left child of node at index i is at 2i + 1
Right child of node at index i is at 2i + 2

"""

from typing import List

class Heap:

    def __init__(self, minHeap: True):
        self.minHeap = minHeap
        self.heap = []

    def compare(self, n1, n2) -> bool:
        if self.minHeap:
            return n1 < n2
        else:
            return n1 > n2

    def peek(self) -> int:
        if not self.heap:
            return None
        return self.heap[0]

    def insert(self, val: int) -> None:
        # insert at next available spot
        self.heap.append(val)
        # heap (bottom to top)
        self.perlocate_up()

    def pop(self) -> int:

        if not self.heap:
            return None
        
        lastElementIdx = len(self.heap) - 1
        
        # swap root with last element
        self.swap(0, lastElementIdx)
        # remove/return last element
        val = self.heap.pop()
        # heap (top to bottom)
        self.perlocate_down()
        return val

    def swap(self, i1, i2) -> None:
        self.heap[i1], self.heap[i2] = self.heap[i2], self.heap[i1]

    def perlocate_up(self) -> None:
        if len(self.heap) == 1:
            return
        
        # heap (bottom to top)
        # Last val is at self.heap[-1]
        # index of last val is len(self.heap) - 1

        # if child is index i, parent will be (i - 1) // 2
        currIdx = len(self.heap) - 1
        parentIdx = (currIdx - 1) // 2

        def curVal() -> int:
            return self.heap[currIdx]
        def parentVal() -> int:
            return self.heap[parentIdx]

        # if parent is greater than child, swap
        while currIdx != 0 and self.compare(curVal(), parentVal()):
            self.swap(currIdx, parentIdx)
            currIdx = parentIdx
            parentIdx = (currIdx - 1) // 2

    def perlocate_down(self) -> None:
        # heap (top to bottom)
        currIdx = 0

        # Left child of node at index i is at 2i + 1
        def leftChildIdx() -> int:
            return (2 * currIdx) + 1

        # Right child of node at index i is at 2i + 2
        def rightChildIdx() -> int:
            return (2 * currIdx) + 2

        def leftChildVal() -> int:
            if leftChildIdx() >= len(self.heap):
                if self.minHeap:
                    return float("inf")
                else:
                    return float("-inf")
            else:
                return self.heap[leftChildIdx()]
        def rightChildval() -> int:
            if rightChildIdx() >= len(self.heap):
                if self.minHeap:
                    return float("inf")
                else:
                    return float("-inf")
            else:
                return self.heap[rightChildIdx()]

        bestChildIdx = None

        def updateBestChildIdx():
            nonlocal bestChildIdx
            if self.compare(leftChildVal(), rightChildval()):
                bestChildIdx = leftChildIdx()
            else:
                bestChildIdx = rightChildIdx()

        updateBestChildIdx()

        while bestChildIdx < len(self.heap) and self.compare(self.heap[bestChildIdx], self.heap[currIdx]):
            self.swap(currIdx, bestChildIdx)
            updateBestChildIdx()

# Test minHeap
minHeap = Heap(minHeap=True)
minHeap.insert(3)
minHeap.insert(2)
minHeap.insert(1)
assert minHeap.peek() == 1
assert minHeap.pop() == 1
assert minHeap.peek() == 2
minHeap.insert(15)
minHeap.insert(5)
assert minHeap.pop() == 2
assert minHeap.pop() == 3
assert minHeap.pop() == 5
assert minHeap.pop() == 15

# Test maxHeap
maxHeap = Heap(minHeap=False)
maxHeap.insert(3)
maxHeap.insert(2)
maxHeap.insert(1)
assert maxHeap.peek() == 3
assert maxHeap.pop() == 3
assert maxHeap.peek() == 2
maxHeap.insert(15)
maxHeap.insert(5)
assert maxHeap.pop() == 15
assert maxHeap.pop() == 5
assert maxHeap.pop() == 2
assert maxHeap.pop() == 1