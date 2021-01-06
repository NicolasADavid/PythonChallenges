from collections import defaultdict

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        odds = 0
        counts = defaultdict(int)
        
        for c in s:

            counts[c] += 1

            if counts[c] % 2 != 0:
                odds += 1
            else:
                odds -= 1

        return odds <= 1