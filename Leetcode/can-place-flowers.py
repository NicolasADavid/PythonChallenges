from typing import List

class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if not n: return True

        p = 0

        for idx, spot in enumerate(flowerbed):

            before = flowerbed[idx-1] if idx-1 >= 0 else 0
            after = flowerbed[idx+1] if idx+1 < len(flowerbed) else 0

            if 1 not in [before, spot, after]:
                p += 1
                flowerbed[idx] = 1
                if p == n: return True
        
        return False

if __name__ == "__main__":
    s = Solution()

    print(s.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))