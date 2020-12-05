import math
import heapq

class Solution:

    # def kthFactor(self, n: int, k: int) -> int:
    #     factors = [x for x in range(1, n+1) if n % x == 0]
    #     return factors[k-1] if k <= len(factors) else -1

    def kthFactor(self, n: int, k: int) -> int:

        # Only need to iterate up to floor(sqrt(n))
        # When x is a divisor of n, n/x is also a divisor of n. Add both to heap.
        # Maintain heap at size k
        # Return heap[0] if len(h) == k else -1

        h = []

        for x in range(1, math.floor(math.sqrt(n) + 1)):

            if n % x == 0:

                new = [x, int(n/x)] if x != int(n/x) else [x]

                for item in new:

                    if len(h) < k:
                        heapq.heappush(h, -item)
                    else:
                        heapq.heappushpop(h, -item)
        
        return -h[0] if len(h) == k else -1

        
if __name__ == "__main__":
    s = Solution()
    # print(s.kthFactor(20, 3))
    # print(s.kthFactor(12, 3))
    # print(s.kthFactor(7, 2))
    print(s.kthFactor(4, 4))