from collections import deque

class Solution:
    # def convert(self, s: str, numRows: int) -> str:

    #     stacks = []

    #     # Create a stack for each row
    #     for _ in range(numRows):
    #         stacks.append([])

    #     r1 = range(numRows) # going down
    #     r2 = reversed(range(numRows)[1:-1]) # going up, excluding last and first
    #     rangeConcat = list(r1) + list(r2)

    #     offsets = deque() # for rotating the stack to use

    #     for x in rangeConcat:
    #         offsets.append(x)

    #     while s:
    #         stacks[offsets[0]].append(s[0])
    #         s = s[1:]
    #         offsets.rotate(1)

    #     output = ""

    #     for stack in stacks:
    #         output = output + "".join(stack)

    #     return output

    def convert(self, s: str, numRows:int) -> str:

        stacks = []

        # Create a stack for each row
        for _ in range(numRows):
            stacks.append([])

        # Create a range that goes down and up, all rows on down, only middle rows on up

        r1 = range(numRows) # going down
        r2 = reversed(range(numRows)[1:-1])

        rr = list(r1) + list(r2)

        offsets = deque(rr)

        output = []

        for c in s:
            stacks[offsets[0]].append(c)
            offsets.rotate(1)

        output = "".join(["".join(stack) for stack in stacks])

        return output

if __name__ == "__main__":
    # s = Solution()
    # input = "PAYPALISHIRING"
    # print(s.convert(input, 3)) # "PAHNAPLSIIGYIR"

    assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert Solution().convert("A", 1) == "A"
    assert Solution().convert("A", 2) == "A"