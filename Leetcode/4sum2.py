from collections import defaultdict
from typing import List

class Solution:

    #T: O(N^3) S: O(1)
    # def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        
    #     # Make map1 of sums of values A+B
    #     # Make map2 of sums of values of C + keys of map1
    #     # Res is values of D + keys of map2 that == 0

    #     # A -> i
    #     # B -> j
    #     # C -> k
    #     # D -> l

    #     # Values of A+B
    #     map1 = defaultdict(list)

    #     for ii, i in enumerate(A):
    #         for jj, j in enumerate(B):
    #             map1[i+j].append((ii, jj))

    #     map2 = defaultdict(list)
        
    #     for kk, k in enumerate(C):
    #         for ij in map1.keys():
    #             for ijtuple in map1[ij]:
    #                 ii, jj = ijtuple
    #                 map2[ij + k].append((ii, jj, kk))

    #     ans = 0

    #     # for ll, l in enumerate(D):
    #     for ll, l in enumerate(D):
    #         x = 0 - l
    #         if x in map2:
    #             ans += len(map2[x])

    #     return ans

    # T: O(N^2) S: O(N)
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:

        res = 0

        # key: sums of individual values in A and individual values in B 
        # value: count
        m = defaultdict(int)

        for a in A:
            for b in B:
                m[a+b] = m[a+b] + 1

        # for every c+d, if the inverse exists as a key in m1, add the value of that key to res
        for c in C:
            for d in D:
                v = -(c+d)
                if v in m:
                    res += m[v]

        return res

    # def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    #     cnt = 0
    #     m = {}
    #     for a in A:
    #         for b in B:
    #             m[a + b] = m.get(a + b, 0) + 1
    #     for c in C:
    #         for d in D:
    #             cnt += m.get(-(c + d), 0)
    #     return cnt

if __name__ == "__main__":
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]

    print(Solution().fourSumCount(A, B, C, D))