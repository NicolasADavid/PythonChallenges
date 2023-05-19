from typing import List
from collections import defaultdict, deque

# Write any import statements here


def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:

    def def_value():
        return 0

    sol = 0
    e = defaultdict(def_value)
    dq = deque()

    for d in D:

        # haven't eaten recently, eat
        if e[d] == 0:

            # count eaten
            sol = sol + 1

            # track have eaten this dish
            e[d] = e[d] + 1
            dq.append(d)

            # forget have eaten dishes
            if len(dq) > K:
                le = dq.popleft()
                e[le] = e[le] - 1

    return sol


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number,
              ': Expected ', sep='', end='')
        # printInteger(expected)
        print(expected)
        print(' Your output: ', end='')
        # printInteger(output)
        print(output)
        print()
    test_case_number += 1


if __name__ == "__main__":

    n1 = 6
    d1 = [1, 2, 3, 3, 2, 1]
    k1 = 1
    expected_1 = 5
    output_1 = getMaximumEatenDishCount(n1, d1, k1)
    check(expected_1, output_1)

    n2 = 6
    d2 = [1, 2, 3, 3, 2, 1]
    k2 = 2
    expected_2 = 4
    output_2 = getMaximumEatenDishCount(n2, d2, k2)
    check(expected_2, output_2)

    n3 = 7
    d3 = [1, 2, 1, 2, 1, 2, 1]
    k3 = 2
    expected_3 = 2
    output_3 = getMaximumEatenDishCount(n3, d3, k3)
    check(expected_3, output_3)
