# Write any import statements here

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:

    def countPhotos(C: str, X: int, Y: int) -> int:

        solutions = 0

        bl = -1
        bf = 0
        bc = 0

        pl = -1
        pf = 0
        pc = 0

        for i in range(len(C)):

            # 1 move B window

            while bl < i + Y:
                bl = bl + 1
                if bl < len(C) and C[bl] == "B":
                    bc = bc + 1

            while bf < i + X:
                if bf < len(C) and C[bf] == "B":
                    bc = bc - 1
                bf = bf + 1

            # 2 move P window

            while pl < i - X:
                pl = pl + 1
                if pl < len(C) and C[pl] == "P":
                    pc = pc + 1

            while pf < i - Y:
                if pf < len(C) and C[pf] == "P":
                    pc = pc - 1
                pf = pf + 1

            # 3 if Actor, count solutions

            if C[i] == "A":
                solutions = solutions + (pc * bc)

        return solutions

    fwd = countPhotos(C, X, Y)
    bwd = countPhotos(C[::-1], X, Y)

    return fwd + bwd


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

    n1 = 5
    c1 = "APABA"
    x1 = 1
    y1 = 2
    expected_1 = 1
    output_1 = getArtisticPhotographCount(n1, c1, x1, y1)
    check(expected_1, output_1)

    n2 = 5
    c2 = "APABA"
    x2 = 2
    y2 = 3
    expected_2 = 0
    output_2 = getArtisticPhotographCount(n2, c2, x2, y2)
    check(expected_2, output_2)

    n3 = 8
    c3 = ".PBAAP.B"
    x3 = 1
    y3 = 3
    expected_3 = 3
    output_3 = getArtisticPhotographCount(n3, c3, x3, y3)
    check(expected_3, output_3)

    # Add your own test cases here
