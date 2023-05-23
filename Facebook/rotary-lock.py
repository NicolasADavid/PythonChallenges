from typing import List


def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:

    solution = 0

    atNum = 1

    for targetNum in C:

        goDirect = abs(targetNum - atNum)
        goAround = abs(max(targetNum, atNum) - (min(targetNum, atNum) + N))

        distance = min(goDirect, goAround)

        print("Distance: ", distance)

        solution = solution + distance

        atNum = targetNum

    print(solution)

    return solution


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
        print(' Your output: ', output, end='')
        print()
    test_case_number += 1


if __name__ == "__main__":
    # n_1 = 3
    # m_1 = 3
    # c_1 = [1, 2, 3]
    # expected_1 = 2
    # output_1 = getMinCodeEntryTime(n_1, m_1, c_1)
    # check(expected_1, output_1)

    n2 = 10
    m2 = 4
    c2 = [9, 4, 4, 8]
    expected_2 = 11
    output_2 = getMinCodeEntryTime(n2, m2, c2)
    check(expected_2, output_2)

    # n3 = 10
    # m3 = 4
    # c3 = [9, 4, 4, 8]
    # expected_2 = 11
    # output_2 = getMinCodeEntryTime(n2, m2, c2)
    # check(expected_2, output_2)
