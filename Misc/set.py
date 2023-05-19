from typing import Set

if __name__ == "__main__":
    s = {1, 2, 3}
    t = {3, 4, 5}
    s2 = s.copy()

    # s.add(1, 2, 3)
    # s.add(2)
    # s.add(3)

    # print(s < t)
    # print(s > t)
    # print(s == t)
    # print(s != t)

    print(s | t)
    print(s & t)
    print(s - t)
    print(s ^ t)

    print(s)
