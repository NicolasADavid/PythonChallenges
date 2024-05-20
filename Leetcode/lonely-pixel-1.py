from typing import List
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:

        if not picture:
            return 0

        n = len(picture)
        m = len(picture[0])

        rows = [0] * n
        cols = [0] * m

        # Traverse input, tracking how many 'B's are found in each row and each column. O(NxM)
        for i in range(n):
            for j in range(m):
                if picture[i][j] == "B":
                    rows[i] += 1
                    cols[j] += 1

        # Traverse input, for each B, check how many 'B's belong to the same row and column. If 1 each, incr answer.
        ans = 0
        for i in range(n):
            for j in range(m):
                if picture[i][j] == "B":
                    if rows[i] == 1 and cols[j] == 1:
                        ans += 1

        return ans


if __name__ == "__main__":
    # print(Solution().findLonelyPixel(picture = [["W","W","B"],["W","B","W"],["B","W","W"]])) # 3
    print(Solution().findLonelyPixel(picture = [["W","W",],["W","B",],["B","W",]]))
    print(Solution().findLonelyPixel(picture = [["W","W","B"],["W","B","W"]]))
    # print(Solution().findLonelyPixel(picture = [["W","W","B", "W"],["W","B","W", "W"]]))

    # print(Solution().findLonelyPixel(picture = [["B","B","B"]])) # 0

    