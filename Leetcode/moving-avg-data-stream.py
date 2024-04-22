from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = deque()
        self.sum = 0

    def next(self, val: int) -> float:
        self.q.append(val)
        self.sum += val
        if len(self.q)>self.size:
            self.sum -= self.q.popleft()
        
        return self.sum / len(self.q)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
    
if __name__ == "__main__":
    # ["MovingAverage","next","next","next","next"]
    # [[3],[1],[10],[3],[5]]
    ma = MovingAverage(3)
    print(ma.next(1))
    print(ma.next(10))
    print(ma.next(3))
    print(ma.next(5))