from collections import deque
from typing import List
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        # Make deque of characters in s
        dq = deque([c for c in s])

        for op in shift:

            for _ in range(op[1]):

                if op[0]:
                    # right shift
                    dq.appendleft(dq.pop())

                else:
                    # left shift
                    dq.append(dq.popleft())

        return "".join(dq)

if __name__ == "__main__":
    print(Solution().stringShift(s = "abc", shift = [[0,1],[1,2]]))
    print(Solution().stringShift(s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]))