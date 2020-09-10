class StockSpanner:

    def __init__(self):
        self.stack = []
        # (price, weight)

    def next(self, price: int) -> int:
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]

        self.stack.append((price, weight))

        return weight


if __name__ == "__main__":
    s = StockSpanner()

    input = [11, 3, 9, 5, 6, 4, 7]
    
    for inp in input:
        print(s.next(inp))
