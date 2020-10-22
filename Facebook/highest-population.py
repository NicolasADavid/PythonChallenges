from typing import List

class Person:
    def __init__(self, born: int, died: int):
        self.born = born
        self.died = died

class Solution:
    def maxPopYear(self, people) -> int:
        born = {}
        died = {}

        minY = -1
        maxY = -1

        for p in people:
            born[p.born] = born.setdefault(p.born, 0) + 1
            died[p.died] = died.setdefault(p.died, 0) + 1
            minY = min(minY, p.born)
            maxY = max(maxY, p.died)

        alive = 0
        best = (-1, -1)


        # instead use iterors of the dicts in sorted order.
        # bIt = iter(sorted(d.iteritems()))
        # bIt = iter(sorted(born.keys()))
        # dIt = iter(sorted(died.keys()))
        
        for year in range(minY, maxY+1):
            # add born in year
            alive += born.setdefault(year, 0)
            # subtract died in year
            alive -= died.setdefault(year, 0)
            # compare to best
            if alive > best[1]:
                best = (year, alive)

        return best[0]

if __name__ == "__main__":
    s = Solution()
    p = []
    p.append(Person(1000, 1002))
    p.append(Person(1001, 1008))
    p.append(Person(1005, 1006))

    print(s.maxPopYear(p))

