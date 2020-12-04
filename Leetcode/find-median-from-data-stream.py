import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """

        # middle existing means there's a middle element that is automatically the median
        # heapsizes are always maintained equal

        self.middle = None
        self.leftHeap = []
        self.rightHeap = []
        
    def addNum(self, num: int) -> None:

        # values in leftHeap are inverted so that the highest number is at the top
        # can't do this if heaps are empty

        # If nothing has been inserted to left or right and there is no middle
        if not len(self.leftHeap) and not len(self.rightHeap):
            if not self.middle:
                self.middle = num
                return None

        # If middle: put middle in one stack and num in the other
        if self.middle is not None:
            # if num > self.middle Move num to R and middle to L

            # if num is greater than middle, insert to rightHeap. middle to leftHeap
            # if num is less than middle, insert to leftHeap. middle to rightHeap
            # if num is equal to middle, insert num to both

            if num > self.middle:
                heapq.heappush(self.rightHeap, num)
                heapq.heappush(self.leftHeap, self.middle * -1)

            elif num < self.middle:
                heapq.heappush(self.rightHeap, self.middle)
                heapq.heappush(self.leftHeap, -num)

            else:
                heapq.heappush(self.rightHeap, num)
                heapq.heappush(self.leftHeap, -num)

            self.middle = None

        # Determine if middle should be num, top of Left, or top of Right
        else:

            lt = -(self.leftHeap[0])
            rt = self.rightHeap[0]
            
            if lt <= num <= rt:
                self.middle = num

            else:
                if num > rt:
                    self.middle = heapq.heappushpop(self.rightHeap, num)
                if num < lt:
                    self.middle = -(heapq.heappushpop(self.leftHeap, -num))

    def findMedian(self) -> float:

        if self.middle is not None: return self.middle

        rt = self.rightHeap[0]
        lt = self.leftHeap[0] * -1

        return (lt + rt) / 2        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


if __name__ == "__main__":
    s = MedianFinder()

    # s.addNum(1)
    # print(s.findMedian())
    # s.addNum(2)
    # print(s.findMedian())
    # s.addNum(5)
    # print(s.findMedian())


    # s.addNum(0)
    # s.addNum(0)
    # s.findMedian()

    s.addNum(6)
    print(s.findMedian())
    s.addNum(10)
    print(s.findMedian())
    s.addNum(2)
    print(s.findMedian())
    s.addNum(6)
    print(s.findMedian())
    s.addNum(5)
    print(s.findMedian())
    s.addNum(0)
    print(s.findMedian())
    s.addNum(6)
    print(s.findMedian())
    s.addNum(3)
    print(s.findMedian())
    s.addNum(1)
    print(s.findMedian())
    s.addNum(0)
    print(s.findMedian())
    s.addNum(0)
    print(s.findMedian())