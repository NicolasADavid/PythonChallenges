from itertools import chain
from collections import deque

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        stacks = []

        # Create a stack for each row
        for _ in range(numRows):
            stacks.append([])

        range1 = range(numRows) # going down
        range2 = reversed(range(numRows)[1:-1]) # going up, excluding last and first
        range3 = chain(range1, range2) # combine ranges

        offsets = deque() # for rotating the stack to use

        for x in range3:
            offsets.append(x)

        while s:
            stacks[offsets[0]].append(s[0])
            s = s[1:]
            offsets.rotate(1)

        output = ""

        for stack in stacks:
            output = output + "".join(stack)

        return output


if __name__ == "__main__":
    s = Solution()
    input = "PAYPALISHIRING"
    print(s.convert(input, 3)) # "PAHNAPLSIIGYIR"