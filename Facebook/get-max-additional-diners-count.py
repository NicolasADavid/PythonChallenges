from typing import List, Set
# Write any import statements here


def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:

    additionalDiners = 0
    chairsBehind = K
    chairsAhead = 0
    S2 = set(S)

    for i in range(N):

        # is seat occupied?
        # seatOccupied if i + 1 in S2
        seatOccupied = i + 1 in S2

        if seatOccupied:
            # reset
            chairsBehind = chairsAhead = 0
            continue

        # First, need K + 1 chairs behind. +1 for the target chair to seat a diner in.
        if chairsBehind >= K + 1:

            chairsAhead = chairsAhead + 1

            # Second, need k chairs ahead of the target chair
            if chairsAhead >= K:

                # count
                additionalDiners = additionalDiners + 1

                # reset
                chairsBehind = chairsAhead
                chairsAhead = 0

        else:
            # This chair will count as an empty chair behind potential target chair on next iteration.
            chairsBehind = chairsBehind + 1
            continue

    if chairsBehind == K + 1:
        additionalDiners = additionalDiners + 1

    return additionalDiners


# if __name__ == "__main__":
#     # print("Hello")
#     N = 10
#     K = 1
#     M = 2
#     # S = [2, 6]
#     S = [6, 2]
#     r = getMaxAdditionalDinersCount(N, K, M, S)
#     print(r)

#     N = 15
#     K = 2
#     M = 3
#     S = [11, 6, 14]
#     r = getMaxAdditionalDinersCount(N, K, M, S)
#     print(r)
