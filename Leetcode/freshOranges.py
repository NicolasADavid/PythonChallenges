from typing import List, Tuple

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid:
            return -1

        time = 0

        def rotAdjacent(col, row) -> List[Tuple[int, int]]:

            rotted = []

            # change from fresh to rotten and collect newly rotted
            def rot(col, row):
                #check bounds
                if col < 0 or col >= len(grid):
                    return
                
                if row < 0 or row >= len(grid[0]):
                    return

                if grid[col][row] == 1:
                    grid[col][row] = 2
                    rotted.append((col, row))

            # up
            rot(col-1, row)

            # down
            rot(col+1, row)

            # left
            rot(col, row-1)

            # right
            rot(col, row+1)

            return rotted

        def collectRotten() -> List[Tuple[int, int]]:
            result = []

            for colIdx, col in enumerate(grid):
                for rowIdx, orange in enumerate(col):
                    if orange == 2:
                        result.append((colIdx, rowIdx))

            return result

        def collectFresh() -> List[Tuple[int, int]]:
            result = []

            for colIdx, col in enumerate(grid):
                for rowIdx, orange in enumerate(col):
                    if orange == 1:
                        result.append((colIdx, rowIdx))

            return result

        # initially rotten oranges
        rottens = collectRotten()

        # repeat while rottens exist, replacing rottens with newly rotted
        while rottens:

            newRottens = []

            for rotten in rottens:
                # turn fresh into rotten oranges
                # collect the newly rotten oranges
                newRottens += rotAdjacent(rotten[0], rotten[1])

            # replace rottens with the newly rotten oranges. while will repeat until a loop produces no new rotten oranges.
            rottens = newRottens

            # if any oranges were rotted
            if rottens:
                # increment time
                time += 1

        # if any fresh oranges remain
        if collectFresh():
            return -1
        else:
            return time


if __name__ == "__main__":
    s = Solution()

    input = [[2,1,1],[1,1,0],[0,1,1]] #4

    r = s.orangesRotting(input)

    print(r)