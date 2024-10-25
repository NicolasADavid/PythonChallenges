"""

- run the study on the main street of the city
- select a "block" of B contiguous houses
- match every household's income to the highest in this block

B = 3

    x    x     x    x     x    x 
   20k  500k   65k 50k  70k  100k
   --------------
   45 + 15 = 60k
        ---------------
        450k + 435k = 885k
   ----------------

find the block on which it is the cheapest to run this study (for a year)!



Sliding window

Size of B

Expanding:
    track:
        total income of the block
        highest income of the block
        maintain a mono queue

        if block is of size B: Track: Potential best answer = (highest income of block * size of the block) - total income of block

Contracting
    Track:
        if removing highest income (bottom of monoque), remove from mono queue. Replace highest block income with adjacent element of mono queue

        subtract from total income of block

"""
from typing import List
from collections import deque

def getBestBlockStudyCost(incomes: List[int], blockSize: int) -> int:

    left = 0
    right = -1

    blockBest = float("-inf")
    blockTotal = 0
    mono = deque()
    best = float("inf")

    while right < len(incomes) - 1:

        # print("left: ", left, " right: ", right)

        if right - left + 1 < blockSize:

            # expand

            right += 1
            new = incomes[right]
            blockTotal += new
            blockBest = max(blockBest, new)

            while mono and mono[-1] < new:
                mono.pop()
            
            mono.append(new)

            if right - left + 1 == blockSize:
                blockCost = (blockSize * blockBest) - blockTotal
                best = min(best, blockCost)

        else:

            # contract

            old = incomes[left]

            blockTotal -= old

            if old == mono[0]:
                mono.popleft()
                blockBest = mono[0]
            
            left += 1

    return best

# assert getBestBlockStudyCost([20,  500,   65, 50,  70,  100], 3) == 25
# assert getBestBlockStudyCost([100, 80, 50, 45, 40], 3) == 15
# assert getBestBlockStudyCost([100, 80, 50, 50, 50], 3) == 0
# assert getBestBlockStudyCost([100, 80, 50], 3) == 70
# assert getBestBlockStudyCost([100, 80, 40, 45, 50], 3) == 15
# assert getBestBlockStudyCost([1,1,1,2,1], 4) == 3