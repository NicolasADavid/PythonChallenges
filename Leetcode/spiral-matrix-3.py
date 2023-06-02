from collections import deque
from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        ans = []

        directions = deque(["r", "d", "l", "u"])

        rb = cStart + 1
        db = rStart + 1
        lb = cStart - 1
        ub = rStart - 1

        cc = cStart
        cr = rStart

        def checkSolution(cc, cr, tr,  tc, sol):
            if cc < tc and cc >= 0 and cr < tr and cr >= 0:
                # print(f"Add ({cr}, {cc})")
                sol.append([cr, cc])

        checkSolution(cc, cr, rows, cols, ans)

        while len(ans) < rows * cols:

            direction = directions.popleft()
            directions.append(direction)

            match direction:
                case "r":
                    while cc < rb:
                        # move
                        cc += 1
                        # check
                        checkSolution(cc, cr, rows, cols, ans)
                    else:
                        # move bound, change direction
                        rb += 1

                case "d":
                    while cr < db:
                        cr += 1
                        checkSolution(cc, cr, rows, cols, ans)
                    else:
                        db += 1

                case "l":
                    while cc > lb:
                        cc -= 1
                        checkSolution(cc, cr, rows, cols, ans)
                    else:
                        lb -= 1

                case "u":
                    while cr > ub:
                        cr -= 1
                        checkSolution(cc, cr, rows, cols, ans)
                    else:
                        ub -= 1

                case _:
                    pass

        return ans


if __name__ == "__main__":

    s = Solution()

    r = s.spiralMatrixIII(rows=1, cols=4, rStart=0, cStart=0)
    print(r)

    r = s.spiralMatrixIII(rows=5, cols=6, rStart=1, cStart=4)
    print(r)
