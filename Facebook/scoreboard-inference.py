from typing import List
# Write any import statements here


def getMinProblemCount(N: int, S: List[int]) -> int:

    def isOdd(number):
        return number % 2 == 1

    hasOdd = False

    solution = 0

    for s in S:
        if isOdd(s):
            hasOdd = True

    biggest = max(S)

    if isOdd(biggest):
        solution = ((biggest - 1) / 2) + 1
    else:
        if hasOdd:
            solution = (biggest / 2) + 1
        else:
            solution = biggest / 2

    return int(solution)


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
              ': Expected ', expected, sep='', end='')
        print(' Your output: ', output, end='')
        print()
    test_case_number += 1


if __name__ == "__main__":
    n1 = 6
    s1 = [1, 2, 3, 4, 5, 6]
    expected_1 = 4
    output_1 = getMinProblemCount(n1, s1)
    check(expected_1, output_1)

    n2 = 10
    s2 = [4, 3, 3, 4]
    expected_2 = 3
    output_2 = getMinProblemCount(n2, s2)
    check(expected_2, output_2)

    n3 = 4
    s3 = [2, 4, 6, 8]
    expected_3 = 4
    output_3 = getMinProblemCount(n3, s3)
    check(expected_3, output_3)
