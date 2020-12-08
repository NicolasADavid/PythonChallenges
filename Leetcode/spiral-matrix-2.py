from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        out = [ [0] * n for _ in range(n) ]
        num = 1
        l = t = 0
        r = b = n

        while num <= n**2:
            for i in range(l, r):
                out[t][i] = num
                num += 1
            for i in range(t+1, b):
                out[i][r-1] = num
                num += 1
            for i in range(r-2, l, -1):
                out[b-1][i] = num
                num += 1
            for i in range(b-1, t, -1):
                out[i][l] = num
                num += 1
            l += 1
            t += 1
            r -= 1
            b -= 1
        return out

if __name__ == "__main__":
    s = Solution()
    # print(s.generateMatrix(1))
    print(s.generateMatrix(4))