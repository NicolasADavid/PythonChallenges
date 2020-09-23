import heapq

class Solution:
    def reorganizeString(self, S: str) -> str:

        # Count occurences of each letter O(n)
        d = {}
        for c in S:
            d[c] = d.setdefault(c, 0) + 1

        # Create heap of letters sorted by their number of occurences O(n*lg(n)).
        # Use negative so larger numbers have higher priority.
        pq = []
        for (letter, occurences) in d.items():
            heapq.heappush(pq, (-occurences, letter))

        res = []

        while len(pq) >= 2:
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)

            res.extend([ch1, ch2])

            if nct1 + 1: heapq.heappush(pq, (nct1 + 1, ch1))
            if nct2 + 1: heapq.heappush(pq, (nct2 + 1, ch2))

        # If there is more than one letter left to place, no solution
        if pq and pq[0][0] < -1: return ""

        # If there is one letter left to place, place it at the end
        return "".join(res) + (pq[0][1] if pq else '')

if __name__ == "__main__":
    s = Solution()

    print(s.reorganizeString("aaaab"))
